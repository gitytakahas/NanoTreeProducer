import os, glob, sys, shlex
import subprocess
from ROOT import TFile, Double

import optparse

parser = optparse.OptionParser()

parser.add_option('-c', '--channel', action="store", type="string", default="tautau", dest='channel')

(options, args) = parser.parse_args() 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



gtotal_processed = 0.
gtotal_das = 0.

for directory in os.listdir("./"):

#    if directory.find('W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER')==-1: continue

    target = directory + '/' + options.channel + '.root'

    if os.path.isfile(target):
        print bcolors.BOLD + directory + bcolors.ENDC        
    else:
#        print bcolors.BOLD + bcolors.FAIL + '[NG] : ' + directory + '/' + options.channel + '.root does not exist ...' + bcolors.ENDC
        continue

    if directory in ['ZTT', 'SingleMuon', 'SingleElectron', 'Tau']: 
        continue

    dataflag = False
    dataflag = directory.find('SingleMuon')!=-1 or directory.find('SingleElectron')!=-1 or directory.find('Tau')!=-1 
    
    f_hadd = TFile(target)
    total_processed = Double(f_hadd.Get('h_cutflow').GetBinContent(1))
            
    if dataflag:
        gtotal_processed += total_processed

    

    if directory.find('LQ')==-1:

        dasname = directory.replace('__', '/')
        instance = 'prod/global'
    
        if dasname.find('USER')!=-1:
            instance = 'prod/phys03'
            
        dascmd = 'das_client --limit=0 --query=\"summary dataset=/' + dasname + ' instance=' + instance + '\"'
        args = shlex.split(dascmd)
        output,error = subprocess.Popen(args, stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()

        total_das = Double(output.split('"nevents":')[1].split(',')[0])
        
        if dataflag:
            gtotal_das += total_das

        
    
        fraction = total_processed/total_das
    
        if fraction > 0.8:
            print bcolors.BOLD + bcolors.OKBLUE + '\t [OK] DAS entries = ' + str(int(total_das)) + ' Tree produced = ' + str(int(total_processed)) + ' (frac = {0:.2f}'.format(fraction) + ')' + bcolors.ENDC
        else:
            print bcolors.BOLD + bcolors.FAIL + '\t [NG] DAS entries = ' + str(int(total_das)) + ' Tree produced = ' + str(int(total_processed)) + ' (frac = {0:.2f}'.format(fraction) + ')' + bcolors.ENDC

    else:
        total_processed = Double(f_hadd.Get('h_cutflow').GetBinContent(4))
        tree = f_hadd.Get('tree')
        total_tree = tree.GetEntries()
        
        fraction = total_tree/total_processed

        if fraction == 1:
            print bcolors.BOLD + bcolors.OKBLUE + '\t [OK] Tree produced = ' + str(int(total_processed)) + ' (frac = {0:.2f}'.format(fraction) + ')' + bcolors.ENDC
        else:
            print bcolors.BOLD + bcolors.FAIL + '\t [NG] Tree produced = ' + str(int(total_processed)) + ' (frac = {0:.2f}'.format(fraction) + ')' + bcolors.ENDC
        
        

print 'data (DAS, processed) = ', gtotal_das, '/',  gtotal_processed, '=>', '{0:.3f}'.format(Double(gtotal_processed/gtotal_das))



