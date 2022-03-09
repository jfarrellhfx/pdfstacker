@ECHO OFF

SET infile=%1
SET outfile=%2
SET percent=%3

SHIFT
SHIFT
SHIFT

call conda activate base
call python stack.py %infile% %outfile% %percent%
