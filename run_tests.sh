#!/bin/bash

pytest --show-capture=stdout \
    --color=yes  \
    --full-trace \
    --log-cli-level=INFO \
    --log-file=app/log/tests.log
# show errors to stdout with color, keep full trace of python errors, use live-logging and write logs to path