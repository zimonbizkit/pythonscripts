#!/usr/bin/python
import Queue
import sys
from time import sleep
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New job:', description
        return
        
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)



q = Queue.PriorityQueue()


_in = ""
while _in != 'end':
    print "Please input system job name (or command):"
    _in = raw_input()
    print "And please input priority:"
    _priority = sys.stdin.readline()
    q.put(Job(_priority,_in))

while not q.empty():
    next_job = q.get()
    print 'Processing job:', next_job.description
    sleep(0.5)                                                                  
