sources := sources.csv

.PHONY: all
all: $(sources)

.PHONY: clean
clean:
	-rm -rf *.pdf
