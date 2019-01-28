# -*- Python -*-
# Jiao Lin <jiao.lin@gmail.com>


# Refs. Vogel thesis

import numpy as np


def phi1(theta1):
    def sum_series(theta1):
        n = np.arange(1., 35.)
        series = 1./np.exp(n/theta1)/n/n
        return np.sum(series)
    return 1./2+2*(theta1*np.log(1-np.exp(-1/theta1))+theta1**2*(np.pi**2/6 - sum_series(theta1)))


def phi3(theta1):
    def sum_series(theta1):
        n = np.arange(1., 35.)
        tmp = theta1/n
        series = (1./2+tmp+tmp*tmp)/np.exp(n/theta1)/n/n
        return np.sum(series)
    return 1./4+2*(theta1*np.log(1-np.exp(-1/theta1))+6*theta1**2*(np.pi**4/90*theta1**2 - sum_series(theta1)))


# End of file
