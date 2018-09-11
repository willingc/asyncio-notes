# asyncio for developers

## asyncio library files (alphabetical)

|  file  |  purpose   |
|--------|------------|
| \__init\__.py |  |
| base_events.py | Base implementation of event loop |
| base_futures.py | Check for a future and helper functions |
| base_subprocess.py | Base subprocess transport and r/w pipe protocols |
| base_tasks.py | task and its stack info |
| constants.py | misc constants for connections and comms |
| coroutines.py | coroutine helpers and wrapper |
| events.py | Event loop abstract classes and handles |
| format_helpers.py | callback format helpers |
| futures.py | Future class |
| locks.py | lock primitives, context, Event, Condition, Semaphore, BoundedSemaphore |
| log.py | logger for asyncio|
| proactor_events.py | event loop using "notify on completion" mux; windows |
| protocols.py | Protocol base classes |
| queues.py | queues - useful for producer/consumer |
| runners.py | run a coroutine |
| selector_events.py | event loop using "notify-when-ready" mux; unix |
| ssl_proto.py | SSL protocol and pipe |
| streams.py | Stream readers and writers |
| subprocess.py | subprocess readers and writers |
| tasks.py | Support for tasks, coroutines and the scheduler; Task - coroutine wrapped in a Future |
| transports.py | Base class for transports; types of transports |
| unix_events.py | Selector event loop for Unix with signal handling |
| windows_events.py | Selector and proactor event loops for Windows |
| windows_utils.py | Windows helper utilities |

## async library files (by functionality)

| file | purpose |
|------|---------|
| **Event Loop** | |
| base_events.py | Base implementation of event loop |
| events.py | Event loop abstract classes and handles |
| selector_events.py | event loop using "notify-when-ready" mux; unix |
| proactor_events.py | event loop using "notify on completion" mux; windows |
| unix_events.py | Selector event loop for Unix with signal handling |
| windows_events.py | Selector and proactor event loops for Windows |
| **Futures** | |
| base_futures.py | Check for a future and helper functions |
| futures.py | Future class |
| **Coroutines** | |
| coroutines.py | coroutine helpers and wrapper |
| **Tasks** | |
| base_tasks.py | task and its stack info |
| tasks.py | Support for tasks, coroutines and the scheduler; Task - coroutine wrapped in a Future |
| **Subprocesses
| base_subprocess.py | Base subprocess transport and r/w pipe protocols |
| subprocess.py | subprocess readers and writers |
| **Comms** | |
| runners.py | run a coroutine |
| transports.py | Base class for transports; types of transports |
| protocols.py | Protocol base classes |
| ssl_proto.py | SSL protocol and pipe |
| streams.py | Stream readers and writers |
| locks.py | lock primitives, context, Event, Condition, Semaphore, BoundedSemaphore |
| **Implementations** |  |
| format_helpers.py | callback format helpers |
| queues.py | queues - useful for producer/consumer |
| **Utilities** | |
| log.py | logger for asyncio|
| constants.py | misc constants for connections and comms |
| windows_utils.py | Windows helper utilities |
| \__init\__.py | |