all:	
	pdflatex elec_total 
	pdflatex basic_elec
	pdflatex basic_mech

crop:	
	pdfcrop elec_total.pdf a.pdf ; mv a.pdf elec_total.pdf
	pdfcrop basic_elec.pdf a.pdf ; mv a.pdf basic_elec.pdf
	pdfcrop basic_mech.pdf a.pdf ; mv a.pdf basic_mech.pdf

clean:
	rm -f *log *aux *pdf *~
