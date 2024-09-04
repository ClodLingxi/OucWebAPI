import hashlib
import base64
from io import BytesIO
from logging import Logger

from PIL import Image
import pytesseract
import cv2
import numpy as np
from datetime import datetime, timezone, timedelta

import requests
import re

from ouc_course_tool.config import LoginConfig

class AccountValidation:
    _LOGIN_URL = 'http://jwgl.ouc.edu.cn/cas/login.action'
    _CAPTCHA_URL = 'http://jwgl.ouc.edu.cn/cas/genValidateCode'

    _MAX_RECOGNIZE_TIME = 10
    _MAX_LOGIN_TIME = 5

    def __init__(self, config: LoginConfig):
        self.config = config
        self.logger = Logger('AccountValidation')

    @staticmethod
    def _md5_hash(text):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    @staticmethod
    def _base64_encode(text):
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')

    def _get_encoded_username_and_password(self, username, password, session_id, rand_number):
        encoded_username = self._base64_encode(username + ";;" + session_id)
        hashed_password = self._md5_hash(self._md5_hash(password) + self._md5_hash(rand_number.lower()))
        return encoded_username, hashed_password

    @staticmethod
    def _rand_number_validation(rand_number):
        rand_number = re.sub('[^a-zA-Z0-9]', '', rand_number)
        rand_number = rand_number.replace(' ', '')
        if len(rand_number) != 4:
            return None
        return rand_number

    def _recognize_captcha(self, image):
        pytesseract.pytesseract.tesseract_cmd = self.config.get_tesseract_path()
        img = image.convert('L')
        img = np.array(img)
        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = Image.fromarray(img)
        text = pytesseract.image_to_string(img)
        return text.strip()

    def _get_raw_captcha_and_session_id(self):
        offset = timedelta(hours=8)
        tz = timezone(offset, name="中国标准时间")
        now = datetime.now(tz)
        date_time = now.strftime('%a %b %d %Y %H:%M:%S GMT%z (%Z)')
        respond = (
            requests.get(self._CAPTCHA_URL, params={"dateTime": date_time}, headers=self.config.get_captcha_headers()))
        cookies = respond.cookies
        if len(cookies) == 0:
            return respond.content, self.config.get_session_id()

        return respond.content, respond.cookies.get('JSESSIONID')

    def get_rand_number_and_session_id(self):
        recognize_time = self._MAX_RECOGNIZE_TIME

        while recognize_time:
            raw_captcha, session_id = self._get_raw_captcha_and_session_id()
            if raw_captcha.startswith('<!DOCTYPE html>'.encode('utf-8')):
                return None, session_id

            captcha_image = Image.open(BytesIO(raw_captcha))
            rand_number = self._recognize_captcha(captcha_image)
            rand_number = self._rand_number_validation(rand_number)
            if rand_number is not None:
                return rand_number, session_id
            recognize_time -= 1

        return None, None

    def get_login_raw_result_and_session_id(self):
        rand_number, session_id = self.get_rand_number_and_session_id()
        if rand_number is None or session_id is None:
            return None, None

        encoded_username, hashed_password = self._get_encoded_username_and_password(username=self.config.get_username(),
                                                                                     password=self.config.get_password(),
                                                                                     session_id=session_id,
                                                                                     rand_number=rand_number)
        p_username = "_u" + rand_number
        p_password = "_p" + rand_number
        params = {
            p_username: encoded_username,
            p_password: hashed_password,
            "randnumber": rand_number,
            "isPasswordPolicy": "1",
            "txt_mm_expression": "12",
            "txt_mm_length": "8",
            "txt_mm_userzh": "0"
        }

        self.config.set_session_id(session_id)

        # print("Start login " + str(self.config.get_url()))
        response = requests.post(self.config.get_url(), params=params, headers=self.config.get_headers(), timeout=(10, 10))
        # print("End login " + str(self.config.get_url()))

        return response.json(), session_id

    def get_login_session_id(self):
        time = self._MAX_LOGIN_TIME
        while time:
            result, session_id = self.get_login_raw_result_and_session_id()
            message = result.get('message')
            if message == '操作成功!':
                return session_id
            elif message == '验证码有误!':
                time -= 1
            else:
                print("err" + result)
                break

        return None