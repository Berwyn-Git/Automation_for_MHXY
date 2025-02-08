# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, scrolledtext
from utils.logger import logger

class GUIPanel:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.root = tk.Tk()
        self.root.title("自动化任务管理面板")
        self.root.geometry("400x300")

        # 任务选择下拉菜单
        self.task_label = tk.Label(self.root, text="选择任务:", font=("Arial", 12))
        self.task_label.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_combobox = ttk.Combobox(self.root, textvariable=self.task_var, state="readonly")
        self.task_combobox['values'] = ["师门任务", "抓鬼任务", "押镖任务", "打图任务", "挖图任务"]
        self.task_combobox.pack(pady=5)

        # 执行状态标签
        self.status_label = tk.Label(self.root, text="状态: 未运行", font=("Arial", 12))
        self.status_label.pack(pady=5)

        # 日志输出区域
        self.log_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=100, height=30)
        self.log_area.pack(pady=10)

        # 控制按钮
        self.start_button = tk.Button(self.root, text="开始", command=self.start_task, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.root, text="暂停", command=self.pause_task, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.root, text="停止", command=self.stop_task, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # 绑定任务选择事件
        self.task_combobox.bind("<<ComboboxSelected>>", self.on_task_select)

        # 日志重定向
        self.redirect_logs()

    def redirect_logs(self):
        """
        将日志输出重定向到 GUI 的日志区域
        """
        class LogRedirector:
            def __init__(self, log_area):
                self.log_area = log_area

            def write(self, message):
                self.log_area.insert(tk.END, message)
                self.log_area.see(tk.END)

        import sys
        sys.stdout = LogRedirector(self.log_area)
        sys.stderr = LogRedirector(self.log_area)

    def on_task_select(self, event):
        """
        任务选择事件处理
        """
        selected_task = self.task_var.get()
        logger.info(f"已选择任务: {selected_task}")
        self.start_button.config(state=tk.NORMAL)  # 启用“开始”按钮

    def start_task(self):
        """
        启动任务
        """
        selected_task = self.task_var.get()
        if not selected_task:
            logger.warning("请先选择一个任务")
            return

        self.task_manager.start_task(selected_task)
        self.status_label.config(text="状态: 运行中")
        self.start_button.config(state=tk.DISABLED)  # 禁用“开始”按钮
        self.pause_button.config(state=tk.NORMAL)    # 启用“暂停”按钮
        self.stop_button.config(state=tk.NORMAL)     # 启用“停止”按钮
        logger.info(f"任务已启动: {selected_task}")

    def pause_task(self):
        """
        暂停任务
        """
        self.task_manager.pause_task()
        self.status_label.config(text="状态: 已暂停")
        self.pause_button.config(state=tk.DISABLED)  # 禁用“暂停”按钮
        self.start_button.config(state=tk.NORMAL)    # 启用“开始”按钮
        logger.info("任务已暂停")

    def stop_task(self):
        """
        停止任务
        """
        self.task_manager.stop_task()
        self.status_label.config(text="状态: 已停止")
        self.start_button.config(state=tk.NORMAL)    # 启用“开始”按钮
        self.pause_button.config(state=tk.DISABLED)  # 禁用“暂停”按钮
        self.stop_button.config(state=tk.DISABLED)   # 禁用“停止”按钮
        logger.info("任务已停止")

    def run(self):
        """
        运行 GUI
        """
        self.root.mainloop()
