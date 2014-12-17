import OSC
import time, threading
import sys
from keyedmarkov import KeyedMarkovEmitter

try:
    listen_on_address = ('127.0.0.1', int(sys.argv[1]))
    send_to_address = ('127.0.0.1', int(sys.argv[2]))
except IndexError, ValueError:
    print "Usage: python markov_server.py [port to listen on] [port to send to] [...keys to use for merkov emitter]"
    exit()

osc_server = OSC.OSCServer(listen_on_address)
osc_server.addDefaultHandlers()

osc_client = OSC.OSCClient()
osc_client.connect( send_to_address )

emitter = KeyedMarkovEmitter()
emitter.setup(16, sys.argv[2:], 2000)

def log_request(id, addr, tags, stuff, source):
    print "--- Data received [" + str(id) + "]: (" + str(OSC.getUrlStr(source)) + " : " + str(addr) + ")"
    print "--- Typetags: [%s]" % tags
    print "--- Data: %s" % stuff
    print ""

def train_system(received_data, delimiter=":"):
    """
    Accepts data of the form:
    [
        "snare:2635",
        "kick:2615"
    ]

    Where the key and the offset are separated by the delimiter. This function
    then trains the emitter on this data as a sequence.
    """
    training_data = []
    for datum in received_data:
        key, offset = datum.split(delimiter)
        d = {
            "key": key,
            "offset": int(offset)
        }
        training_data.append(d)
    emitter.train_sequence(training_data)
    print "[Info] Trained system on data: " + str(training_data)

def reset_system(received_data):
    pass

def export_system(received_data):
    data = emitter.get_data(as_strings=True) # only booleans, not probabilities
    result_strings = []
    for index, datum in enumerate(data):
        print datum
        result_strings.append(str(index) + ":" + "-".join(
            [known_key + "." + str(datum[known_key]) for known_key in emitter.known_keys]
        ))
    return result_strings

def train_system_handler(addr, tags, data, source):
    log_request("train system", addr, tags, data, source)
    train_system(data)
    print "[Info] Sending message: success" 
    osc_client.send( OSC.OSCMessage("/response/train", "train system:success" ) )

def reset_handler(addr, tags, data, source):
    log_request("reset", addr, tags, data, source)
    osc_client.send( OSC.OSCMessage("/response/reset", "reset:success" ) )

def export_data_handler(addr, tags, data, source):
    log_request("data", addr, tags, data, source)
    return_data = export_system(data)
    print "[Info] Returning export data: " + str(return_data)
    osc_client.send( OSC.OSCMessage("/response/export", return_data ) )

def main():
    osc_server.addMsgHandler("/train", train_system_handler)
    osc_server.addMsgHandler("/reset", reset_handler)
    osc_server.addMsgHandler("/data", export_data_handler)

    # Check which handlers we have added
    print "[Info] Registered Callback-functions are :"
    for addr in sorted(osc_server.getOSCAddressSpace()):
        print "[Info] : " + addr

    # Start OSCServer
    print "[Info] Starting OSCServer!"
    print "[Info] Listening at host %s and port %s." % (listen_on_address[0], listen_on_address[1])
    print "[Info] Sending to host %s and port %s." % (send_to_address[0], send_to_address[1])
    print "[Info] Use ctrl-C to quit."
    st = threading.Thread( target = osc_server.serve_forever )
    st.start()

    try :
        while 1 :
            time.sleep(5)

    except KeyboardInterrupt :
        print "\n[Info] Closing OSCServer."
        osc_server.close()
        print "[Info] Waiting for Server-thread to finish"
        st.join() ##!!!
        print "[Info] Done!"

if __name__ == '__main__':
    main()
