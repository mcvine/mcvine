# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Alex Dementsov
#                      California Institute of Technology
#                        (C) 2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
HDF5Converter   - takes directory with .h5 files in HDF5 format and converts
                  them to .png files
"""

# Usage string
USAGE_MESSAGE   = """
NAME:
    HDF5Converter - converter for files in HDF5 format

SYNOPSIS:
    python hdf5converter.py (--input-dir|-id)=input_directory (--output-dir|-od)=output_directory

DESCIRPTION:
    HDF5Converter - takes directory with .h5 files in HDF5 format and converts
                    them to .png files

EXAMPLE:
    python hdf5converter.py -id=in -od=out
"""

INPUT_DIR       = ["--input-dir", "-id"]
OUTPUT_DIR      = ["--output-dir", "-od"]
ARGS            = INPUT_DIR + OUTPUT_DIR


import sys
import os
import h5py
import pylab
import numpy

class HDF5Converter:

    def __init__(self, input_dir="", output_dir=""):
        self._h5files   = []    # List of hdf5 files in input directory
        self._pngfiles  = []    # List of png files that will be generated
        
        if input_dir == "" or output_dir == "":
            if len(sys.argv) != 3:
                raise Exception, USAGE_MESSAGE
                return
           
            for arg in sys.argv:
                parts   = arg.split("=")
                key     = parts[0]
                if len(parts) != 2:
                    continue

                if not key in ARGS:
                    raise Exception, USAGE_MESSAGE
                    return

                if key in INPUT_DIR:
                    self._input_dir = parts[1]
                elif key in OUTPUT_DIR:
                    self._output_dir = parts[1]

        else:
            self._input_dir     = input_dir
            self._output_dir    = output_dir

        if not os.path.exists(self._input_dir) or not os.path.exists(self._output_dir):
            raise Exception, "Error: Input directory '%s' or output directory '%s' don't exist" % \
                    (self._input_dir, self._output_dir)

        # Populates list of .h5 and .png files
        inpfiles    = os.listdir(self._input_dir)
        names       = []    # Keeps base names
        for inp in inpfiles:
            if inp.endswith(".h5"):
                parts    = inp.split(".h5")
                names.append(parts[0])
                self._h5files.append(os.path.join(self._input_dir, inp))

        for n in names:
            self._pngfiles.append(os.path.join(self._output_dir, n + ".png"))

        assert len(self._h5files) == len(self._pngfiles)


    def toPNG(self):
        "Generates .png files from .h5 files"
        for i in range(len(self._h5files)):
            f       = h5py.File(self._h5files[i])
            gr_name = f.values()[0].name
            grbin_name  = f.values()[0].values()[2].values()[0].name

            gr      = f[gr_name]     # group. e.g. "/iw"
            gr_bin  = f[grbin_name]  # "/iw/grid/w"
            yset    = gr["data"]     # set
            xset    = gr_bin["bin boundaries"]
            ylist   = [repr(item) for item in yset]
            xlist   = [repr(item) for item in xset]
            xlist.pop()     # Last element should be removed
            y   = numpy.array(ylist)
            x   = numpy.array(xlist)

            pylab.plot(x,y)
            pylab.savefig(self._pngfiles[i])
            pylab.clf()
            print "... " + self._pngfiles[i]


if __name__ == "__main__":
    conv    = HDF5Converter()
    conv.toPNG()