PYTHON ?= python3
VENV ?= .venv
BIN := $(VENV)/bin

.PHONY: setup test report

setup:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/python -m pip install --upgrade pip
	$(BIN)/python -m pip install -e . pytest

test:
	$(BIN)/python -m pytest

report:
	$(BIN)/fabricscope report --input data/sample_fabric_events.csv
