# Convert ARCS instrument file

* The original file is ARCS_10_25_2008.instr.original
* Convert "AT(" to "AT (" and created ARCS_10_25_2008.instr.
* Run `$ mcvine mcstas convertinstrument ARCS_10_25_2008.instr` and generated ARCS_10_25_2008_mcvine.py.
* Clean up the script
  - Look for "unknown" in the generated python script. They are unsupported components. For this case, we can just
    remove them.
  - Look for strings in "position"s and remove the quotes
  - Add "INITIALIZE" code and convert to python
  - Check the script by `python ARCS_10_25_2008_mcvine_revised.py` and make corrections
* Test run: `./testrun.py`
* Check results: `plothist out.testrun/I_E.h5`
