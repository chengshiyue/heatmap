#! /usr/bin/env python3
# -*- coding:utf-8-*-
import sys
import os
import re
import tkinter.filedialog
import csv


__author__='Liu Tao'
__mail__= 'taoliu@annoroad.com'

pat1=re.compile('^\s+$')

def parsefile(infile):
	record={}
	tag = 0
	sample = ''
	samples = []
	for line in csv.reader(infile):
		#print(line)
		#if line.startswith('#') or re.search(pat1,line):continue
		tmp = line
		if tmp[0] == 'Sample Name':
			sample = tmp[1]
			samples.append(sample)
			if not sample in record:
				record[sample]=[]
		elif tmp[0]=='Size [bp]':
			tag = 1 
			continue
		if tag >0:
			tag += 1
		if tag == 3 :
			record[sample] += tmp[0:3]
			tag = 0
	#	if not sample in samples:
	#		print(sample)
	#		samples.append(sample)
	return(record,samples)

def main():
	#parser=argparse.ArgumentParser(description=__doc__,
	#		formatter_class=argparse.RawDescriptionHelpFormatter,
	#		epilog='author:\t{0}\nmail:\t{1}'.format(__author__,__mail__))
	#parser.add_argument('-i','--input',help='input file',dest='input',type=argparse.FileType('r'),required=True)
	#parser.add_argument('-o','--output',help='output file',dest='output',type=argparse.FileType('w'),required=True)
	#args=parser.parse_args()

	infile = tkinter.filedialog.askopenfilename(filetypes=[])

	prefix = os.path.splitext(infile)[0]
	outfile = prefix+'.txt'
	with open(infile,encoding='gbk') as f_file:
		result,samples =  parsefile(f_file)
	print(samples)
	with open(outfile,'w') as output:
		for i in samples:
			output.write('{0}\t{1}\n'.format(i,'\t'.join(result[i])))

if __name__=='__main__':
	main()
