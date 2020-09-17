#!/usr/bin/env python

import os

# 
dir = os.path.dirname(__file__)
header = """.. _kernels:

Kernels
=======

.. note::
   Developers: please also read :ref:`Kernel implementation <kernel-implementation>`.


.. toctree::
   :maxdepth: 2

"""
# list all rst files
rstlist = []
for entry in os.listdir(dir):
    path = os.path.join(dir, entry)
    if not os.path.isfile(path): continue
    if not path.endswith(".rst"): continue
    stream = open(path)
    lines = [stream.readline() for i in range(3)]
    if len(lines) != 3: continue
    # check the signature
    if lines[0][:11] != ".. _kernel_": continue
    # get kernel name
    name = lines[2].strip()
    # get kernel ref
    ref = lines[0][11:].strip().rstrip(':')
    # get filename base without ext
    basename = os.path.splitext(entry)[0]
    rstlist.append(basename)
    continue

rstlist.sort()
content = header + '\n'.join("  %s" % n for n in rstlist) + "\n"
print(content)
