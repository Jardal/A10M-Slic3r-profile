import sys
import shutil
import os

# Repetier-Host sends only the file name, stand alone slic3r sends path and file name
sourcename = sys.argv[1]
if sourcename[1] != ':':
	sourcename = 'C:\\3DPrintingFiles\\' + sourcename	# source file passed from Slic3r

tmpname = 'C:\\3DPrintingFiles\\tmpfile.gcode'	# temp file name
currlayer = 1	# set current layer to 1
maxlayer = 0	# get ready to count the layer changes

with open(sourcename,'rt') as fin:
#	fout.write('; File open\n')
	while 1:	# loop to count the M117 layers
		ln = fin.readline()
		if (ln == ''):	# check for end of file
			break
		if ln[0] == ';':	# don't count M117 in comments
			continue
		if ln[:4] == "M117":	# found a M117 outside of comment
			maxlayer += 1
	#fin.seek(0)	# start at the begining of input file again
	#ln = fin.readline()
	#fout.wtite(ln)
fin.close() 

with open(sourcename,'rt') as fin, open(tmpname,'w') as fout:
#	fout.write('; File open\n')
	while 1:	# loop to replace M117 with "M117 Layer x of x"
#		fpos = fin.tell()
		ln = fin.readline()
		if (ln == ''):	# check for end of file
			break
		if ln[0] == ';':	# skip comment lines
			fout.write(ln)
			continue
		if (currlayer > maxlayer):
			continue
		if ln[:4] == 'M117':	# replace M117 with "M117 Layer n of x"
			if (currlayer < maxlayer):
				fout.write('M117 Layer ' + str(currlayer) + ' of ' + str(maxlayer-1) + '\n')
#			        fout.write('; ' + str(fpos) + '\n')
				currlayer += 1
			else:
				fout.write('M117 Print Done\n')
		else:
			fout.write(ln)

fin.close()	# close the files
fout.close()

shutil.move(tmpname,sourcename)	# replace orginal file with modified file
#os.remove(sourcename + '~')
