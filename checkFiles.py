import os, glob, sys, shlex
import subprocess
from ROOT import TFile, Double

import optparse

parser = optparse.OptionParser()

parser.add_option('-m', '--make', action="store_true", default=False, dest='make')
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



for directory in os.listdir("./"):

#    if directory.find('W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER')==-1: continue

    filelist = glob.glob(directory + '/*_' + options.channel + '.root')


    if os.path.isfile(directory + '/' + options.channel + '.root'):
        print bcolors.BOLD + bcolors.OKBLUE + '[OK] ' + directory + bcolors.ENDC        


    if not filelist: continue
    
    
    flag = False
    files = []
    
    for file2check in filelist:
        
        f = TFile(file2check, "read")
        
        if not f.GetListOfKeys().Contains("tree"):
            files.append(file2check)

            flag = True


    if flag:
        print bcolors.FAIL + "[NG]" + directory + bcolors.ENDC
        print '\t', len(files), ' out of ', len(filelist), ' files are corrupted ... skip this sample (consider to resubmit the job)'
        continue

    else:
        print bcolors.BOLD + bcolors.OKGREEN + '[OK] ' + directory + ' ... can be hadded ' + bcolors.ENDC
        
    

    if options.make:

        target = directory + '/' + options.channel + '.root'

        if not os.path.isfile(target):

            haddcmd = 'hadd -f ' + directory + '/' + options.channel + '.root ' + directory + '/*_' + options.channel + '.root'
            os.system(haddcmd)

            f_hadd = TFile(directory + '/' + options.channel + '.root')
            total_processed = Double(f_hadd.Get('h_cutflow').GetBinContent(1))
            
#            print 'Check number of events = ', total_processed
            
            dasname = directory.replace('__', '/')
            instance = 'prod/global'
            
            if dasname.find('USER')!=-1:
                instance = 'prod/phys03'

            dascmd = 'das_client --limit=0 --query=\"summary dataset=/' + dasname + ' instance=' + instance + '\"'
            args = shlex.split(dascmd)
            output,error = subprocess.Popen(args, stdout = subprocess.PIPE, stderr= subprocess.PIPE).communicate()
            total_das = Double(output.split('"nevents":')[1].split(',')[0])


            fraction = total_processed/total_das
            
            if fraction > 0.8:
                print bcolors.BOLD + bcolors.OKBLUE + '\t [OK] DAS entries = ' + str(int(total_das)) + ' Tree produced = ' + str(int(total_processed)) + '(frac = {0:.2f}'.format(fraction) + ')' + bcolors.ENDC

                skimcmd = 'python extractTrees.py -c ' + options.channel + ' -f ' + directory + '/' + options.channel + '.root'
                os.system(skimcmd)
                
                # cleaning up ...
                rmcmd = 'rm ' + directory + '/*_' + options.channel + '.root'
                os.system(rmcmd)

            else:
                print bcolors.BOLD + bcolors.FAIL + '\t [OK] DAS entries = ' + str(int(total_das)) + ' Tree produced = ' + str(int(total_processed)) + '(frac = {0.2f}'.format(fraction) + ')' + bcolors.ENDC




