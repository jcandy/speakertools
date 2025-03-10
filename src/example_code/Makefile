all:
	python plot_discrete.py
	python print_c4.py > print_c4.txt
	python print_ca.py > print_ca.txt
	python print_qt.py > print_qt.txt
	python print_quasi.py > print_quasi.txt
	mv *png ../images/alignment
	mv *txt ../images/alignment
	tar -zcf libalignment.tgz print* libalignment.py
	zip libalignment print* libalignment.py

clean:
	rm *-amp.png *-delay.png *-poles.png *txt
