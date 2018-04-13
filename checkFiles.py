#!/usr/bin/env python
import os, glob, sys
from commands import getoutput
import re
import ROOT

pattern = "Wprime"
if len(sys.argv) > 1: pattern = sys.argv[1]
		
filelist = glob.glob('*/*.root')
# filelist = glob.glob('/scratch/thaarres/SUBSTRUCTURE/LOLAoutput/*.root')

for file in filelist:
	f = ROOT.TFile(file, "read")
	if not f.GetListOfKeys().Contains("tree"):
  # if not f.GetListOfKeys().Contains("tree"):
	    print "FILE is ghost ... ", file
	    cmd = 'rm %s' %file
	    print 'Going to execute: ' , cmd
#	    print "Remember to resubmit, job number %s" %(file.split("_")[2])
	    os.system(cmd)
	else:
#		print "FILE IS GOOD, KEEPING IT"	
		continue

