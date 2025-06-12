.SUFFIXES:

.PHONY: all
all: site

site: mkdocs.yml $(shell find docs -type f)
	mkdocs build && cp docs/img/*.cast site/demo-anaconda/

.PHONY: clean
clean:
	-rm -rf site __pycache__
