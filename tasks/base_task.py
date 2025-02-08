# -*- coding: utf-8 -*-

from utils.logger import logger

class BaseTask:
    def __init__(self, task_name):
        """
        初始化基础任务

        :param task_name: 任务名称
        """
        self.task_name = task_name

    def check_condition(self):
        """
        检查任务条件（需子类实现）
        """
        raise NotImplementedError("子类必须实现 check_condition 方法")

    def execute_action(self):
        """
        执行任务动作（需子类实现）
        """
        raise NotImplementedError("子类必须实现 execute_action 方法")

    def run(self):
        """
        运行任务
        """
        logger.info(f"开始任务: {self.task_name}")
        if self.check_condition():
            self.execute_action()
        logger.info(f"任务完成: {self.task_name}")
