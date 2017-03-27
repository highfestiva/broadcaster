# broadcaster.py

Simplistic component for publishing any type of data from a background thread. This is the minimum code you need for [server push](https://www.w3schools.com/html/html5_serversentevents.asp).


# Example of use:

```python
import broadcaster
from threading import Thread
from time import sleep

def listen():
    for msg in broadcaster.listen('bananas'):
        assert msg == 'one yellow'
        break

worker = Thread(target=listen)
worker.start()
sleep(0.1)    # Wait for listener thread to register.
broadcaster.publish('bananas', 'one yellow')
worker.join()
```
