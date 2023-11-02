#!/bin/bash

pytest --show-capture=log --log-file=app/log/tests.log --full-trace --log-level=INFO
