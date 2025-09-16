#!/usr/bin/env bash

ruff check . --fix      # lint + auto-fix
ruff format .           # code formatter (like black)
