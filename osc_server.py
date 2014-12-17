import OSC
import time, threading

receive_address = '127.0.0.1', 54321
send_address = '127.0.0.1', 31337

osc_server = OSC.OSCServer(receive_address)
osc_server.addDefaultHandlers()

osc_client = OSC.OSCClient()
osc_client.connect( send_address )


def repeater_handler(addr, tags, stuff, source):
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print "with addr : %s" % addr
    print "typetags %s" % tags
    print "data %s" % stuff
    print "---"

    count = stuff[0]
    message = stuff[1]
    full_message = repeater(count, message)
    osc_client.send( OSC.OSCMessage("/repeater/message", full_message ) )

def repeater(count, message):
    return ' '.join([message] * count)

osc_server.addMsgHandler("/repeater", repeater_handler)

# Check which handlers we have added
print "Registered Callback-functions are :"
for addr in sorted(osc_server.getOSCAddressSpace()):
    print addr

# Start OSCServer
print "\nStarting OSCServer!\nListening at host %s and port %s.\nSending to host %s and port %s.\nUse ctrl-C to quit." % (receive_address[0], receive_address[1], send_address[0], send_address[1])
st = threading.Thread( target = osc_server.serve_forever )
st.start()

try :
    while 1 :
        time.sleep(5)

except KeyboardInterrupt :
    print "\nClosing OSCServer."
    osc_server.close()
    print "Waiting for Server-thread to finish"
    st.join() ##!!!
    print "Done!"
