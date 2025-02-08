# -*- coding: utf-8 -*-

import os
import yaml
from utils.logger import logger

def generate_task_code(task_config):
    """
    根据任务配置生成任务代码

    :param task_config: 任务配置字典
    :return: 生成的任务代码
    """
    task_name = task_config["任务名称"]
    task_name_en = task_name.replace("任务", "")  # 去掉“任务”后缀
    task_name_en = task_name_en.lower()  # 转换为小写
    code = f"""# -*- coding: utf-8 -*-

from tasks.base_task import BaseTask
from utils.condition_checker import ConditionChecker
from utils.action_executor import ActionExecutor
from utils.logger import logger

class {task_name_en.capitalize()}Task(BaseTask):
    def __init__(self):
        super().__init__("{task_name}")
        self.condition_checker = ConditionChecker()
        self.action_executor = ActionExecutor()

    def check_condition(self):
        # 判断逻辑
"""

    for condition in task_config["判断逻辑"]:
        code += f"""
        # {condition['条件']}
        if not self.condition_checker.{condition['操作']}:
            logger.warning("{condition['条件']} 不满足")
            return False
"""

    code += """
        logger.info("所有条件满足")
        return True

    def execute_action(self):
        # 动作逻辑
"""

    for action in task_config["动作逻辑"]:
        code += f"""
        try:
            # {action['操作']}
            self.action_executor.{action['操作']}
            logger.info("{action['操作']} 成功")
        except Exception as e:
            logger.error(f"操作失败: {{e}}")
"""

    code += """
    def run(self):
        super().run()
"""
    return code

def save_task_code(task_code, task_name):
    """
    保存生成的任务代码到文件

    :param task_code: 生成的任务代码
    :param task_name: 任务名称
    """
    task_name_en = task_name.replace("任务", "")  # 去掉“任务”后缀
    task_name_en = task_name_en.lower()  # 转换为小写
    task_file_path = os.path.join("tasks", f"{task_name_en}_task.py")
    with open(task_file_path, "w", encoding="utf-8") as f:
        f.write(task_code)
    logger.info(f"任务代码已保存: {task_file_path}")

def main():
    """
    主函数：读取任务配置文件并生成任务代码
    """
    # 读取任务配置文件
    task_config_path = os.path.join("tasks", "generate", "task_workflow.yaml")
    try:
        with open(task_config_path, "r", encoding="utf-8") as f:
            task_config = yaml.safe_load(f)
        logger.info(f"任务配置文件加载成功: {task_config_path}")
    except Exception as e:
        logger.error(f"任务配置文件加载失败: {e}")
        return

    # 生成任务代码
    task_code = generate_task_code(task_config)
    print(task_code)  # 打印生成的代码

    # 保存任务代码
    save_task_code(task_code, task_config["任务名称"])

if __name__ == "__main__":
    main()
