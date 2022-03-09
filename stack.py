"""
Jack Farrell, 2020

Command line to "stack" two-column pdfs - that is, make one long column.  This is for easier viewing on mobile devices.
"""
# imports
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy
import sys

# pass command line values
inName = str(sys.argv[1])
outName = str(sys.argv[2])
percent = float(sys.argv[3]) / 100

# load the pdf and prepare a writer
infile = PdfFileReader(inName)
writer = PdfFileWriter()

# iterate through all pages
for n in range(infile.getNumPages()):

    page = infile.getPage(n)

    # prepare what will become the new pages corresponding to the old left and right columns
    left = copy.deepcopy(page)
    right = copy.deepcopy(page)
    
    # figure out where to crop, and do it!
    current_coords = left.mediaBox.upperRight
    new_coords = (current_coords[0] * percent, current_coords[1])
    left.mediaBox.upperRight = new_coords
    leftwidth = left.mediaBox.upperRight[0] - left.mediaBox.upperLeft[0]
    right.mediaBox.upperLeft = (leftwidth, new_coords[1])
    right.mediaBox.upperRight = (2 * leftwidth, new_coords[1])
    
    # add the pages to our new document
    writer.addPage(left)
    writer.addPage(right)
    
# save the new document
with open(outName, 'wb') as f:
    writer.write(f)
    