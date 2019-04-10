import zmq
import sys
import threading
import time
from random import randint, random

def tprint(msg):
    sys.stdout.write(msg + '\n')
    sys.stdout.flush()

class ClientTask(threading.Thread):
    def __init__(self, id):
        self.id = id
        threading.Thread.__init__ (self)

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.DEALER)
        identity = u'worker-%d' % self.id
        socket.identity = identity.encode('ascii')
        socket.connect('tcp://localhost:5570')
        print('Client %s started' % (identity))
        poll = zmq.Poller()
        poll.register(socket, zmq.POLLIN)
        reqs = 0
        
        reqs = reqs + 1
        print('Req #%d sent..' % (reqs))
        socket.send_string("Mensagem enviada")
        
        count = 0
        while count<2:
            count += 1
            msg = socket.recv()
            if msg:
                tprint('Client %s received: %s' % (identity, msg))
            else:
                print("Sem resposta")

        socket.close()
        context.term()

def main():
    client = ClientTask(1)
    client.start()

if __name__ == "__main__":
    main()