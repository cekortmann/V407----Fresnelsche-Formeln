all: build/v407.pdf

build/v407.pdf: v407.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v407.tex
	lualatex  --output-directory=build v407.tex
	biber build/v407.bcf
	lualatex  --output-directory=build v407.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
