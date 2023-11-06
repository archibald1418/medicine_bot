#!/bin/bash

pytest --show-capture=no \
    --color=yes  \
    --log-file=app/log/tests.log \
    -r E
    # --log-cli-level=INFO \
# show errors to stdout with color, keep full trace of python errors, use live-logging and write logs to path
