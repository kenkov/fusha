==============================
fusha.py
==============================

Fusha is an easily customizable progress bar module for Python.
It contains several progress bars which you can use after installing it; however, you can write your own
progress bars to inherit the class provided in this package.

License
---------

MIT License (MIT)

Features
----------

*   You can use fusha by using the **with** statement as follows;

    .. code-block:: python

        with Fusha():
            waiting_function()

*   You can write your own progresss bars by inheriting
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

    # FushaBar
    print "Fusha start"
    with Fusha(interval=0.12, title='now loading ...'):
        time.sleep(3)
    print "finish"

.. image:: http://kenkov.jp/_images/software/Fusha.gif

.. code-block:: python

    print "FushaBar start"
    with FushaBar(interval=0.12, bar_len=20) as f:
        for i in range(100):
            f.update(i)
            time.sleep(.1)
    print "finish"

.. image:: http://kenkov.jp/_images/software/FushaBar.gif

.. code-block:: python

    print "FushaBubble start"
    with FushaBubble(interval=0.2, title="now loading ..."):
        time.sleep(3)
    print "finish"

.. image:: http://kenkov.jp/_images/software/FushaBubble.gif


Application
--------------

The following code downloads a content with the FushaBar progress bar.

.. code-block:: python

    from urllib.request import urlretrieve as retrieve
    from fusha import FushaBar


    url = "http://here/is/the/url/which/you/want/to/download"
    with FushaBar(bar_len=100) as f:
        retrieve(
            url,
            filename="hogefuga"
            reporthook=lambda count, total, size: f.update(
                int(100 * float(count) * total / size))
        )

How to Customize
-------------------

You can create your own progress bars.

First, implement a new class which inherits the **FushaTemplate** class provided in this module.
Then, override two methods - **format** and **exit_format** .
The **format** method will be called while your function running in the **with** statement.
On the other hand, the **exit_format** method will be called after your function is finished.
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
