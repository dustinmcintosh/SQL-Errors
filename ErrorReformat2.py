# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 15:41:55 2015

@author: dustin
"""

string = """canceling statement due to user request
cancelled on user's request
Query execution was interrupted
cancelled due to client request"""

string = string.split('\n')

for i in string:
    print 'elif "'+i.lower()+ '" in errString.lower():'
    print "    return "+'"execution canceled/interupted"'