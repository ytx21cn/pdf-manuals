PYTHON := python3

download := download.py
clean := clean.py

sources := sources.csv

.PHONY: all
all: $(sources)
	$(PYTHON) $(download) $<

.PHONY: clean
clean:
	$(PYTHON) $(clean)
