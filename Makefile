.SUFFIXES:

.PHONY: all
all: site/index.html

site/index.html: mkdocs.yml $(shell find docs -type f)
	mkdocs build
	cp docs/img/*.cast site/demo-anaconda/

.PHONY: clean
clean:
	rm -rf site __pycache__ docs/javascripts/glossary.js
