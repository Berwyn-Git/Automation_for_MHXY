# -*- coding: utf-8 -*-

import os
import pyautogui

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 图像资源目录
IMAGE_DIR = os.path.join(PROJECT_ROOT, "images")
FLAG_DIR = os.path.join(IMAGE_DIR, "flag")  # 标识图像目录
SUB_DIR = os.path.join(IMAGE_DIR, "sub")    # 子图像目录
DATA_DIR = os.path.join(IMAGE_DIR, "data")  # 训练数据目录
MAP_DIR = os.path.join(IMAGE_DIR, "maps")   # 地图图像目录

# 日志目录
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

# 模型目录
MODEL_DIR = os.path.join(PROJECT_ROOT, "model")
MODEL_PATH = os.path.join(MODEL_DIR, "mhxy.h5")  # 模型文件路径

# 截图目录
SCREENSHOT_DIR = os.path.join(IMAGE_DIR, "screenshots")

# 屏幕尺寸
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# 按键映射
KEY_MAPPING = {
    "ALT+Q": ("alt", "q"),
    "F8": "f8",
    "TAB": "tab",
}

# 默认阈值
DEFAULT_THRESHOLD = 0.8

# 默认等待时间（秒）
DEFAULT_WAIT_TIME = 1

# 默认重试次数
DEFAULT_RETRY_TIMES = 3

# 默认重试延迟（秒）
DEFAULT_RETRY_DELAY = 1

# 默认重试倍数
DEFAULT_RETRY_BACKOFF = 2

# 日志格式
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# 日志级别
LOG_LEVEL = "INFO"

if __name__ == '__main__':
    # 示例：打印常量
    print(f"项目根目录: {PROJECT_ROOT}")
    print(f"图像资源目录: {IMAGE_DIR}")
    print(f"日志目录: {LOG_DIR}")
    print(f"模型目录: {MODEL_DIR}")
    print(f"屏幕尺寸: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
