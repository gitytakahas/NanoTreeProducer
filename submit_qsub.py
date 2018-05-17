#!/usr/bin/env python

import os
from commands import getoutput
import itertools
import optparse

parser = optparse.OptionParser()

parser.add_option('-f', '--force', action="store_true", default=False, dest='force')
parser.add_option('-c', '--channel', action="store", type="string", default="mutau", dest='channel')
parser.add_option('-s', '--sample', action="store", type="string", default=None, dest='sample')
parser.add_option('-n', '--njob', action="store", type=int, default=1, dest='njob')

(options, args) = parser.parse_args() 

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
    
#    cmd='das_client --limit=0 --query="file dataset=%s instance=%s"'%(dataset,instance)
    cmd='das_client --limit=0 --query="file dataset=%s instance=%s status=*"'%(dataset,instance)
    print "Executing ",cmd
    cmd_out = getoutput( cmd )
    tmpList = cmd_out.split(os.linesep)
    files = []
    for l in tmpList:
        if l.find(".root") != -1:
            files.append(l)
	         
    return files 
   
def createJobs(f, outfolder,name,nchunks, channel):
  infiles = []
  for files in f:
    infiles.append("root://cms-xrd-global.cern.ch/"+files)
  cmd = 'python job.py %s %s %s %i %s \n'%(','.join(infiles), outfolder,name,nchunks, channel)
  print cmd
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


if __name__ == "__main__":

	batchSystem = 'psibatch_runner.sh'

        # read samples
        patterns = []
        
        for line in open('samples.cfg', 'r'):

                        
            if line.find('#')!=-1: continue
            if line.count('/')!=3:
                continue 


            patterns.append(line.rstrip())


	
	for pattern in patterns:

            
                if options.sample!=None:
                        if pattern.find(options.sample)==-1: continue

		files = getFileListDAS(pattern)
#		print "FILELIST = ", files
#                print pattern.split('/')

		name = pattern.split("/")[1].replace("/","") + '__' + pattern.split("/")[2].replace("/","") + '__' + pattern.split("/")[3].replace("/","")

#		if sys.argv[1].find("data")!=-1: 
#                    name = pattern.split("/")[2].replace("/","")

                print 
		print "creating job file " ,'joblist/joblist%s.txt'%name
                print 
		try: os.stat('joblist/')
		except: os.mkdir('joblist/')
		jobList = 'joblist/joblist%s_%s.txt' % (name, options.channel)
		jobs = open(jobList, 'w')
		nChunks = 0

                outfolder = name

		try: os.stat(outfolder)
		except: os.mkdir(outfolder)
		try: os.stat(outfolder+'/logs/')
		except: os.mkdir(outfolder+'/logs/')

		filelists = list(split_seq(files, options.njob))
#		filelists = list(split_seq(files,1))

		for f in filelists:
#			print "FILES = ",f
			createJobs(f,outfolder,name,nChunks, options.channel)
			nChunks = nChunks+1
		
		jobs.close()


                if options.force:
                    submitJobs(jobList,nChunks, outfolder, batchSystem)

                else:
                    submit = raw_input("Do you also want to submit " + str(nChunks) + " jobs to the batch system? [y/n] ")

                    if submit == 'y' or submit=='Y':
                        submitJobs(jobList,nChunks, outfolder, batchSystem)
                    else:
                        print "Not submitting jobs"
		
		
		
