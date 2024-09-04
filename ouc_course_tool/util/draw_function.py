import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_course_table(course_list: list[Course]):
    # 指定中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    # 定义一周的天数和每天的课程节次
    days = ['一', '二', '三', '四', '五', '六', '日']
    periods = list(map(lambda x: x - 1, list(range(1, 13))))  # 假设每天有 12 节课

    # 创建绘图对象
    fig, ax = plt.subplots(figsize=(10, 7))

    # 绘制课程表的背景网格
    ax.set_xlim(0, 7)
    ax.set_ylim(1, 13)
    ax.set_xticks([i for i in range(7)])
    ax.set_yticks([i for i in range(1, 13)])  # 调整 y 轴的刻度，使其与 periods 匹配
    ax.set_xticklabels(days)
    ax.set_yticklabels(periods)
    ax.grid(True)

    # 使用 colormap 生成浅色且分辨度高的颜色
    cmap = plt.colormaps['Pastel1']  # 选择 Pastel1 颜色映射
    colors = cmap(np.linspace(0, 1, len(course_list)))  # 生成 len(course_list) 个颜色

    # 绘制每门课程的块
    for i, temp_course in enumerate(course_list):
        course_name = temp_course.course_name.split(']')[1]
        if len(course_name) > 6:
            course_name = course_name[:6] + "..."
        color = colors[i]  # 为每个课程分配一种颜色
        for schedule in temp_course.get_class_time_list():  # 如果一个课程有多个时间安排
            day_index = days.index(schedule.day_of_week)
            start_period = schedule.start_period
            end_period = schedule.end_period

            # 在表格上绘制课程
            rect = patches.Rectangle((day_index, start_period), 1, end_period - start_period + 1,
                                     edgecolor='black', facecolor=color, linewidth=1)
            ax.add_patch(rect)
            ax.text(day_index + 0.5, start_period + 0.5 * (end_period - start_period + 1),
                    course_name, ha='center', va='center', fontsize=10)

    # 设置标题和标签
    plt.title('课程表')
    plt.xlabel('星期')
    plt.ylabel('节次')

    # 显示图表
    plt.show()