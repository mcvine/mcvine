# -*- Python -*-
# Jiao Lin <linjiao@caltech.edu>


def root():
    from .deployment_info import mcvine_resources
    if not mcvine_resources:
        alert_missing_resources()
    return mcvine_resources


def alert_missing_resources():
    msg = """Missing information about MCViNE resources. 

If it is available in your system, please set environment
variable MCVINE_RESOURCES to its root path.

If it is not available, please obtain it by

 $ git clone https://github.com/heetuu/mcvine-resources.git

, and then set MCVINE_RESOURCES to the path of the new
directory.

"""
    raise IOError(msg)


import os

def instrument(name):
    r = root()
    return os.path.join(r, "instruments", name)


# End of file 

