[![Build Status](https://github.com/mcvine/mcvine/workflows/CI/badge.svg)](https://github.com/mcvine/mcvine/actions?query=workflow%3ACI)

# MCViNE: Monte Carlo VIrtual Neutron Experiment

* Homepage: http://mcvine.github.io
* Examples: http://mcvine.github.io/examples.html
* Publications: http://mcvine.github.io/publications.html
* Training: https://github.com/mcvine/training
* Development: https://github.com/mcvine/devel
* Build mcvine-core (current repository) and subpackages from source: [build-dev](builders/dev/README.md)

# Installing the MCViNe ecosystem

The MCVine packages are released through conda: [Anaconda Mcvine Registry](https://anaconda.org/mcvine/).
The mcvine-core is available as a conda package:

```bash

conda install mcvine-core

```
Release candidate versions are provided through the rc channel (mcvine/label/rc), while full production releases through tha main channel (mcvine).

*It is strongly recommended to install the full MCVine ecosystem, instead of selective subpackages, due to internal package dependencies.*

```bash
conda install mcvine

```

To see the full list of dependencies, subpackages and the latest versions, please refer to: [mcvine conda-recipes](https://github.com/mcvine/conda-recipes)

# Starting MCViNe for the first time - Prerequisites

MCVine depedends on Mantid and it requires the Mantid workbench to be executed at least once on the user's directory or to call the following Mantid function from a script

```bash

DownloadInstrument

```

The [DownloadInstrument](https://docs.mantidproject.org/nightly/algorithms/DownloadInstrument-v1.html) algorithm downloads the contents of the instruments/ directory and Facilites.xml in the local directory.

# Using python logging in mcvine-core

mcvine-core uses python logging to log messages. Logging is configured in packages/mcvine/etc/mcvine.conf. The logging level is set by the level tag. By default, logging is set to debug level, which will show all logging messages. The logging levels from lowest to highest are the following:
* DEBUG 
* INFO
* WARNING
* ERROR
* CRITICAL

The higher the log level, the higher the suppression. If logging level is set to WARNING, only WARNING and above messages are logged.
To add logging to a file, add the following code:
```
import logging
logger = logging.getLogger("MCVine")
logger.<level>("<log message>")
```
where level is any of the levels mentioned above but in lower case.

The filename tag in mcvine.conf determines where the logging is saved to; in this case, it is mcvine.log.
For more info on how to use logging, see the [python documentation](https://docs.python.org/3/library/logging.html)
