import digitalio
import board
import busio

reset = digitalio.DigitalInOut(board.GP3)
reset.direction = digitalio.Direction.INPUT
rst = digitalio.DigitalInOut(board.GP2)
rst.direction = digitalio.Direction.OUTPUT
rst.value = True
def r():
    if not reset.value:
        exit(1)