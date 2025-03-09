all:
	cd src ; make html

sync:
#	rsync -a --exclude-from='exclude.txt' src/_build/html/ doc/
	rsync -a src/_build/html/ doc/

clean:
	cd src ; make clean

distclean:
	make clean
	rm -rf doc/*
