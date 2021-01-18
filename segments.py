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

#           a, b, c, d,  e,  f,  g
seg = [0, 2, 4, 5, 12, 13, 14]
segment = []

# set pins to be output pins 
for i in range(len(seg)):
    segment[i] = machine.Pin(seg[i], machine.Pin.out)

# segment values 
zero  = [1, 1, 1, 1, 1, 1, 0]
one   = [0, 1, 1, 0, 0, 0, 0]
two   = [1, 1, 0, 1, 1, 0, 1]
three = [1, 1, 1, 1, 0, 0, 1]
four  = [0, 1, 1, 0, 0, 1, 1]
five  = [1, 0, 1, 1, 0, 1, 1]
six   = [1, 0, 1, 1, 1, 1, 1]
seven = [1, 1, 1, 0, 0, 0, 0]
eight = [1, 1, 1, 1, 1, 1, 1]
nine  = [1, 1, 1, 1, 0, 1, 1]


# input flags from mobile app or web app 
count_up = False
count_down = False 
reset = False


# if Count up 
if count_up:

    while ((not(count_down)) and (not(reset))):

        # display 1 
        for i in range(len(segment)):
            segment[i].value(one[i])
        time.sleep(0.3)

        # display 2 
        for i in range(len(segment)):
            segment[i].value(two[i])
        time.sleep(0.3)

        # display 3 
        for i in range(len(segment)):
            segment[i].value(three[i])
        time.sleep(0.3)

        # display 4 
        for i in range(len(segment)):
            segment[i].value(four[i])
        time.sleep(0.3)

        # display 5 
        for i in range(len(segment)):
            segment[i].value(five[i])
        time.sleep(0.3)

        # display 6 
        for i in range(len(segment)):
            segment[i].value(six[i])
        time.sleep(0.3)

        # display 7
        for i in range(len(segment)):
            segment[i].value(seven[i])
        time.sleep(0.3)

        # display 8 
        for i in range(len(segment)):
            segment[i].value(eight[i])
        time.sleep(0.3)

        # display 9 
        for i in range(len(segment)):
            segment[i].value(nine[i])
        time.sleep(0.3)

        # display 0 
        for i in range(len(segment)):
            segment[i].value(zero[i])
        time.sleep(0.3)


# if Count down 
if count_down:

    while ((not(count_up)) and not(reset)):
    
        # display 9 
        for i in range(len(segment)):
            segment[i].value(nine[i])
        time.sleep(0.3)

        # display 8 
        for i in range(len(segment)):
            segment[i].value(eight[i])
        time.sleep(0.3)

        # display 7
        for i in range(len(segment)):
            segment[i].value(seven[i])
        time.sleep(0.3)

        # display 6
        for i in range(len(segment)):
            segment[i].value(six[i])
        time.sleep(0.3)

        # display 5 
        for i in range(len(segment)):
            segment[i].value(five[i])
        time.sleep(0.3)

        # display 4 
        for i in range(len(segment)):
            segment[i].value(four[i])
        time.sleep(0.3)

        # display 3
        for i in range(len(segment)):
            segment[i].value(three[i])
        time.sleep(0.3)

        # display 2 
        for i in range(len(segment)):
            segment[i].value(two[i])
        time.sleep(0.3)

        # display 1 
        for i in range(len(segment)):
            segment[i].value(one[i])
        time.sleep(0.3)

        # display 0 
        for i in range(len(segment)):
            segment[i].value(zero[i])
        time.sleep(0.3)
        
if reset:
    while (not(count_up) and not(count_down)):
        for i in range(len(segment)):
            segment[i].value(zero[i])
            
    