#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: CapsuleEnv.py
@time: 2019/4/16 16:44
"""
from tkinter import *
import time
import sys
import random


class CapsuleEnv(Tk, object):
    def __init__(self):
        super(CapsuleEnv, self).__init__()
        self.width = 23
        self.title('maze')
        self.geometry('600x600')
        self.action_space = ['u', 'd', 'l', 'r']
        #  创建一个Canvas，设置其背景色为白色

        self.cvinit = Canvas(self, bg='white', height=600, width=600)

        self.build_env()

    def changesize(self):
        height = random.randint(1, 100)
        width = random.randint(400, 600)
        self.cvinit.coords(self.rtinit, (height, width, height + 40, width + 40))

    def build_env(self):
        rtinit = self.cvinit.create_rectangle(120, 120, 160, 160)
        rtfinal = self.cvinit.create_rectangle(400, 10, 440, 50)
        self.cvinit.pack()
        rtfinal.pack()
        rtinit.pack()
        b = Button(self, text='改变大小', command=self.changesize)
        b.pack()


if __name__ == '__main__':
    env = CapsuleEnv()
    env.mainloop()
