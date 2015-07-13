import time
import os
import sys
import random
import gevent
from gevent import select
from gevent.queue import Queue
from gevent import lock
from gevent.lock import DummySemaphore
cnt =0
start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr(no):
    # Busy waits for a second, but we don't want to stick around...
    print('GR1 Started Polling: %s' % tic())
    global cnt
    cnt += 1
    gevent.sleep(random.randint(2,12))
    print "GR1     " + str(no)
    #select.select([], [], [], 2)
    #time.sleep(3)
    #sched_yield()
    #yield 1
    
    print('GR1 Ended Polling: %s' % tic())

def gr2(no):
   
    # Busy waits for a second, but we don't want to stick around...
    print('GR2 Started Polling: %s' % tic())
    global cnt
    cnt += 1
    print "GR2     " + str(cnt)
    #select.select([], [], [], 2)
    #gevent.sleep(15)
    print('GR2 Ended Polling: %s' % tic())

def gr3():
    print("GR3  Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)

queue = Queue()    

#queue.put_nowait(gevent.spawn(gr1))

#queue.put_nowait(gevent.spawn(gr2))

#queue.put_nowait(gevent.spawn(gr3))

#job = queue.get()
#job.join()

threads = [gevent.spawn(gr,i)for i in xrange(200)]
gevent.joinall(threads)

#gevent.joinall([
#     gevent.spawn(gr1),
#     gevent.spawn(gr2),
#     gevent.spawn(gr3),
#])




