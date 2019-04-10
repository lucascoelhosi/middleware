import zmq
import sys
import threading, multiprocessing
import time
from random import randint, random

import socket
import json
import requests
import select
from os.path import join


def tprint(msg):
    sys.stdout.write(msg + '\n')
    sys.stdout.flush()

class ServerTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__ (self)

    def run(self):
        context = zmq.Context()
        frontend = context.socket(zmq.ROUTER)
        frontend.bind('tcp://*:5570')
        print(frontend)

        backend = context.socket(zmq.DEALER)
        backend.bind('inproc://backend')
        print(backend)

        workers = []
        worker = ServerWorker(context)
        worker.start()
        workers.append(worker)

        zmq.proxy(frontend, backend)

        frontend.close()
        backend.close()
        context.term()

class ServerWorker(threading.Thread):
    def __init__(self, context):
        threading.Thread.__init__ (self)
        self.context = context

    def run(self):
        worker = self.context.socket(zmq.DEALER)
        worker.connect('inproc://backend')
        tprint('Worker started')

        while True:
            ident, msg = worker.recv_multipart()
            tprint('Dado Recebido: %s -> Usuario: %s' % (msg, ident))
            data = msg.decode("utf-8")

            data_send = requests.post('http://127.0.0.1:5000/todos', json={"task": data})
            data_json = data_send.json()

            data_encode = data_json['task'].encode('ASCII')

            worker.send_multipart([ident, data_encode])            



            data_send = requests.post('http://127.0.0.1:500/todos', json={"task": data})
            data_json = data_send.json()

            data_encode = data_json['task'].encode('ASCII')
            worker.send_multipart([ident, data_encode])

        worker.close()

def main():
    """main function"""
    server = ServerTask()
    server.start()

    server.join()

if __name__ == "__main__":
    main()