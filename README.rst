==============================
fusha.py
==============================

Fusha is an easily customizable progress bar package for Python.
It contains default progress bars. However, you can write your own
progress bar easily to inherit the class provided in this package.

Installation
-------------

.. code-block:: python

    $ python setup.py install

How to Use
---------------

.. code-block:: python

    import time
    import fusha

    print('start')
    with fusha.Fusha(0.12, title='now loading ...'):
        time.sleep(3)
    print('finish')

.. code-block:: sh

    start get application
    now loading ... done
    finish

Screenshots
-------------

Fusha

.. image:: http://kenkov.jp/_images/software/Fusha.gif

FushaBar

.. image:: http://kenkov.jp/_images/software/FushaBar.gif

FushaBubble

.. image:: http://kenkov.jp/_images/software/FushaBubble.gif
