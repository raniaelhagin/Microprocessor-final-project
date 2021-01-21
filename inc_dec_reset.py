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
        segment.append(machine.Pin(seg[i], machine.Pin.OUT))

    for i in range(len(seg)):
        segment[i].value(0)
        
def display(num):
    for i in range(len(segment)):
        values = seg_values[num]
        segment[i].value(not values[i])

# input flags from mobile app or web app 
increment = False
decrement = False 
reset = True
counter = 0

# segment values 
seg_values = {  0: [1, 1, 1, 1, 1, 1, 0],
                1: [0, 1, 1, 0, 0, 0, 0],
                2: [1, 1, 0, 1, 1, 0, 1],
                3: [1, 1, 1, 1, 0, 0, 1],
                4: [0, 1, 1, 0, 0, 1, 1], 
                5: [1, 0, 1, 1, 0, 1, 1],
                6: [1, 0, 1, 1, 1, 1, 1], 
                7: [1, 1, 1, 0, 0, 0, 0],
                8: [1, 1, 1, 1, 1, 1, 1],
                9: [1, 1, 1, 1, 0, 1, 1]
            }

initialize()
# default (display 0) 
display(5)

time.sleep(1)
    
while True:

    if increment:

        if ((not(decrement)) and (not(reset))): 

            if counter == 9:
                # reset counter 
                counter = 0

                # display zero 
                display(counter)
            
            elif 0 <= counter < 9:
                # increment counter
                counter += 1

                # display counter 
                display(counter)
        
    if decrement:

        if ((not(increment)) and (not(reset))): 

            if counter == 0:
                # reset counter 
                counter = 9

                # display zero 
                display(counter)
            
            elif 0 < counter <= 9:
                # deecrement counter
                counter -= 1

                # display counter 
                display(counter)
            
    if reset:

        if ((not(decrement)) and (not(increment))): 
                counter = 0
                # display zero 
                display(counter)
                
    time.sleep(1)
        
    

    
