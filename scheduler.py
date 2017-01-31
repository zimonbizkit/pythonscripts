#!/usr/bin/python
import Queue
import sys
import os
from time import sleep
class Job(object):
    def __init__(self, priority, description,kind):
        self.priority = priority
        self.description = description
        self.kind= kind
        print 'New job-->',description,kind
        return
        
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)



q = Queue.PriorityQueue()


_in = ""
while _in != 'end':
    _kind=''
    print "Please input type of command (either command or just string):"
    _kind=raw_input()
    while _kind!='string' and _kind!='command':
        print "Damn, you are wrong. Input either string or command!"
        _kind=raw_input()

    print "Please input system job name (or command):"
    _in = raw_input()
    print "And please input priority:"
    _priority = sys.stdin.readline()
    q.put(Job(_priority,_in,_kind))

while not q.empty():
    next_job = q.get()
    if next_job.kind == "string":
        print 'Processing job:PRINTING-->', next_job.description
    elif next_job.kind =="command":
        print 'Processing job:EXECUTING-->',next_job.description
        os.system(next_job.description);
    sleep(0.5)                                                                  
