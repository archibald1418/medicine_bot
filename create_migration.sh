#!/bin/bash


read -p "Migration name?: " name

alembic revision --autogenerate -m $name

