.PHONY: clean-pyc clean-build docs clean

GOMOKU_HOME = $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
RUNNER = $(GOMOKU_HOME)/src/run.py

help:
	@echo "clean - remove all build and Python artifacts"
	@echo "install - install the package to the active Python's site-packages"
	@echo "help - print help"
	@echo "run - run rbgomoku game"
	@echo "test - run tests quickly with the default Python"

clean:
	@python setup.py clean --all
	@rm -rf .eggs/ dist/ rbgomoku.egg-info/ src/rbgomoku.egg-info/

install:
	@python setup.py install --record unisntall.txt

test:
	@python setup.py test

run: install
	@python $(RUNNER)
