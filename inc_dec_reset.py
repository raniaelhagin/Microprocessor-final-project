import machine 
import time 

"""
            7 segment display 
            ------- a ------    0 
            -              -
        13  f              b    2
            -              -
            ------- g ------    14
            -              -
        12  e              c    4
            -              -
            ------- d ------    5 
"""

#      a, b, c, d,  e,  f,  g
seg = [0, 2, 4, 5, 12, 13, 14]
segment = []


def initialize():
    # set pins to be output pins 
    for i in range(len(seg)):
        segment[i] = machine.Pin(seg[i], machine.Pin.out)

    for i in range(len(seg)):
        segment[i].value(0)

# input flags from mobile app or web app 
increment = False
decrement = False 
reset = False
counter = 0

# segment values 
values = { 0: [1, 1, 1, 1, 1, 1, 0],
           1: [0, 1, 1, 0, 0, 0, 0],
           2: [1, 1, 0, 1, 1, 0, 1],
           3: [1, 1, 1, 1, 0, 0, 1],
           4: [0, 1, 1, 0, 0, 1, 1], 
           5: [1, 0, 1, 1, 0, 1, 1],
           6: [1, 0, 1, 1, 1, 1, 1], 
           7: [1, 1, 1, 0, 0, 0, 0],
           8: [1, 1, 1, 1, 1, 1, 1],
           9: [1, 1, 1, 1, 0, 1, 1]}

initialize()
while True:

    # default (display 0) 
    for i in range(len(segment)):
        segment[i].value(values[0])
    
    if increment:
        counter += 1

        # display counter 





