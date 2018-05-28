.. _asyncio-howto:

============================
Getting Started with asyncio
============================

Building Understanding
======================

The terminology and jargon around concurrency, asynchronous communication, 
and coroutines can obscure the different concepts of what the asyncio module provides in Python.

This section strives to break down the jargon and increase understanding about
asyncio by:

- sharing the ultimate goal of asyncio
- explaining asynchronous programming and its comparison to synchronous programming
- describing what a coroutine is
- creating a timeline of the different coroutine approaches used in Python's history

An Important Goal
-----------------

"The ultimate goal is to help establish a common, easily approachable, mental
model of asynchronous programming in Python and make it as close to
synchronous programming as possible." - PEP 492

Understanding asynchronous programming
--------------------------------------

Why asynchronous programming?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- web growth
- many long lived connections
- efficiency of resources

Asynchronous vs Synchronous
~~~~~~~~~~~~~~~~~~~~~~~~~~~

synchronous - step by step through time; meticulous can't go out of order

asynchronous - planning a party; workers do what they can do until they reach
a roadblock or bottleneck; when the roadblock or bottleneck is removed; continue
working

From Generators to Native Coroutines
------------------------------------

Slightly complicating the understanding of coroutines in Python is that there exists
more than one implementation of coroutines.
As Python grew and evolved, the language added generators, then coroutines via enhanced generators, and
recently coroutines using async/await in the asyncio module.

Generators -> Coroutines (*generator-based*) via Enhanced Generators -> Coroutines (*native*) in asyncio

What is a Generator?
~~~~~~~~~~~~~~~~~~~~

Generators are almost coroutines.
Generators can not yield control easily.
Pass values into a generator when it has suspended.
Generators don't allow easy cleanup.

Using generators to create limited coroutines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initially, when PEP 342 was accepted, coroutine behavior was created by enhancing Python Generators.
We'll refer to these as *generator-based* coroutines. 

PEP 342 Coroutines via Enhanced Generators
- added yield to generators
- yield (like pause in a video game)
- closely tied to generators

Native Coroutines
~~~~~~~~~~~~~~~~~

Beginning with PEP 492 and Python 3.6, a proper standalone concept of coroutines was added.
We refer to these as *native* coroutines, and these *native* coroutines rely on the ``async`` and
``await`` keywords.

PEP 492 Coroutines with async/await syntax
- provides a proper standalone concept of coroutines
- adds syntax to support this concept

Most often, especially when writing new code, you will choose to use *native* coroutines (``async`` and ``await``).

Overview of the asyncio module
==============================

High-level asyncio
------------------

High-level async/await
----------------------

* :keyword:`async` and :keyword:`await` are reserved keywords.

A basic tutorial
================

- show how to use asyncio.run() 
- basic functions like asyncio.sleep()
- teach that asyncio programs are all about async/await and *not* about 
  callbacks or event loops

High-level APIs
===============

Tasks, Streams, Subprocesses, few other functions

Low-level APIs
==============

Preface
-------
talk a bit about everything: 
- what's an event loop, 
- what is a Future
- what is a Transport)
 
Futures
-------

Event loop APIs
---------------

Transports and Protocols
------------------------

(when to use and when not to use them)

Tutorials
=========

  - High-level networking server
  - HTTP application
  - Low-level protocol implementation using Transports
  - etc

Resources
=========

- Yury's 2017 PyCon talk
- Other PyCon talks
- Caleb Hattingh's Book
- Guido/Jesse asyncio paper
- Brett's blog post

Background from release notes
=============================

* PEP 567 Context Variables: The new :mod:`contextvars` module and a set of
  :ref:`new C APIs <contextvarsobjects>` introduce
  support for *context variables*.  Context variables are conceptually
  similar to thread-local variables.  Unlike TLS, context variables
  support asynchronous code correctly.

  The :mod:`asyncio` and :mod:`decimal` modules have been updated to use
  and support context variables out of the box.  Particularly the active
  decimal context is now stored in a context variable, which allows
  decimal operations to work with the correct context in asynchronous code.

asyncio
-------

The :mod:`asyncio` module has received many new features, usability and
:ref:`performance improvements <whatsnew37-asyncio-perf>`.  Notable changes
include:

* The new :term:`provisional <provisional api>` :func:`asyncio.run` function can
  be used to run a coroutine from synchronous code by automatically creating and
  destroying the event loop.
  (Contributed by Yury Selivanov in :issue:`32314`.)

* asyncio gained support for :mod:`contextvars`.
  :meth:`loop.call_soon() <asyncio.AbstractEventLoop.call_soon>`,
  :meth:`loop.call_soon_threadsafe() <asyncio.AbstractEventLoop.call_soon_threadsafe>`,
  :meth:`loop.call_later() <asyncio.AbstractEventLoop.call_later>`,
  :meth:`loop.call_at() <asyncio.AbstractEventLoop.call_at>`, and
  :meth:`Future.add_done_callback() <asyncio.Future.add_done_callback>`
  have a new optional keyword-only *context* parameter.
  :class:`Tasks <asyncio.Task>` now track their context automatically.
  See :pep:`567` for more details.
  (Contributed by Yury Selivanov in :issue:`32436`.)

* The new :func:`asyncio.create_task` function has been added as a shortcut
  to ``asyncio.get_event_loop().create_task()``.
  (Contributed by Andrew Svetlov in :issue:`32311`.)

* The new :meth:`loop.start_tls() <asyncio.AbstractEventLoop.start_tls>`
  method can be used to upgrade an existing connection to TLS.
  (Contributed by Yury Selivanov in :issue:`23749`.)

* The new :meth:`loop.sock_recv_into() <asyncio.AbstractEventLoop.sock_recv_into>`
  method allows reading data from a socket directly into a provided buffer making
  it possible to reduce data copies.
  (Contributed by Antoine Pitrou in :issue:`31819`.)

* The new :func:`asyncio.current_task` function returns the currently running
  :class:`~asyncio.Task` instance, and the new :func:`asyncio.all_tasks`
  function returns a set of all existing ``Task`` instances in a given loop.
  The :meth:`Task.current_task() <asyncio.Task.current_task>` and
  :meth:`Task.all_tasks() <asyncio.Task.all_tasks>` methods have been deprecated.
  (Contributed by Andrew Svetlov in :issue:`32250`.)

* The new *provisional* :class:`~asyncio.BufferedProtocol` class allows
  implementing streaming protocols with manual control over the receive buffer.
  (Contributed by Yury Selivanov in :issue:`32251`.)

* The new :func:`asyncio.get_running_loop` function returns the currently
  running loop, and raises a :exc:`RuntimeError` if no loop is running.
  This is in contrast with :func:`asyncio.get_event_loop`, which will *create*
  a new event loop if none is running.
  (Contributed by Yury Selivanov in :issue:`32269`.)

* The new :meth:`StreamWriter.wait_closed() <asyncio.StreamWriter.wait_closed>`
  coroutine method allows waiting until the stream writer is closed.  The new
  :meth:`StreamWriter.is_closing() <asyncio.StreamWriter.is_closing>` method
  can be used to determine if the writer is closing.
  (Contributed by Andrew Svetlov in :issue:`32391`.)

* The new :meth:`loop.sock_sendfile() <asyncio.AbstractEventLoop.sock_sendfile>`
  coroutine method allows sending files using :mod:`os.sendfile` when possible.
  (Contributed by Andrew Svetlov in :issue:`32410`.)

* The new :meth:`Task.get_loop() <asyncio.Task.get_loop>` and
  :meth:`Future.get_loop() <asyncio.Future.get_loop>` methods
  return the instance of the loop on which a task or a future were created.
  :meth:`Server.get_loop() <asyncio.Server.get_loop>` allows doing the same for
  :class:`asyncio.Server` objects.
  (Contributed by Yury Selivanov in :issue:`32415` and
  Srinivas Reddy Thatiparthy in :issue:`32418`.)

* It is now possible to control how instances of :class:`asyncio.Server` begin
  serving.  Previously, the server would start serving immediately when created.
  The new *start_serving* keyword argument to
  :meth:`loop.create_server() <asyncio.AbstractEventLoop.create_server>` and
  :meth:`loop.create_unix_server() <asyncio.AbstractEventLoop.create_unix_server>`,
  as well as :meth:`Server.start_serving() <asyncio.Server.start_serving>`, and
  :meth:`Server.serve_forever() <asyncio.Server.serve_forever>`
  can be used to decouple server instantiation and serving.  The new
  :meth:`Server.is_serving() <asyncio.Server.is_serving>` method returns ``True``
  if the server is serving.  :class:`~asyncio.Server` objects are now
  asynchronous context managers::

      srv = await loop.create_server(...)

      async with srv:
          # some code

      # At this point, srv is closed and no longer accepts new connections.

  (Contributed by Yury Selivanov in :issue:`32662`.)

* Callback objects returned by
  :func:`loop.call_later() <asyncio.AbstractEventLoop.call_later>`
  gained the new :meth:`when() <asyncio.TimerHandle.when>` method which
  returns an absolute scheduled callback timestamp.
  (Contributed by Andrew Svetlov in :issue:`32741`.)

* The :meth:`loop.create_datagram_endpoint() \
  <asyncio.AbstractEventLoop.create_datagram_endpoint>` method
  gained support for Unix sockets.
  (Contributed by Quentin Dawans in :issue:`31245`.)

* The :meth:`loop.create_connection() <asyncio.AbstractEventLoop.create_connection>`,
  :meth:`loop.create_server() <asyncio.AbstractEventLoop.create_server>`,
  :meth:`loop.create_unix_server() <asyncio.AbstractEventLoop.create_unix_server>`, and
  :meth:`loop.create_accepted_socket() <asyncio.BaseEventLoop.connect_accepted_socket>`
  now accept the *ssl_handshake_timeout* keyword argument.
  (Contributed by Neil Aspinall in :issue:`29970`.)

* The new :meth:`Handle.cancelled() <asyncio.Handle.cancelled>` method returns
  ``True`` if the callback was cancelled.
  (Contributed by Marat Sharafutdinov in :issue:`31943`.)

* The asyncio source has been converted to use the
  :keyword:`async`/:keyword:`await` syntax.
  (Contributed by Andrew Svetlov in :issue:`32193`.)

* The new :meth:`ReadTransport.is_reading() <asyncio.ReadTransport.is_reading>`
  method can be used to determine the reading state of the transport.
  Additionally, calls to
  :meth:`ReadTransport.resume_reading() <asyncio.ReadTransport.resume_reading>`
  and :meth:`ReadTransport.pause_reading() <asyncio.ReadTransport.pause_reading>`
  are now idempotent.
  (Contributed by Yury Selivanov in :issue:`32356`.)

* Loop methods which accept socket paths now support passing
  :term:`path-like objects <path-like object>`.
  (Contributed by Yury Selivanov in :issue:`32066`.)

* In :mod:`asyncio` TCP sockets on Linux are now created with ``TCP_NODELAY``
  flag set by default.
  (Contributed by Yury Selivanov and Victor Stinner in :issue:`27456`.)

* Exceptions occurring in cancelled tasks are no longer logged.
  (Contributed by Yury Selivanov in :issue:`30508`.)

Several ``asyncio`` APIs have been
:ref:`deprecated <whatsnew37-asyncio-deprecated>`.

The :mod:`asyncio` module received a number of notable optimizations for
commonly used functions:

* The :func:`asyncio.get_event_loop` function has been reimplemented in C to
  make it up to 15 times faster.
  (Contributed by Yury Selivanov in :issue:`32296`.)

* :class:`asyncio.Future` callback management has been optimized.
  (Contributed by Yury Selivanov in :issue:`32348`.)

* :func:`asyncio.gather` is now up to 15% faster.
  (Contributed by Yury Selivanov in :issue:`32355`.)

* :func:`asyncio.sleep` is now up to 2 times faster when the *delay*
  argument is zero or negative.
  (Contributed by Andrew Svetlov in :issue:`32351`.)

* The performance overhead of asyncio debug mode has been reduced.
  (Contributed by Antoine Pitrou in :issue:`31970`.)

.. _whatsnew37-asyncio-deprecated:

deprecated
----------

Support for directly ``await``-ing instances of :class:`asyncio.Lock` and
other asyncio synchronization primitives has been deprecated.  An
asynchronous context manager must be used in order to acquire and release
the synchronization resource.  See :ref:`async-with-locks` for more
information.
(Contributed by Andrew Svetlov in :issue:`32253`.)

The :meth:`asyncio.Task.current_task` and :meth:`asyncio.Task.all_tasks`
methods have been deprecated.
(Contributed by Andrew Svetlov in :issue:`32250`.)

3.6
* The :mod:`asyncio` module has received new features, significant
  usability and performance improvements, and a fair amount of bug fixes.
  Starting with Python 3.6 the ``asyncio`` module is no longer provisional
  and its API is considered stable.

.. _whatsnew36-pep525:

PEP 525: Asynchronous Generators
--------------------------------

:pep:`492` introduced support for native coroutines and ``async`` / ``await``
syntax to Python 3.5.  A notable limitation of the Python 3.5 implementation
is that it was not possible to use ``await`` and ``yield`` in the same
function body.  In Python 3.6 this restriction has been lifted, making it
possible to define *asynchronous generators*::

    async def ticker(delay, to):
        """Yield numbers from 0 to *to* every *delay* seconds."""
        for i in range(to):
            yield i
            await asyncio.sleep(delay)

The new syntax allows for faster and more concise code.

.. seealso::

   :pep:`525` -- Asynchronous Generators
      PEP written and implemented by Yury Selivanov.


.. _whatsnew36-pep530:

PEP 530: Asynchronous Comprehensions
------------------------------------

:pep:`530` adds support for using ``async for`` in list, set, dict
comprehensions and generator expressions::

    result = [i async for i in aiter() if i % 2]

Additionally, ``await`` expressions are supported in all kinds
of comprehensions::

    result = [await fun() for fun in funcs if await condition()]

.. seealso::

 :pep:`530` -- Asynchronous Comprehensions
    PEP written and implemented by Yury Selivanov.

asyncio
-------

Starting with Python 3.6 the ``asyncio`` module is no longer provisional and its
API is considered stable.

Notable changes in the :mod:`asyncio` module since Python 3.5.0
(all backported to 3.5.x due to the provisional status):

* The :func:`~asyncio.get_event_loop` function has been changed to
  always return the currently running loop when called from couroutines
  and callbacks.
  (Contributed by Yury Selivanov in :issue:`28613`.)

* The :func:`~asyncio.ensure_future` function and all functions that
  use it, such as :meth:`loop.run_until_complete() <asyncio.BaseEventLoop.run_until_complete>`,
  now accept all kinds of :term:`awaitable objects <awaitable>`.
  (Contributed by Yury Selivanov.)

* New :func:`~asyncio.run_coroutine_threadsafe` function to submit
  coroutines to event loops from other threads.
  (Contributed by Vincent Michel.)

* New :meth:`Transport.is_closing() <asyncio.BaseTransport.is_closing>`
  method to check if the transport is closing or closed.
  (Contributed by Yury Selivanov.)

* The :meth:`loop.create_server() <asyncio.BaseEventLoop.create_server>`
  method can now accept a list of hosts.
  (Contributed by Yann Sionneau.)

* New :meth:`loop.create_future() <asyncio.BaseEventLoop.create_future>`
  method to create Future objects.  This allows alternative event
  loop implementations, such as
  `uvloop <https://github.com/MagicStack/uvloop>`_, to provide a faster
  :class:`asyncio.Future` implementation.
  (Contributed by Yury Selivanov in :issue:`27041`.)

* New :meth:`loop.get_exception_handler() <asyncio.BaseEventLoop.get_exception_handler>`
  method to get the current exception handler.
  (Contributed by Yury Selivanov in :issue:`27040`.)

* New :meth:`StreamReader.readuntil() <asyncio.StreamReader.readuntil>`
  method to read data from the stream until a separator bytes
  sequence appears.
  (Contributed by Mark Korenberg.)

* The performance of :meth:`StreamReader.readexactly() <asyncio.StreamReader.readexactly>`
  has been improved.
  (Contributed by Mark Korenberg in :issue:`28370`.)

* The :meth:`loop.getaddrinfo() <asyncio.BaseEventLoop.getaddrinfo>`
  method is optimized to avoid calling the system ``getaddrinfo``
  function if the address is already resolved.
  (Contributed by A. Jesse Jiryu Davis.)

* The :meth:`loop.stop() <asyncio.BaseEventLoop.stop>`
  method has been changed to stop the loop immediately after
  the current iteration.  Any new callbacks scheduled as a result
  of the last iteration will be discarded.
  (Contributed by Guido van Rossum in :issue:`25593`.)

* :meth:`Future.set_exception <asyncio.futures.Future.set_exception>`
  will now raise :exc:`TypeError` when passed an instance of
  the :exc:`StopIteration` exception.
  (Contributed by Chris Angelico in :issue:`26221`.)

* New :meth:`loop.connect_accepted_socket() <asyncio.BaseEventLoop.connect_accepted_socket>`
  method to be used by servers that accept connections outside of asyncio,
  but that use asyncio to handle them.
  (Contributed by Jim Fulton in :issue:`27392`.)

* ``TCP_NODELAY`` flag is now set for all TCP transports by default.
  (Contributed by Yury Selivanov in :issue:`27456`.)

* New :meth:`loop.shutdown_asyncgens() <asyncio.AbstractEventLoop.shutdown_asyncgens>`
  to properly close pending asynchronous generators before closing the
  loop.
  (Contributed by Yury Selivanov in :issue:`28003`.)

* :class:`Future <asyncio.Future>` and :class:`Task <asyncio.Task>`
  classes now have an optimized C implementation which makes asyncio
  code up to 30% faster.
  (Contributed by Yury Selivanov and INADA Naoki in :issue:`26081`
  and :issue:`28544`.)
