from gevent import monkey
import gevent
import random
import socket
import time


monkey.patch_all()  # Patch everything


class Hub:
    
    def __init__(self):
        self.handlersAll = {}
    
    
    def on(self, event_name, handler):
        """Binds an event to a function."""
        handlers = self.handlersAll.get(event_name,[])
        if not handler in handlers:
           handlers.append(handler)
        self.handlersAll[event_name] = handlers
    
    def off(self, event_name, handler):
        """Unbinds an event to a function."""
        #global self.handlersAll
        handlers = self.handlersAll.get(event_name, [])
        self.handlersAll.remove(handler)
    
    def emit(self, event_name, *args, **kwargs):
        """Calls an event. You can also pass arguments."""
        #global self.handlersAll
        #gevent.sleep(random.randint(1,5))
        print "Event_NAME   "
        print event_name
        handlers = self.handlersAll.get(event_name, [])
        for handler in handlers:
           # XXX: If spawned within a greenlet, there's no need to join
           # the greenlet. It is automatically executed.
           gevent.spawn(handler, *args, **kwargs)
    
    def start(self, event_name):
        #gevent.joinall([gevent.spawn(ep) for ep in entry_points])
        #gevent.joinall([gevent.spawn(self.emit,i%3,[])for i in xrange(200)])
        gevent.joinall([gevent.spawn(self.emit,event_name,[])])
    
   
    def handler1(self, string):
        gevent.sleep(random.randint(1,5))
        print "Handler 1 is :%s:" % string
    
    def handler2(self, string):
        gevent.sleep(random.randint(1,5))
        print "Handler 2 is :%s:" % string
        
    def handler3(self, string):
        gevent.sleep(random.randint(1,5))
        print "Handler 3 is :%s:" % string
        
    def registerHandlers(self):
        self.on(0, self.handler1)
        self.on(1, self.handler2)
        self.on(2, self.handler3)
        
    

    
