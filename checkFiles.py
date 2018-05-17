import os, glob, sys
from ROOT import TFile

import optparse

parser = optparse.OptionParser()

parser.add_option('-f', '--force', action="store_true", default=False, dest='force')
parser.add_option('-r', '--remove', action="store_true", default=False, dest='rmghost')
parser.add_option('-s', '--skim', action="store_true", default=False, dest='skim')
parser.add_option('-c', '--channel', action="store", type="string", default="tautau", dest='channel')
parser.add_option('-t', '--resubmit', action="store_true", default=False, dest='resubmit')

(options, args) = parser.parse_args() 


def returnDAS(filename):
    cmd = 'hadd -f ' + dir + '/' + options.channel + '.root ' + dir + '/*.root'
    os.system(cmd)



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# read samples lists
samplelist = []

for line in open('samples.cfg', 'r'):
    if line.find('#')!=-1: continue
    samplelist.append(line.rstrip())


#print samplelist    

#sys.exit(1)

for dir in os.listdir("./"):

    filelist = glob.glob(dir + '/*.root')

    if filelist:
        pass
    else:
        continue

    print bcolors.BOLD + '[Processing] :' + dir + bcolors.ENDC

    print '\t Check files ...', 

    flag = False
    
    for file2check in filelist:

        f = TFile(file2check, "read")

        if not f.GetListOfKeys().Contains("tree"):
            print bcolors.FAIL + "\t Warning: file is ghost ... ", file2check + bcolors.ENDC

            flag = True


            if flag and options.rmghost:
                print bcolors.FAIL + "\t rm: ", file2check + bcolors.ENDC
                cmd = 'rm %s' %file2check
                os.system(cmd)

            if options.resubmit:
                pass


    if flag:
        continue

    print bcolors.HEADER + 'OK' + bcolors.ENDC

    if options.resubmit:
        continue


    if (not os.path.isfile(dir + '/' + options.channel + '.root')) or options.force:    
        cmd = 'hadd -f ' + dir + '/' + options.channel + '.root ' + dir + '/*.root'
        os.system(cmd)

#        f_hadd = TFile(dir + '/' + options.channel + '.root')
#        tree = f_had.Get('tree')
#        total_processed = tree.GetEntries()

#        Tau_ytakahas-NanoTest_20180507_B-55055ff3316a022bb149a249662ed4c4/
#        Tau/ytakahas-NanoTest_20180507_B-55055ff3316a022bb149a249662ed4c4/USER
#
#        cmd = 'hadd -f ' + dir + '/' + options.channel + '.root ' + dir + '/*.root'
#        os.system(cmd)
        

        


    if options.skim:
        cmd2 = 'python extractTrees.py -c ' + options.channel + ' -f ' + dir + '/' + options.channel + '.root'
        os.system(cmd2)




