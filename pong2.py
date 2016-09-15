from tkinter import *
import random
import time

counter = 0
counter1 = 0

playagain = 'N'

tk = Tk()
tk.title('Pong')
tk.resizable(0,0)#cant resize window
tk.wm_attributes("-topmost",1)#topmost means it should be in front of all apps
canvas = Canvas(tk,width = 500,height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg="black")
canvas.pack()
tk.update()

canvas.create_line(250,0,250,400,fill='white')

class Ball:
    def __init__(self,canvas,paddle,paddle1,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,232,195)
        starts = [-3,3]
        random.shuffle(starts)
        self.counters = 0
        self.x = starts[0]
        self.y = -3
        self.speed1 = 3
        self.speed2 = -3
        self.paddle = paddle
        self.paddle1 = paddle1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if self.counters == 10:
            self.speed1 = 5
            self.speed2 = -5
        if self.counters == 20:
            self.speed1 = 7
            self.speed2 = -7
        if pos[1] <= 0:
            self.y = self.speed1
        if pos[3] >= self.canvas_height:
            self.y = self.speed2
        if pos[0] <= 0:
            self.x = self.speed1
            #self.counter += 1
            #print(self.counter)
            self.score(False)
        if pos[2] >= self.canvas_width:#if greater than 500
            self.x = self.speed2
            #self.counter1 += 1
            #print(self.counter)
            self.score(True)
            
        if self.hit_paddle(pos) == True:#pos is the coord of the ball
            self.x = self.speed1
            self.counters += 1
        if self.hit_paddle1(pos) == True:
            self.x = self.speed2
            self.counters += 1

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                #self.score = self.score + 1
                #score.set(self.score)
                return True
            return False

        
    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                #self.score = self.score + 1
                #score.set(self.score)
                return True
            return False
    def score(self,val):
        global counter
        global counter1

        if val == True:
            a = self.canvas.create_text(125,40,text=counter,font=("Arial",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter +=1
            a = self.canvas.create_text(125,40,text=counter,font=("Arial",60),fill="white")

        if val == False:
            a = self.canvas.create_text(375,40,text=counter1,font=("Arial",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter1 +=1
            a = self.canvas.create_text(375,40,text=counter1,font=("Arial",60),fill="white")

class Paddle:
    def __init__(self,canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,2,30,90,fill='white')
        #self.canvas.move(self.id,10,200)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('d',self.turn_up)
        self.canvas.bind_all('c',self.turn_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)#self.id,x position, y position
        pos = self.canvas.coords(self.id)
        self.y = 0#I added this so it doesn't move without user input
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
            
    def turn_up(self,event):#event tells the function a physical thing will happen
        self.y = -34
        pos = self.canvas.coords(self.id)#after -30 it updates the self.canvas_height
            
        if pos[1] <= 15: 
            self.y = 0
 
    def turn_down(self,event):
        self.y = 34
        pos = self.canvas.coords(self.id)#all this is doing is getting the
        #coordinates of self. from there, pos[2] is checking x2 to see
        #if its greater than the width of the self.canvas. 
        if pos[3] >= self.canvas_height -15:
            self.y = 0
            
class Paddle1:
    def __init__(self,canvas):
        self.canvas = canvas
        self.id = canvas.create_rectangle(490,398,470,310,fill='white')
        #self.canvas.move(self.id,10,300)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)#self.id,x position, y position
        pos = self.canvas.coords(self.id)
        self.y = 0#I added this so it doesn't move without user input
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
            
    def turn_up(self,event):#event tells the function a physical thing will happen
        self.y = -34
        pos = self.canvas.coords(self.id)#after -30 it updates the self.canvas_height
        if pos[1] <= 15: 
            self.y = 0
 
    def turn_down(self,event):
        self.y = 34
        pos = self.canvas.coords(self.id)#all this is doing is getting the
        #coordinates of self. from there, pos[2] is checking x2 to see
        #if its greater than the width of the self.canvas. 
        if pos[3] >= self.canvas_height - 15:
            self.y = 0

def start():
    global counter
    global playagain
    while 1:
        if counter == 3:
            canvas.create_text(250,200,text="You win P1",font=32,fill="red")
            break
        if counter1 == 3:
            canvas.create_text(250,200,text="You win P2",font=32,fill="red")
            break
        ball.draw()
        paddle.draw()
        paddle1.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    print('play again? Y/N')
    playagain = input()
"""
    if playagain == 'Y' or playagain == 'y':
        counter = 0
        counter1 = 0
        start()
"""            
    
paddle = Paddle(canvas)
paddle1 = Paddle1(canvas)                
ball = Ball(canvas,paddle,paddle1,'white')


button = Button(tk,text="Start",command=lambda:start()).pack()
#button.pack()


