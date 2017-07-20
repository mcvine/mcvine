SRC=`python -c "from mcvine.resources import sample; import os; print os.path.dirname(sample('Al', temperature='300K'))"`
ln -s $SRC/phonons Al-phonons
