# import socket and python socket API to create web server
try:
  import usocket as socket
except:
  import socket

import time
import machine 
import network 

########################### Sevent segment initialization ####################
seg_pins = [0, 2, 4, 5, 12, 13, 14]
seg_name = []
counter = 0

#            counter:  seg values 
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

def initialize():
    """ Initialize seven segment display: set used pins to output 
                                          and initalize them to high """
    # set pins to be output pins 
    for i in range(len(seg_pins)):
        seg_name.append(machine.Pin(seg_pins[i], machine.Pin.OUT))

    for i in range(len(seg_pins)):
        seg_name[i].value(0)

        
def display(num):
    """ Display the desired number """
    for i in range(len(seg_name)):
        values = seg_values[num]
        seg_name[i].value(not values[i])

################ Connect to esp8266 as an Access Point ########################

essid = 'MicroPython-xxxxxx'  # the x’s are replaced with part of the MAC address of esp
password = 'micropythoN'
# ip_address = '192.168.4.1'

# create instance of the object for an access point 
# (for other devices to connect to the ESP8266)
ap_if = network.WLAN(network.AP_IF)

# Activate the access point interface 
ap_if.active(True)

# Configure the access point with the essid and password
ap_if.connect(essid=essid, password=password)

while ap_if.active() == False:
    pass

print('Connection successful')

# The network settings of the interface 
# The returned values are: IP address, netmask, gateway, DNS.
print(ap_if.ifconfig())

############################### Web Page ####################################
def web_page():
    html = """
    <html>

        <head>

        <title>ESP-8266 Web Server</title> 
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            <p><a href="/?seg=inc"><button class="button">Increment</button></a></p>
            <p><a href="/?seg=dec"><button class="button button2">Decrement</button></a></p>
            <p><a href="/?seg=reset"><button class="button button3">Reset</button></a></p>
        </body>

        </html>"""
    return html

############### create a socket and connect to web server ####################
try:
    # create a socket server
    # AF_INET refers to the address family ipv4. 
    # The SOCK_STREAM means connection oriented TCP protocol.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error:
    print("Socket creation failed with error {}".format(str(socket.error)))

# bind associates the socket with a specific network interface and port number
# the empty string refers to the localhost IP address (eps-8266)
# and it means that the server will accept connections on all available IPv4 interfaces
s.bind(('', 80)) 

# max numbers of connections
# enables a server to accept connections
s.listen(5)

while True:

    # wait for an incoming connection
    # When a client connects, it returns a new socket object (conn) 
    # representing the connection and a tuple holding the address of the client
    conn, addr = s.accept() 
    print('Got a connection from {}'.format(str(addr)))

    request = conn.recv(1024)
    request = str(request)
    print("Request {}".format(str(request)))

    seg_inc = request.find('/?seg=inc')
    seg_dec = request.find('/?seg=dec')
    seg_reset = request.find('/?seg=reset')
    print("Inc: {}        Dec:{}        Reset:{}".format(seg_inc, seg_dec, seg_reset))

    if seg_inc == 6:
        print('Increment')
        if counter == 9:
            counter = 0  # reset counter 
            display(counter) # display zero 

        elif 0 <= counter < 9:
            counter += 1  # increment counter 
            display(counter) # display counter

    if seg_dec == 6:
        print('Decrement')
        if counter == 0: 
            counter = 9   # reset counter 
            display(counter)  # display zero
    
        elif 0 < counter <= 9:
            counter -= 1    # deecrement counter
            display(counter)  # display counter

    if seg_reset == 6:
        print("Reset")
        counter = 0
        display(counter)

    response = web_page() # the HTML text returned by the web page
    
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close() 
    













