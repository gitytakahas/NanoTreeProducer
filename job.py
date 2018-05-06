#!/Usr-/bin/env python

import os,sys

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 



def ensureDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



if len(sys.argv)>1:
   infile = sys.argv[1].split(',')
else:
   print '[warning] input file not specified'

#   infile = ["root://cms-xrd-global.cern.ch//store/user/arizzi/Nano01_17Nov17/SingleMuon/RunII2017ReReco17Nov17-94X-Nano01/180205_181602/0000/test_data_94X_NANO_432.root"]
   infile = ["root://cms-xrd-global.cern.ch//store/user/arizzi/Nano01Fall17/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X-Nano01Fall17/180205_160029/0000/test94X_NANO_70.root"]

if len(sys.argv)>2:
    outputDir = sys.argv[2]
else:
    print '[warning] output directory name not specified'
    outputDir = "test"
    
if len(sys.argv)>3:
    name = sys.argv[3]
else:
    print '[warning] output filename not specified'
    name = "test"

if len(sys.argv)>4:
    chunck = sys.argv[4]
else:
    print '[warning] chunck not specified'
    chunck = "test"
    
   
if len(sys.argv)>5:
    channel = sys.argv[5]
else:
    print '[warning] channel not specified'
    channel = "mutau"
    


print '-'*80
print 'input file =', infile
print 'output directory = ', outputDir
print 'output filename = ', name
print 'output chunck = ', chunck
print 'channel = ', channel
print '-'*80


DataType = 'mc'

if infile[0].find("/SingleMuon/")!=-1 or infile[0].find("/Tau/")!=-1:
    DataType = 'data'


json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

ensureDir(outputDir)

_postfix = outputDir + '/' + name + '_' + chunck + '_' + channel + '.root'

module2run = None

if channel == 'tautau':

    from TauTauModule import *

    module2run = lambda : TauTauProducer(_postfix, DataType)

elif channel == 'mutau':

    from MuTauModule import *

    module2run = lambda : MuTauProducer(_postfix, DataType)


else:
    print 'Unkonwn channel !!!!!!!'
    sys.exit(0)





if DataType=='data':
    p=PostProcessor(outputDir, infile, None, "keep_and_drop.txt", noOut=True, 
                    modules=[module2run()],provenance=False,fwkJobReport=False,
                    jsonInput=json, postfix=_postfix)

    
else:
    p=PostProcessor(outputDir, infile, None, "keep_and_drop.txt", noOut=True,
                    modules=[module2run()],provenance=False,fwkJobReport=False, postfix=_postfix)




p.run()
print "DONE"
