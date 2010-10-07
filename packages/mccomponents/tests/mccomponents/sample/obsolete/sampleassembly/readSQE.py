
from mccomponents.sample.idf  import readSQE
sqe = readSQE( 'SQE-examples' )
import histogram.hdf as hh
hh.dump( sqe, 'sqe.h5', '/', 'c' )
