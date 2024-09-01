import hashlib
import base64
from io import BytesIO

from PIL import Image
import pytesseract
import cv2
import numpy as np
from datetime import datetime, timezone, timedelta

import requests


class AccountValidation:
    _LOGIN_URL = 'http://jwgl.ouc.edu.cn/cas/login.action'
    _CAPTCHA_URL = 'http://jwgl.ouc.edu.cn/cas/genValidateCode'

    def __init__(self, config):
        self.username = config['username']
        self.password = config['password']

    @staticmethod
    def _md5_hash(text):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    @staticmethod
    def _base64_encode(text):
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')

    @staticmethod
    def _recognize_captcha(image):
        pytesseract.pytesseract.tesseract_cmd = 'D:/Tools/Tesseract/tesseract.exe'
        img = image.convert('L')
        img = np.array(img)
        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        img = Image.fromarray(img)
        text = pytesseract.image_to_string(img)
        return text.strip()

    def _get_raw_captcha_and_session(self):
        offset = timedelta(hours=8)
        tz = timezone(offset, name="中国标准时间")
        now = datetime.now(tz)
        date_time = now.strftime('%a %b %d %Y %H:%M:%S GMT%z (%Z)')
        respond = requests.get(self._CAPTCHA_URL, params={"dateTime": date_time})
        return respond.content, respond.cookies

    def get_rand_number_and_session_id(self):
        raw_captcha, cookies = self._get_raw_captcha_and_session()
        captcha_image = Image.open(BytesIO(raw_captcha))
        rand_number = self._recognize_captcha(captcha_image)
        return rand_number, cookies.values()[0]


    def login(self):
        rand_number, session_id = self.get_rand_number_and_session_id()
        hashed_password = self._md5_hash(self._md5_hash(self.password) + self._md5_hash(rand_number.lower()))
        encoded_username = self._base64_encode(self.username + ";;" + session_id)
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
        response = requests.post(self._LOGIN_URL, params=params)

        return response.text
