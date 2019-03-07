#coding=utf-8
import pymouse, pykeyboard, os, sys
from pymouse import *
from pykeyboard import PyKeyboard
import configparser

config = configparser.ConfigParser()
config.read("config.ini", encoding='utf-8')

startFight = [int(config['开始战斗']['x']), int(config['开始战斗']['y'])]

m = PyMouse()
k = PyKeyboard()

# 鼠标事件监听，需要继承PyMouseEvent，重载其中的函数
class MouseEventListen(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        if button == 1:
            if press == 1:
                print('click in (%d, %d)'%(x,y))
        else:
            self.stop()

# C = MouseEventListen()
# C.run()


m.click(startFight[0], startFight[1], 1, 1)
