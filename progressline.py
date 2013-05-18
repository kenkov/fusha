#! /usr/bin/env python
# coding:utf-8

from __future__ import division
import threading
import time
import sys
import abc


class FushaTemplate(threading.Thread):
    """Template class"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, interval=0.12):
        threading.Thread.__init__(self)
        self._interval = interval
        self._stop_flag = False
        self.setDaemon(True)

    @abc.abstractmethod
    def format(self):
        pass

    @abc.abstractmethod
    def exit_format(self):
        pass

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._stop_flag = True
        sys.stdout.write(self.exit_format())
        sys.stdout.flush()

    def run(self):
        while not self._stop_flag:
            sys.stdout.write(self.format())
            sys.stdout.flush()
            time.sleep(self._interval)


class Fusha(FushaTemplate):

    def __init__(self,
                 interval=0.12,
                 title='waiting ...'):
        FushaTemplate.__init__(self, interval)
        self.title = title
        self._count = 0

    def format(self):
        if self._count in [0, 4]:
            fmt = '\r{0} -'.format(self.title)
        elif self._count in [1, 5]:
            fmt = '\r{0} \\'.format(self.title)
        elif self._count in [3, 7]:
            fmt = '\r{0} /'.format(self.title)
        elif self._count in [2, 6]:
            fmt = '\r{0} |'.format(self.title)
        # set count
        if self._count == 7:
            self._count = 0
        else:
            self._count += 1

        return fmt

    def exit_format(self):
        return '\r{0} done\n'.format(self.title)


class FushaBubble(FushaTemplate):

    def __init__(self,
                 interval=0.12,
                 title='waiting ...'):
        FushaTemplate.__init__(self, interval)
        self.title = title
        self._count = 0

    def format(self):
        if self._count % 3 == 0:
            fmt = '\r{0} .'.format(self.title)
        elif self._count % 3 == 1:
            fmt = '\r{0} o'.format(self.title)
        else:
            fmt = '\r{0} O'.format(self.title)
        # set count
        if self._count == 2:
            self._count = 0
        else:
            self._count += 1
        return fmt

    def exit_format(self):
        return '\r{0} done\n'.format(self.title)


class FushaBar(FushaTemplate):
    def __init__(self, interval=0.12, bar_len=10):
        FushaTemplate.__init__(self, interval)
        self._percent = 0
        self._bar_len = bar_len

    def format(self):
        interval = 100 // self._bar_len
        finished = self._percent // interval
        return '\r{:3}% [{}{}]'.format(
            self._percent,
            "="*(finished),
            " "*(self._bar_len-finished))

    def exit_format(self):
        return '\r{:3}% [{}]\n'.format(
            100,
            "="*(self._bar_len))

    def update(self, i):
        self._percent = i


if __name__ == '__main__':

    print "Fusha start"
    with Fusha(interval=0.12, title='now loading ...'):
        time.sleep(3)
    print "finish"

    print "FushaBar start"
    with FushaBar(interval=0.12, bar_len=20) as f:
        for i in range(100):
            f.update(i)
            time.sleep(.1)
    print "finish"

    print "FushaBubble start"
    with FushaBubble(interval=0.2, title="now loading ..."):
        time.sleep(3)
    print "finish"
