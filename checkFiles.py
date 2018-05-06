#!/usr/bin/env python
import os, glob, sys
from commands import getoutput
import re
import ROOT

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


pattern = "Wprime"
if len(sys.argv) > 1: pattern = sys.argv[1]
		
filelist = glob.glob('*/*.root')
# filelist = glob.glob('/scratch/thaarres/SUBSTRUCTURE/LOLAoutput/*.root')

for file in filelist:
	f = ROOT.TFile(file, "read")
	if not f.GetListOfKeys().Contains("tree"):
  # if not f.GetListOfKeys().Contains("tree"):
	    print bcolors.FAIL + "Warning: file is ghost ... ", file + bcolors.ENDC
	    cmd = 'rm %s' %file
#	    print 'Going to execute: ' , cmd
#	    print "Remember to resubmit, job number %s" %(file.split("_")[2])
#	    os.system(cmd)
	else:
#		print "FILE IS GOOD, KEEPING IT"	
#		print bcolors.OKGREEN + "OK: File is good", file + bcolors.ENDC
		continue

