# import socket to create web server
try:
  import usocket as socket
except:
  import socket

import time

# import esp library -> Pin method
from machine import Pin
import machine

# import network for wifi connection
import network

# The following lines turn off vendor OS debugging messages:
import esp
esp.osdebug(None)

# garbage collector
# This is a way to reclaim memory occupied by objects that are no longer in used by the program.
import gc
gc.collect()

# wifi id
ssid = 'Galaxy A50C77B'
# wifi pw
password = '123654ab'

# initialize wifi station
station = network.WLAN(network.STA_IF)
# activate wifi station
station.active(True)
# connect to wifi using id and pw
station.connect(ssid, password)

# while loop breaks when connected
while station.isconnected() == False:
  pass
print('Connection successful')
# prints ip config
print(station.ifconfig())

# pin2 output (Used to switch built in led on and off)
led = Pin(2, Pin.OUT)

# fn returns HTML text to build the web page.
def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html>
    <head>
        <title>ESP Web Server</title> 
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel=" " href="data:,"> 

        <style>

        html{font-family: Helvetica; 
             display:inline-block; 
             margin: 0px auto; 
             text-align: center;}

        h1{color: #0F3376; 
           padding: 2vh;}

        p{font-size: 1.5rem;}

        .button{display: inline-block; 
                background-color: #e7bd3b; 
                border: none; 
                border-radius: 4px; 
                color: white; 
                padding: 16px 40px; 
                text-decoration: none; 
                font-size: 30px; 
                margin: 2px; 
                cursor: pointer;}

        .button2{background-color: #4286f4;}

        .button3{background-color: #41b99b;}
        </style>
        </head>
        
        <body> 
            <h1>ESP Web Server</h1> 
            <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
            <p><a href="/?led=inc"><button class="button">Increment</button></a></p>
            <p><a href="/?led=dec"><button class="button button2">Decrement</button></a></p>
            <p><a href="/?led=reset"><button class="button button3">Reset</button></a></p>
        </body>

</html>"""
  return html

# create a socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binds ip address to socket server
s.bind(('', 80))
# max numbers of connections
s.listen(5)



#############################################################################




seg_pins = [0, 2, 4, 5, 12, 13, 14]
seg_name = []


def initialize():
    # set pins to be output pins 
    for i in range(len(seg_pins)):
        seg_name.append(machine.Pin(seg_pins[i], machine.Pin.OUT))

    for i in range(len(seg_pins)):
        seg_name[i].value(0)
        
def display(num):
    for i in range(len(seg_name)):
        values = seg_values[num]
        seg_name[i].value(not values[i])

# input flags from mobile app or web app 
increment = False
decrement = False 
reset = True
counter = 0

# seg_name values 
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
display(0)


####################################################################





while True:
  conn, addr = s.accept()
  #print('Got a connection from %s' % str(addr))
  
  # the maximum data that can be received at once.
  request = conn.recv(1024)
  request = str(request)
  print("Request {}".format(str(request)))
  #print('Content = %s' % request)
  led_inc = request.find('/?led=inc')
  led_dec = request.find('/?led=dec')
  print("oN: {}        off:{} ".format(led_inc, led_dec))
  if led_inc == 6:
    print('LED ON')
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
  if led_dec == 6:
    print('LED OFF')
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
        
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()