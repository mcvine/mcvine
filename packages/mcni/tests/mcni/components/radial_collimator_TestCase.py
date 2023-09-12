#!/usr/bin/env python
#


'''
Test of RadialCollimator
'''

import os
import numpy as np
import journal

debug = journal.debug( "mcni.components.test" )
warning = journal.warning( "mcni.components.test" )


def test():
    DEG2RAD = np.pi/180
    from mcni import neutron_buffer, neutron
    neutrons = neutron_buffer(1)
    from mcni.components.RadialCollimator import RadialCollimator
    coll = RadialCollimator(
        name="collimator",
        radius1=0.308, height1=0.6, radius2=0.462, height2=0.6,
        theta1=-30*DEG2RAD, theta2=150*DEG2RAD,
        dtheta=1.6*DEG2RAD)
    def check(neutron, absorbed):
        neutrons.resize(1, neutron)
        neutrons[0] = neutron
        coll.process(neutrons)
        assert len(neutrons) == (not absorbed)
        return
    check(neutron(r=(0,0,0), v=(-0.9,0,1.732), prob=1), False)
    check(neutron(r=(0,0,0), v=(-1.1,0,1.732), prob=1), True)
    check(neutron(r=(0,0,0), v=(0,-0.3,0.463), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,-0.3,0.461), prob=1), True)
    check(neutron(r=(0,0,0), v=(0,0.3,0.463), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0.3,0.461), prob=1), True)
    check(neutron(r=(0,0,0), v=(0.1,0.3,0.45), prob=1), True)
    check(neutron(r=(0,0,0), v=(0.1,0.3,0.462), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0,0,0), v=(1000,0,0), prob=1), False)
    check(neutron(r=(0,0,0), v=(1000,0,-1000), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0,-1000), prob=1), True)
    check(neutron(r=(0.1,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.001,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0.01,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0.03,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.025,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.015,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.1,0,0), v=(0,10,0), prob=1), True)
    for i in range(10):
        check(neutron(r=(0,0,0), v=(1,0,i), prob=1), False)
    for i in range(1,10):
        check(neutron(r=(0,0,0), v=(i,0,-1), prob=1), False)
        continue
    return

def test_theta_list():
    DEG2RAD = np.pi/180
    from mcni import neutron_buffer, neutron
    neutrons = neutron_buffer(1)
    from mcni.components.RadialCollimator import RadialCollimator
    theta_list = np.arange(-30*DEG2RAD, 150.1*DEG2RAD, 1.6*DEG2RAD)
    coll = RadialCollimator(
        name="collimator",
        radius1=0.308, height1=0.6, radius2=0.462, height2=0.6,
        theta_list=theta_list,
    )
    def check(neutron, absorbed):
        neutrons.resize(1, neutron)
        neutrons[0] = neutron
        coll.process(neutrons)
        assert len(neutrons) == (not absorbed)
        return
    check(neutron(r=(0,0,0), v=(-0.9,0,1.732), prob=1), False)
    check(neutron(r=(0,0,0), v=(-1.1,0,1.732), prob=1), True)
    check(neutron(r=(0,0,0), v=(0,-0.3,0.463), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,-0.3,0.461), prob=1), True)
    check(neutron(r=(0,0,0), v=(0,0.3,0.463), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0.3,0.461), prob=1), True)
    check(neutron(r=(0,0,0), v=(0.1,0.3,0.45), prob=1), True)
    check(neutron(r=(0,0,0), v=(0.1,0.3,0.462), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0,0,0), v=(1000,0,0), prob=1), False)
    check(neutron(r=(0,0,0), v=(1000,0,-1000), prob=1), False)
    check(neutron(r=(0,0,0), v=(0,0,-1000), prob=1), True)
    check(neutron(r=(0.1,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.001,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0.01,0,0), v=(0,0,1000), prob=1), False)
    check(neutron(r=(0.03,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.025,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.015,0,0), v=(0,0,1000), prob=1), True)
    check(neutron(r=(0.1,0,0), v=(0,10,0), prob=1), True)
    for i in range(10):
        check(neutron(r=(0,0,0), v=(1,0,i), prob=1), False)
    for i in range(1,10):
        check(neutron(r=(0,0,0), v=(i,0,-1), prob=1), False)
        continue
    return

def main():
    test()
    test_theta_list()

if __name__ == "__main__": main()

# End of file
