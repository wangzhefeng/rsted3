***************
说明
***************

此项目是从 `rsted <https://github.com/anru/rsted>`_  库直接修改的，
将原来的代码修改为 Pytonn3 版本

.. code-block:: bash

    $ 2to3 --output-dir=/path/to/rsted3 -W -n /path/to/rsted2

***************
原来的 README
***************

Simple online editor for reStructuredText on Flask.

Try it where: http://rst.ninjs.org/

Getting setup
===============

Requirements for rsted:

* Flask
* rst2html (from Docutils)

These requirements are expressed in the pip-requirements.txt file and may be
installed by running the following (from within a virtual environment)::

    pip install -r pip-requirements.txt


How to run
===============

Your Environment
------------------
From within your environment, just run::

    ./application.py

This will start a server on port 5001.  Just visit http://localhost:5001/ in
your browser.

Docker
------------------
In a docker installed host, just build and run::

    docker build -t rsted .
    docker run --name rsted --rm -p 5001:5001 rsted

A server starts on port 5001. Please adjust it, if you need another port
by changing run command above. And then just visit http://localhost:5001/ in
your browser.
