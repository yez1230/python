# -*- coding: utf-8 -*-

import Tkinter
import random
import time

tk = Tkinter.Tk()
tk.title("弹弹球")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Tkinter.Canvas(tk, width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

class Ball():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,30,30,fill=color)
        self.canvas.move(self.id,120,100)
        x = random.randint(-3, 3)
        y = random.randint(-3, 3)
        if !x:
            x = 1
        if !y:
            y = 1
        self.x = x # 正负代表方向（左右），数字代表速度，数字越大速度越快
        self.y = y # 正负代表方向（上下），数字代表速度，数字越大速度越快
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

# 判断是否碰到了小木板
    def hit_paddle(self,paddle_pos):
        pos = self.canvas.coords(self.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


    def draw(self,paddle_pos):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)

        if self.hit_paddle(paddle_pos) == True:
            self.y = -3 # 为负数是往上弹，负得越大弹得速度越快 下面的x，y是同样的道理

        if pos[1] <= 0:
            self.y = 3

        if pos[0] <= 0:
            self.x = 3

        if pos[2] >= self.canvas_width:
            self.x = -3

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True



class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,390)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-a>', self.turn_left)
        self.canvas.bind_all('<KeyPress-d>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

        return pos

    def turn_left(self, evt):
        if self.x == -2:
            self.x = -4
        else:
            self.x = -2

    def turn_right(self, evt):
        if self.x == 2:
            self.x = 4
        else:
            self.x = 2

    def qqq(self, evt):
        print "q"

paddle = Paddle(canvas,"blue")
ball = Ball(canvas,"red")
i = 1
while i:
    if ball.hit_bottom == False:
        pos = paddle.draw()
        ball.draw(pos)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        i = 0
