.PHONY: all clean cleanall

all: contenedores

scheduling: contenedores.tex
	pdflatex contenedores.tex #> /dev/null
	pdflatex contenedores.tex #> /dev/null

	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

cleanall:
	rm -f contenedores.pdf
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb
