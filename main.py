# -*- coding: utf-8 -*-

from gui.gui_panel import GUIPanel
from task_manager import TaskManager

def main():
    """
    主函数：启动 GUI 面板
    """
    task_manager = TaskManager()
    gui = GUIPanel(task_manager)
    gui.run()

if __name__ == "__main__":
    main()
