lecture01: Lecture_01.md
	# create LaTeX file
	pandoc --pdf-engine xelatex -t beamer --template phys101-slides.latex -V scuro=true -o Lecture_01.tex Lecture_01.md
	# compile tex
	latexmk -f -xelatex -pdf -dvi- -ps- -silent -outdir=. Lecture_01.tex
	# clean up files
	find -name 'Lecture_01*' -not -name "*.md" -not -name "*.pdf" -not -name "*.html" -exec rm {} \;
	# create html
	pandoc --template=default.html --self-contained --listings --filter pandoc-citeproc --mathjax --variable papersize=a4paper -s default.yaml Lecture_01.md > Lecture_01_plain.html