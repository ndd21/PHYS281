default: mkdocs.yml
	mkdocs build
	cp docs/img/minicondainstallation.cast site/
	cp docs/img/condacreate.cast site/
