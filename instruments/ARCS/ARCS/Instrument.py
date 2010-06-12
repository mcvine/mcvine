#!/usr/bin/env python


from mcvine.applications.InstrumentBuilder import build
components = ['moderator', 'core_vessel_insert', 'shutter_guide', 'guide111', 'guide112', 'guide113', 'guide121', 'guide122', 'guide123', 'guide131', 'guide132', 'guide133', 't0chopper', 'guide211', 'guide212', 'guide213', 'guide214', 'guide215', 'fermichopper', 'monitor1', 'guide311', 'guide411', 'guide412', 'guide511', 'monitor']
Instrument = build(components)

