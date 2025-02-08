# -*- coding: utf-8 -*-

from tasks.base_task import BaseTask
from utils.auto import AutoController
from utils.screen import Screen
from utils.logger import logger
from utils.util import log_errors

class ShimenTask(BaseTask):
    def __init__(self):
        """
        初始化师门任务
        """
        super().__init__("师门任务")
        self.auto_controller = AutoController()
        self.screen = Screen()

    @log_errors
    def check_condition(self):
        """
        检查是否领取师门任务

        1. 按下 ALT+Q，打开任务栏。
        2. 检查任务栏中是否有 [百晓任务] 和 [师门任务]。
        """
        logger.info("检查是否领取师门任务")
        self.auto_controller.press_key('ALT+Q')
        if self.screen.find_text("百晓任务") and self.screen.find_text("师门任务"):
            logger.info("已领取师门任务")
            return True
        else:
            logger.info("未领取师门任务")
            return False

    @log_errors
    def execute_action(self):
        """
        执行师门任务

        1. 按下 F8 使用技能，回到门派。
        2. 按下 TAB 自动寻路至门派师傅。
        3. 点击门派师傅，领取师门任务。
        """
        logger.info("开始执行师门任务")

        # 按下 F8 使用技能，回到门派
        logger.info("按下 F8 使用技能，回到门派")
        self.auto_controller.press_key("F8")
        if self.screen.check_map("门派地图"):
            logger.info("成功回到门派")
        else:
            logger.warning("回到门派失败")
            return

        # 按下 TAB 自动寻路至门派师傅
        logger.info("按下 TAB 自动寻路至门派师傅")
        self.auto_controller.press_key("TAB")
        if self.screen.find_text("门派师傅"):
            logger.info("成功找到门派师傅")
            self.auto_controller.click("门派师傅")
        else:
            logger.warning("未找到门派师傅")
            return

        # 点击领取师门任务
        logger.info("点击领取师门任务")
        if self.screen.check_dialog("领取师门任务"):
            self.auto_controller.click("领取师门任务")
            logger.info("成功领取师门任务")
        else:
            logger.warning("领取师门任务失败")

    @log_errors
    def run(self):
        """
        运行师门任务

        1. 检查任务条件。
        2. 如果条件满足，则执行任务动作。
        """
        super().run()
