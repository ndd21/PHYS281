L1:=Lecture_01
# Compilation of Lecture_01_plain.html seems to be broken.  Is it needed?
OUTPUTS:=$(L1).pdf #$(L1)_plain.html

.SUFFIXES:

.PHONY: all
all: $(OUTPUTS)

$(L1).tex: $(L1).md phys101-slides.latex
	pandoc --pdf-engine xelatex -t beamer --template phys101-slides.latex\
	 -V scuro=true -o $@ $<

$(L1).pdf: $(L1).tex
	latexmk -xelatex -pdf -dvi- -ps- $<

$(L1)_plain.html: $(L1).md default.html default.yaml
	pandoc --template=default.html --self-contained --listings\
	 --filter pandoc-citeproc --mathjax --variable papersize=a4paper\
	 -s default.yaml -o $@ $<

.PHONY: clean
clean: tidy
	rm -f $(OUTPUTS)

.PHONY: tidy
tidy:
	rm -f $(L1).aux $(L1).fdb_latexmk $(L1).log $(L1).fls $(L1).nav\
	 $(L1).out $(L1).snm $(L1).tex $(L1).toc $(L1).vrb
