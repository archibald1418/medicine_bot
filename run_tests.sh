#!/bin/bash

pytest --show-capture=no \
    --color=yes  \
    --log-file=app/log/tests.log \
    --log-cli-level=INFO \
    -r E
# show errors to stdout with color, keep full trace of python errors, use live-logging and write logs to path
