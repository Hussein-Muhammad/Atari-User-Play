import asyncio
from concurrent.futures import ProcessPoolExecutor
import gym
from tkinter import *
from tkinter import messagebox
import time
import threading

print('running async test')

action = 0
total_score = 0

# env = gym.make("CartPole-v0")
env = gym.make("MountainCar-v0")

env.mode = 'normal'

env.reset()




def Game_loop():
    while True:
        env.render()
        # time.sleep(0.05)
        observation, reward, done, info = env.step(action)
        global total_score
        total_score += reward
        # main.update()
        if done:
            # print("***** ***** ***** GAME OVER ***** ***** *****")
            break




def leftKey(event):
    global action
    action = 0
    # print ("Left key pressed" , action)
    L_left.config(bg="red", fg="white")
    L_right.config(bg="white", fg="black")
    # time.sleep(.2)        #configure slow motion
    


def rightKey(event):
    global action
    action = 1
    # print ("Right key pressed" , action)
    L_right.config(bg="red", fg="white")
    L_left.config(bg="white", fg="black")
    # time.sleep(.2)
        

def upKey(event):
    global action
    action = 2
    # print ("Right key pressed" , action)
    L_right.config(bg="white", fg="black")
    L_left.config(bg="white", fg="black")
    # time.sleep(.2)
        

def Space_pressed(event):
    messagebox.showinfo("Game Over", ("Your score "+str(total_score)))
    global total_score
    total_score = 0
    env.reset()
    




class App(threading.Thread):

    def __init__(self, tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            Game_loop()
            


main = Tk()
APP = App(main)

L_left = Label(text="Left" ,font=("Courier", 44),bg="white", fg="black")
L_right = Label(text="Right" ,font=("Courier", 44),bg="white", fg="black")

L_left.pack(side = LEFT, padx=20)
L_right.pack(side = RIGHT, padx=20)
frame = Frame(main, width=100, height=100)
frame.bind('<Left>', leftKey)
frame.bind('<Right>', rightKey)
frame.bind('<Up>', upKey)                           #comment here in case of less controls needed
frame.bind('<space>', Space_pressed)
frame.focus_set()
frame.pack()

main.mainloop()
