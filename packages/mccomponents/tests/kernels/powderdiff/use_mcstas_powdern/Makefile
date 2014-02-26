# -*- Makefile -*-

.PHONY: plot-ie clean

sim: out/iqe.h5

clean:
	rm -rf out *.dat *.h5 *~ 

plot-ie: ie.h5
	PlotHist.py ie.h5

plot-iq: iq.h5
	PlotHist.py iq.h5

total-scattered-int: iq.h5
	python -c "import histogram.hdf as hh; iq=hh.load('iq.h5'); print iq[(0.5,None)].I.sum()"



out/iqe.h5: ssd ssd.pml 
	./ssd --ncount=1e7

iqe.h5: out/iqe.h5
	cp out/iqe.h5 iqe.h5

ie.h5: iqe.h5
	python -c "import histogram.hdf as hh; iqe=hh.load('iqe.h5'); ie=iqe.sum('Q'); hh.dump(ie, 'ie.h5')"

iq.h5: iqe.h5
	python -c "import histogram.hdf as hh; iqe=hh.load('iqe.h5'); iq=iqe[(0.5,None), ()].sum('energy'); hh.dump(iq, 'iq.h5')"

