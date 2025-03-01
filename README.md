# Speakertools

## About the project

<p>Speakertools is a tool section for
<a href="https://speakerbench.com">Speakerbench</a>, not only targeting
users, but equally as much the programmers. One such tool is the
documentation, which helps us (the programmers) to remember what we
made, how, and why.</p>

## Instructions

To *edit* webpages:

- edit files in the src directory.

To *build* webpages:

$ make (this will generate html files)

To *publish* webpages:

$ make sync  (to copy html files to doc directory)
$ make clean (to remove temporary files
$ cd .. (change to doc directory)
$ git add . ; git commit -m <message> (add/commit changes)
$ git push

NOTES: Currently,

- updating of _static inhibited
- timestamping of files shut off in conf.py
