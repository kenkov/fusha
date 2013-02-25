#! /usr/bin/env python
# coding:utf-8

from __future__ import division, print_function
import threading
import time
import sys


class ProgressLine(threading.Thread):

    def __init__(self, interval_time=0.12, title='waiting ...'):
        threading.Thread.__init__(self)
        self.interval_time = interval_time
        self.title = title
        self._stop_flag = False
        self._count = 0
        self.setDaemon(True)

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_value, traceback):
        self._stop_flag = True
        sys.stdout.write('\r{0} done\n'.format(self.title))
        sys.stdout.flush()

    def run(self):
        while not self._stop_flag:
            if self._count in [0, 2, 6]:
                sys.stdout.write('\r{0} -'.format(self.title))
            elif self._count in [1, 5, 9]:
                sys.stdout.write('\r{0} /'.format(self.title))
            elif self._count in [3, 7]:
                sys.stdout.write('\r{0} \\'.format(self.title))
            elif self._count in [4, 8]:
                sys.stdout.write('\r{0} |'.format(self.title))
            sys.stdout.flush()
            if self._count == 9:
                self._count = 0
            else:
                self._count += 1
            time.sleep(self.interval_time)


if __name__ == '__main__':

    print('start get application')
    with ProgressLine(interval_time=0.12, title='now loading ...'):
        time.sleep(3)
    print('finish')
