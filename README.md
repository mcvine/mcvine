[![Build Status](https://github.com/mcvine/mcvine/workflows/CI/badge.svg)](https://github.com/mcvine/mcvine/actions?query=workflow%3ACI)

# MCViNE: Monte Carlo VIrtual Neutron Experiment

* Homepage: http://mcvine.github.io
* Examples: http://mcvine.github.io/examples.html
* Publications: http://mcvine.github.io/publications.html
* Training: https://github.com/mcvine/training
* Development: https://github.com/mcvine/devel
* Build mcvine-core and subpackages from source: [build-dev](builders/dev/README.md)

# Using python logging

MCVine uses python logging to log messages. Logging is configured in packages/mcvine/etc/mcvine.conf. The logging level is set by the level tag. By default, logging is set to debug level, which will show all logging messages. The logging levels from lowest to highest are the following:
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
