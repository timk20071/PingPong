#import max7219_simpletest.py
import digitalio
import board
import busio
import time
from adafruit_max7219 import matrices
import sys

# hardware variables
    # reset initialisation
reset = digitalio.DigitalInOut(board.GP3)
reset.direction = digitalio.Direction.INPUT

    # matrix initialisation
spi = busio.SPI(clock=board.GP10, MOSI=board.GP11, MISO=board.GP12)
cs = digitalio.DigitalInOut(board.GP9)
matrix = matrices.Matrix8x8(spi, cs)

    # button initialisation
leftup = digitalio.DigitalInOut(board.GP18)
leftup.direction = digitalio.Direction.INPUT
leftdown = digitalio.DigitalInOut(board.GP19)
leftdown.direction = digitalio.Direction.INPUT
rightup = digitalio.DigitalInOut(board.GP20)
rightup.direction = digitalio.Direction.INPUT
rightdown = digitalio.DigitalInOut(board.GP21)
rightdown.direction = digitalio.Direction.INPUT

# logic variables
data = [[0 for w in range(8)]for h in range(8)]

leftbar_index_top = 2
rightbar_index_top = 2

class Ball:
    def __init__(self,xpos,ypos,moveright,upordown):
        self.xpos = xpos
        self.ypos = ypos
        self.moveright = moveright
        self.upordown = upordown # 0: ball going in a straight line, 1: ball going up, -1 ball going down

ball = Ball(xpos=1,ypos=1,moveright=True,upordown=1)

def r():
    if reset.value:
        exit(1)

def initdata():
    data[0][2] = 1
    data[0][3] = 1
    data[0][4] = 1
    data[7][2] = 1
    data[7][3] = 1
    data[7][4] = 1

def updatematrix():
    matrix.fill(False)
    for x in range(8):
        for y in range(8):
            matrix.pixel(x,y,int(data[x][y])) # 1: Light on, 0: light off

def moveball():
    if ball.upordown == 1:
        ball.ypos -= 1
    elif ball.upordown == -1:
        ball.ypos += 1

    if ball.moveright:
        ball.xpos += 1
    else:
        ball.xpos -= 1
    matrix.pixel(ball.xpos,ball.ypos,1)
    matrix.show()

def checkballstate():
    if (ball.ypos == 0 and ball.upordown == 1) or (ball.ypos == 7 and ball.upordown == -1): # Falls Ball oben oder unten am Rand ankommt, wird die Richtung gedreht
        ball.upordown *= -1
    haswon = False
    if((ball.xpos == 1 and ball.moveright == False) or (ball.xpos == 6 and ball.moveright == True)):
        haswon = checkcollision()
    if haswon:
        if ball.xpos == 1:
            matrix.fill(True)
            matrix.text("2",1,1,0)
            matrix.show()
            exit(2)
        elif ball.xpos == 6:
            matrix.fill(True)
            matrix.text("1",1,1,0)
            matrix.show()
            exit(1)

def checkcollision():
    if(ball.moveright):
        xposmodifier = 1
        bar_index_top = rightbar_index_top
    else:
        xposmodifier = -1
        bar_index_top = leftbar_index_top
    if(data[ball.xpos+xposmodifier][ball.ypos+(ball.upordown*-1)] == 1):
        if bar_index_top-(ball.ypos+(ball.upordown*-1)) == 0 : 
             ball.upordown = 1
        elif bar_index_top-(ball.ypos+(ball.upordown*-1)) == -1:        # filter out which direction the ball should go after touching bar
                ball.upordown = 0
        elif bar_index_top-(ball.ypos+(ball.upordown*-1)) == -2 : 
                ball.upordown = -1
        ball.moveright = not ball.moveright
        return False
    return True

def movebar():
    global leftbar_index_top, rightbar_index_top

    if leftup.value and leftbar_index_top != 0:
        leftbar_index_top -= 1
        data[0][leftbar_index_top+3] = 0
        data[0][leftbar_index_top] = 1
    elif leftdown.value and leftbar_index_top != 5:
        data[0][leftbar_index_top+3] = 1
        leftbar_index_top += 1
        data[0][leftbar_index_top-1] = 0

    if rightup.value and rightbar_index_top != 0:
        rightbar_index_top -= 1
        data[7][rightbar_index_top+3] = 0
        data[7][rightbar_index_top] = 1
    elif rightdown.value and rightbar_index_top != 5:
        data[7][rightbar_index_top+3] = 1
        rightbar_index_top += 1
        data[7][rightbar_index_top-1] = 0

matrix.fill(False)
matrix.text("3",1,1,1)
matrix.show()
time.sleep(1)
matrix.fill(False)
matrix.text("2",1,1,1)
matrix.show()
time.sleep(1)
matrix.fill(False)
matrix.text("1",1,1,1)
matrix.show()
time.sleep(1)


initdata()
updatematrix()
matrix.pixel(ball.xpos,ball.ypos,1)
matrix.show()
time.sleep(1)
while True:
    updatematrix()
    checkballstate()
    moveball()
    movebar()

    time.sleep(1)
    r()



"""
pixel(xpos: int, ypos: int, bit_value: int = None)→ None[source]¶
Set one buffer bit

Parameters
:
xpos (int) – x position to set bit

ypos (int) – y position to set bit

bit_value (int) – value > 0 sets the buffer bit, else clears the buffer bit
"""