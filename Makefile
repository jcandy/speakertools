all:
	cd src ; make html

sync:
	rsync --delete -a src/_build/html/ doc/

clean:
	cd src ; make clean

distclean:
	make clean
	rm -rf doc/*
