@ECHO OFF
SET scriptdir=%~dp0

SET infile=%1
SET outfile=%2
SET percent=%3

SHIFT
SHIFT
SHIFT

call conda activate base
call python "%scriptdir%stack.py" %infile% %outfile% %percent%
