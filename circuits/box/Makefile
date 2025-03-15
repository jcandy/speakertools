all:
	pdflatex box_q
	pdflatex port_q
	pdflatex port_classic
	pdflatex box_classic

crop:
	pdfcrop -bbox "0 660 235 800" box_q.pdf a.pdf ; mv a.pdf box_q.pdf
	pdftoppm -r 300 -png box_q.pdf > box_q.png

	pdfcrop -bbox "0 676 235 816" box_classic.pdf a.pdf ; mv a.pdf box_classic.pdf
	pdftoppm -r 300 -png box_classic.pdf > box_classic.png

	pdfcrop -bbox "0 660 235 800" port_q.pdf a.pdf ; mv a.pdf port_q.pdf
	pdftoppm -r 300 -png port_q.pdf > port_q.png

	pdfcrop -bbox "0 660 235 800" port_classic.pdf a.pdf ; mv a.pdf port_classic.pdf
	pdftoppm -r 300 -png port_classic.pdf > port_classic.png

clean:
	rm -f *log *aux *pdf *png *~
