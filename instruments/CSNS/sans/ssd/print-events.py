#!/usr/bin/env python

from mccomponents.detector import event_utils as evu
f = 'out/events.dat'
print
print "* reading events from %s" % f 
events = evu.readEvents(f)
print
print "* # of events", len(events)
print
print "* events (pixelID, tofID, weight):"
print events
