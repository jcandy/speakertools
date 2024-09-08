all:
	cd src ; make html

sync:
	rsync -a --exclude-from='exclude.txt' src/_build/html/ doc/

clean:
	cd src ; make clean

