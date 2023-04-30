all: build/v407.pdf

build/v407.pdf: build/plot90Pol.pdf build/plot0Pol.pdf v407.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v407.tex
	lualatex  --output-directory=build v407.tex
	biber build/v407.bcf
	lualatex  --output-directory=build v407.tex

build/plot0Pol.pdf: PlotPol0.py Polarisation0.txt | build
	python PlotPol0.py

build/plot90Pol.pdf: PlotPol90.py Polarisation90.txt | build
	python PlotPol90.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
