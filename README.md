# Speakertools

## About the project

Speakertools is a tool and documentation repository for [Speakerbench](https://speakerbench.com) developers and users. Python tools are located in speakertools/bin and Sphinx documentation sources are in speakertools/src. 

## Instructions

To *edit* rst source files for documentation (on laptop):

```
$ cd src
$ vi index.rst
```

To *build* webpages (on laptop):

```
$ make  # this will generate html files in src/_build/html
```

To *build* and *publish* webpages (on server):

```
$ make
$ make sync   # to copy html files to doc directory
$ make clean  # to remove contents of src/_build
```

NOTES: Currently,

- updating of _static inhibited
- timestamping of files shut off in conf.py
