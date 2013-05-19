==============================
fusha.py
==============================

Fusha is an easily customizable progress bar module for Python.
It contains default progress bars. However, you can write your own
progress bar easily to inherit the class provided in this package.

Features
----------

*   You can easily use fusha by using the **with** statement as follows;

    .. code-block:: python

        with Fusha():
            waiting_function()

*   You can easily write your own progress bar by inheriting
    the **FushaTemplate** class as follows;

    .. code-block:: python

        class Fusha(FushaTemplate):

            def __init__(self, interval=0.12)
                FushaTemplate.__init__(self, interval)

            def format(self):
                return waiting_format

            def exit_format(self):
                return exit_format


Installation
-------------

.. code-block:: sh

    $ python setup.py install

or

.. code-block:: sh

    $ pip install fusha

Getting Started
-----------------

Fusha provides default three progress bars - Fusha, FushaBar, and FushaBubble.

The most easiest way to use Fusha is just creating an instance of fusha with **with** statement
before calling your function which you must wait for a while:

.. code-block:: python

    import time
    from fusha import Fusha

    with Fusha():
        time.sleep(3)

That's all.

Default Progress Bars
-----------------------

Fusha provides three default progress bars. You can use them as follows.

.. code-block:: python

    import time
    from fusha import Fusha, FushaBar, FushaBubble

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

Screenshots
-------------

Fusha

.. image:: http://kenkov.jp/_images/software/Fusha.gif

FushaBar

.. image:: http://kenkov.jp/_images/software/FushaBar.gif

FushaBubble

.. image:: http://kenkov.jp/_images/software/FushaBubble.gif

How to Customize
-------------------

You can easily create your own progress bar.

First, you should create a new class which inherits the **FushaTemplate** class.
Then, you should override two methods - **format** and **exit_format** .
The **format** method will be called while your function is running in the with statement;
on the other hand, the **exit_format** will be called after finishing your function.
Both functions should return string.

The following code is for FushaBubble:

.. code-block:: sh

    from fusha import FushaTemplate

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

License
---------

The MIT License (MIT)
