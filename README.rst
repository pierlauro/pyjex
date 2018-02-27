.. image:: http://img.shields.io/pypi/v/pyjex.svg
   :target: https://pypi.python.org/pypi/pyjex

.. image:: https://img.shields.io/badge/python-2.x%20--%203.x-blue.svg
	:target: https://github.com/pierlauro/pyjex


Pyjex: PYthon → Java formatting for EXceptions
==============================================

A simple one-liner to format Python's stracktraces in `Java style <https://docs.oracle.com/javase/9/docs/api/java/lang/Throwable.html#printStackTrace-->`_.


Usage
=====

Simply ``import pyjex`` in your code and enjoy.

Example
=======

.. code-block:: python

  def divzero():
    1/0

  if __name__ == '__main__':
    divzero()

**Normal stacktrace**:

.. code-block:: none

    Traceback (most recent call last):
      File "main.py", line 7, in <module>
        divzero()
      File "main.py", line 4, in divzero
        1/0
    ZeroDivisionError: division by zero


**Stacktrace after importing pyjex**:

.. code-block:: none

    ZeroDivisionError: division by zero
	at divzero(main.py:4)
	at <module>(main.py:7)

Installing
==========
``pip install pyjex`` - no dependencies needed.

======

This is free and unencumbered software released into the public domain. For more information, please refer to http://unlicense.org/
