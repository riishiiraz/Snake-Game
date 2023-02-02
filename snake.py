# Code By : Rishitosh [riishiiraz]
# Time Created : Saturday 31 July 2021 10∶21∶52 AM

from tkinter import *
import random

root = Tk()

ScreenX = 500
ScreenY = 500

#root.minsize(ScreenX , ScreenY)
root["bg"] = "#3a3950"
root.title("Snake Game By RISHITOSH")


#ScreenX = 1366
#ScreenY = 710

"""

ScoreFrame = LabelFrame(root , bg = root["bg"])
ScoreFrame.pack(side = "left" , expand=1 , fill = "both")

Button(ScoreFrame , text=134 , bd = 1).pack()
"""

GameFrame = Frame(root)
GameFrame.pack()

RefreshDuration = 75

GameBg = "#313950"
GameFrame["bg"] = GameBg

SizeOfSnakeBlock = 25
BgOfSnakeBlock = "#309397" #014c78

SizeOfSnakeFoodBlock = SizeOfSnakeBlock
BgOfSnakeFoodBlock = "#ff8d01"

BgOfSnakeHeadBlock = "#014c78"

argsForSnakeBlock = {"bd":0 , "height":SizeOfSnakeBlock , "width" : SizeOfSnakeBlock , "bg": BgOfSnakeBlock}
argsForSnakeFoodBlock = {"bd":0 , "height":SizeOfSnakeFoodBlock , "width" : SizeOfSnakeFoodBlock , "bg": BgOfSnakeFoodBlock}

GapBetweenBlocks = 5
step = SizeOfSnakeBlock + GapBetweenBlocks


GameScreenX = (ScreenX//(SizeOfSnakeBlock+GapBetweenBlocks))*(SizeOfSnakeBlock+GapBetweenBlocks)
GameScreenY = (ScreenY//(SizeOfSnakeBlock+GapBetweenBlocks))*(SizeOfSnakeBlock+GapBetweenBlocks)

print(GameScreenX , GameScreenY)

GameFrame["width"] ,GameFrame["height"] = (GameScreenX, GameScreenY)
root.minsize(GameScreenX, GameScreenY)

b1 = Canvas(GameFrame, **argsForSnakeBlock)
b2 = Canvas(GameFrame, **argsForSnakeBlock)
b3 = Canvas(GameFrame, **argsForSnakeBlock)
b4 = Canvas(GameFrame, **argsForSnakeBlock)
b5 = Canvas(GameFrame, **argsForSnakeBlock)
b5["bg"] = BgOfSnakeHeadBlock

b1.place(x=0, y=0)
b2.place(x=step, y=0)
b3.place(x=step * 2, y=0)
b4.place(x=step * 3, y=0)
b5.place(x=step * 3, y=step)

ScoreLabel = Label(GameFrame , text="00" , font = ("Consolas 15"), bg = GameBg  , fg = "#aeaeae")
ScoreLabel.place(x=GameScreenX - ScoreLabel.winfo_reqwidth() , y=0)


Score = 0


rangeX = range(0, GameScreenX, step)
rangeY = range(0, GameScreenY, step)
ranX = random.choice(rangeX)
ranY = random.choice(rangeY)




bF = Canvas(GameFrame ,**argsForSnakeFoodBlock)       #Food Block
bF.place(x=ranX, y=ranY)

bs = [b1, b2, b3, b4, b5]

dX = IntVar();
dX.set(step)
dY = IntVar()

def lt():
    dY.set(0)
    dX.set(-step)


def rt():
    dY.set(0)
    dX.set(step)


def up():
    dY.set(-step)
    dX.set(0)


def dw():
    dY.set(step)
    dX.set(0)


def setFoodToNewPos():
    global ranX, ranY
    ranX = random.choice(rangeX)
    ranY = random.choice(rangeY)

    for b in bs:
        xx, yy = int(b.place_info()["x"]), int(b.place_info()["y"])
        if (ranX == xx and ranY == yy):
            print("Old Posss Found !")
            setFoodToNewPos()
    bF.place(x=ranX, y=ranY)

RunningId = None
IsRunning = False





def move():
    global bs, ranX, ranY , Score
    global RunningId , IsRunning

    IsRunning = True

    LB = bs[-1]  # Last Button [Head Button]
    PI = LB.place_info()  # Place Info For Last Button
    X = int(PI["x"]) + dX.get()  # X Pos Of Head Button ( With Increment Of Change In Position )
    Y = int(PI["y"]) + dY.get()  # Y Pos Of Head Button ( With Increment Of Change In Position )

    if (X > (GameScreenX - step)):  # Cheking That The Head Gone Out Of The GameScreen
        X = 0
    elif (X < 0):
        X = GameScreenX - step
    if (Y > (GameScreenY - step)):
        Y = 0
    elif (Y < 0):
        Y = GameScreenY - step

    bs[0].place(x=X, y=Y)  # Changing The Starting Button To Ending Position [ Works as Head of The Snake ]
    bs[0]["bg"] = BgOfSnakeHeadBlock  # Changing The Color For Head Of The Snake

    bs.append(bs[0])  # Adding The Head to The Last Of The List of Button
    bs.pop(0)  # Removing The Starting Button
    bs[-2]["bg"] = BgOfSnakeBlock  # Changing The Text For Normal Body ( Excluding Head )

    if (X == ranX and Y == ranY):  # Cheking That The Snake Get The Food ?

        print("Got It !")
        Score += 1
        ScoreLabel["text"] = "%02d"%(Score)

        food = Canvas(GameFrame , **argsForSnakeFoodBlock)  # New Food Button
        StartingBtn = bs[0]
        food["bg"] = BgOfSnakeBlock
        food.place(x=int(StartingBtn.place_info()["x"]) + step,
                   y=int(StartingBtn.place_info()["y"]))  # Placing The Food To The Startig of The Snake's Body
        bs.insert(0, food)
        setFoodToNewPos()  # Changing The Food Position

    RunningId = root.after(RefreshDuration, move)  # Repeating The Process


def PlayPause():
    global IsRunning , RunningId

    if(IsRunning): # Pause
        root.after_cancel(RunningId)
        IsRunning = False
        print("Paused")
    elif(not IsRunning): # Play
        print("Played")
        move()



root.bind( "<space>", lambda e: PlayPause())  # Press "s" To Start The Game

root.bind("<Right>", lambda e: rt())
root.bind("<Left>", lambda e: lt())
root.bind("<Up>", lambda e: up())
root.bind("<Down>", lambda e: dw())

def showTip(tip = "Press Space To Play/Pause !"):
    temp = root.title()
    print(temp)
    root.title(tip)
    root.after(2000 , lambda : root.title(temp))

showTip()





root.mainloop()

"""
if (X > (ScreenX - step)):  # Cheking That The Head Gone Out Of The Screen
        X = 0
    elif (X < 0):
        X = ScreenX - step
    if (Y > (ScreenY - step)):
        Y = 0
    elif (Y < 0):
        Y = ScreenY - step
"""
