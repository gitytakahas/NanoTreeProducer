from commands import getoutput
import itertools

import os, glob, sys, shlex
import subprocess
from ROOT import TFile, Double

import optparse

parser = optparse.OptionParser()

parser.add_option('-c', '--channel', action="store", type="string", default="tautau", dest='channel')
parser.add_option('-n', '--njob', action="store", type=int, default=1, dest='njob')
parser.add_option('-m', '--make', action="store_true", default=False, dest='make')

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


def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))

def getFileListDAS(dataset):

    instance = 'prod/global'
    if dataset.find('USER')!=-1:
        instance = 'prod/phys03'
    
    cmd='das_client --limit=0 --query="file dataset=%s instance=%s"'%(dataset,instance)
    cmd_out = getoutput( cmd )
    tmpList = cmd_out.split(os.linesep)
    files = []
    for l in tmpList:
        if l.find(".root") != -1:
            files.append(l)
	         
    return files 


def createJobs(f, outfolder,name,nchunks, channel, toWrite):
  infiles = []
  for files in f:
    infiles.append("root://cms-xrd-global.cern.ch/"+files)
  cmd = 'python job.py %s %s %s %i %s \n'%(','.join(infiles), outfolder,name,nchunks, channel)
#  print cmd

  if toWrite:
      jobs.write(cmd)

  return 1


def submitJobs(jobList, nchunks, outfolder, batchSystem):
    print 'Reading joblist'
    jobListName = jobList
    print jobList
#    subCmd = 'qsub -t 1-%s -o logs nafbatch_runner_GEN.sh %s' %(nchunks,jobListName)
    subCmd = 'qsub -t 1-%s -o %s/logs/ %s %s' %(nchunks,outfolder,batchSystem,jobListName)
    print 'Going to submit', nchunks, 'jobs with', subCmd
    os.system(subCmd)

    return 1


batchSystem = 'psibatch_runner.sh'
        
for directory in os.listdir("./"):

#    if directory.find('W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8__ytakahas-NanoTest_20180507_W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8-a7a5b67d3e3590e4899e147be08660be__USER')==-1: continue

    filelist = glob.glob(directory + '/*_' + options.channel + '.root')

    if not filelist: continue
    
    total = 0

    files = getFileListDAS('/' + directory.replace('__', '/'))
    filelists = list(split_seq(files, options.njob))
        
    jobList = 'joblist/joblist%s_%s_retry.txt' % (directory, options.channel)
    jobs = open(jobList, 'w')

    ids = []

    for file2check in filelist:
        
        f = TFile(file2check, "read")

        if f.GetListOfKeys().Contains("tree"): continue

        total += 1
        
        id = file2check.split('_')[-2]
        
#        print 'id = ', id

        ids.append(id)

        nChunks = 0

        for f in filelists:

            if int(id) == nChunks:
                createJobs(f, directory,directory, nChunks, options.channel, True)
            else:
                createJobs(f, directory,directory, nChunks, options.channel, False)
                
            nChunks = nChunks+1
		
    jobs.close()


    print bcolors.BOLD + bcolors.OKBLUE + 'Submmited ' + str(len(ids)) + 'jobs from ' + directory + bcolors.ENDC, ids

    if options.make:
        submitJobs(jobList, total, directory, batchSystem)

            
#    if flag:
#        print bcolors.FAIL + "[NG]" + directory + bcolors.ENDC
#        print '\t', len(files), ' out of ', str(total) + ' files are corrupted ... skip this sample (consider to resubmit the job)'
#
#    else:
#        print bcolors.BOLD + bcolors.OKBLUE + '[OK] ' + directory + bcolors.ENDC



