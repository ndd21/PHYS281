default: mkdocs.yml
	mkdocs build
	cp docs/img/minicondainstallation.cast site/demo-anaconda/
	cp docs/img/condacreate.cast site/demo-anaconda/
