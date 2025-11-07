SHELL=/bin/bash
PUBLIC_HTML="$$HOME"/public_html
INSTALLDIR=$(PUBLIC_HTML)/PHYS281

.SUFFIXES:

.PHONY: all
all: site

site: mkdocs.yml $(shell find docs -type f)
	mkdocs build && cp docs/img/*.cast site/demo-anaconda/

.PHONY: install
install: all
	[[ -d site ]] && mountpoint -q $(PUBLIC_HTML)\
	  && mkdir -p $(INSTALLDIR)\
	  && rsync -aHv --delete site/ $(INSTALLDIR)\
	  && chmod -R a+rX $(INSTALLDIR)

.PHONY: clean
clean:
	-rm -rf site __pycache__

.PHONY: uninstall
uninstall: clean
	-rm -rf $(INSTALLDIR)

.PHONY: help
help:
	@echo "Targets: all, install, clean, uninstall and help."
