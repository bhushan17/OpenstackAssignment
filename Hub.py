from gevent import monkey
monkey.patch_all()  # Patch everything
import gevent
import time
import socket
import random


handlersAll = {}

def on(event_name, handler):
    """Binds an event to a function."""
    global handlersAll
    handlers = handlersAll.get(event_name,[])
    if not handler in handlers:
       handlers.append(handler)
    handlersAll[event_name] = handlers

def off(event_name, handler):
    """Unbinds an event to a function."""
    #global handlersAll
    handlers = handlersAll.get(event_name, [])
    handlersAll.remove(handler)

def emit(event_name, *args, **kwargs):
    """Calls an event. You can also pass arguments."""
    #global handlersAll
    gevent.sleep(random.randint(1,22))
    print "Event_NAME   "
    print event_name
    handlers = handlersAll.get(event_name, [])
    for handler in handlers:
       # XXX: If spawned within a greenlet, there's no need to join
       # the greenlet. It is automatically executed.
       gevent.spawn(handler, *args, **kwargs)

def start():
    #gevent.joinall([gevent.spawn(ep) for ep in entry_points])
    gevent.joinall([gevent.spawn(emit,i%3,[])for i in xrange(200)])


#hub = Hub(name='myhub')


def handler1(string):
    # Let's say that this is a long process.
    #time.sleep(5)
    #gevent.sleep(5)
    print "Handler 1 is :%s:" % string


def handler2(string):
    # A slightly long process.
    #time.sleep(1)
    #gevent.sleep(1)
    print "Handler 2 is :%s:" % string


# You can bind multiple events.
on(0, handler1)
on(1, handler2)


# More events.
def handler3(string):
    print "Handler 3 is :%s:" % string
    # You can also emit more events
    


on(2, handler3)



if __name__ == '__main__':
    print "Running awesome!"
    start()
