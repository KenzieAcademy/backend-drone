#!/usr/bin/env python
"""
A class to represent a single Tello drone
"""

import socket
import threading
import time
from stats import Stats


class Tello:
    def __init__(self):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind((self.local_ip, self.local_port))

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_adderss = (self.tello_ip, self.tello_port)
        self.log = []

        self.MAX_TIME_OUT = 10.0
        self.abort = False

    def __enter__(self):
        print("Tello __enter__ ...")
        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(name="TelloRecv", target=self._receive_thread)
        # self.receive_thread.daemon = True
        self.receive_thread.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Tello __exit__ ...")
        #self.socket.close()
        self.abort = True
        self.receive_thread.join()
        print("Tello __exit__ done")

    def send_command(self, command):
        """
        Send a command to the ip address. Will be blocked until
        the last command receives an 'OK'.
        If the command fails (either b/c time out or error),
        will try to resend the command
        :param command: (str) the command to send
        :param ip: (str) the ip of Tello
        :return: The latest command response
        """
        self.log.append(Stats(command, len(self.log)))

        print('sending command: {} to {}' .format(command, self.tello_ip))
        self.socket.sendto(command.encode('utf-8'), self.tello_adderss)

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.MAX_TIME_OUT:
                print 'Max timeout exceeded... command %s' % command
                # TODO: is timeout considered failure or next command still get executed
                # now, next one got executed
                return
        print 'Done!!! sent command: %s to %s' % (command, self.tello_ip)

    def _receive_thread(self):
        """Listen to responses from the Tello.

        Runs as a thread, sets self.response to whatever the Tello last returned.

        """
        print("Tello thread enter")

        while not self.abort:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('Recvd from {}: {}'.format(ip, self.response))

                self.log[-1].add_response(self.response)
            except socket.error, exc:
                print("SOCKET ERROR: " + str(exc))
            except UnicodeDecodeError as exc:
                print("EXCEPTION: " + str(exc))

        print("Tello thread exit")

    def on_close(self):
        pass
        # for ip in self.tello_ip_list:
        #     self.socket.sendto('land'.encode('utf-8'), (ip, 8889))
        # self.socket.close()

    def get_log(self):
        return self.log
