
#!/usr/bin/env python
import os, sys
#import ROOT
#ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from TauTauModule import *

channel = 'tautau'
#channel = 'mutau'
DataType = 'mc'
#DataType = 'data'

#print len(sys.argv)

if len(sys.argv)>1:
    channel = sys.argv[1]

if len(sys.argv)>2:
    DataType = sys.argv[2]

print 'channel = ', channel 

if DataType=='data':
    filelist = ['root://cms-xrd-global.cern.ch//store/data/Run2017B/Tau/NANOAOD/31Mar2018-v1/10000/04463969-D044-E811-8DC1-0242AC130002.root']
else:
#    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/70000/BEA974A4-3E42-E811-85BF-3417EBE51A24.root']
#    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/00000/88F83F15-B242-E811-808E-001E67792488.root',
    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/10000/0A5AB04B-4B42-E811-AD7F-A4BF0112BDE6.root']

#    filelist = ['root://cms-xrd-global.cern.ch//store/user/ytakahas/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTest_20180507_W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/180509_174102/0000/test94X_NANO_45.root']
#    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/70000/B28E4243-3245-E811-B18F-001E67E71BAA.root']

#    filelist = ['root://cms-xrd-global.cern.ch//store/user/ytakahas/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTest_20180507_W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/180509_174145/0000/test94X_NANO_48.root']
#                'root://cms-xrd-global.cern.ch//store/user/ytakahas/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/NanoTest_20180507_W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/180509_174145/0000/test94X_NANO_57.root']

_postfix = channel + '.root'

if channel == 'tautau':

    from TauTauModule import *

    module2run = lambda : TauTauProducer(_postfix, DataType)

elif channel == 'mutau':

    from MuTauModule import *

    module2run = lambda : MuTauProducer(_postfix, DataType)

else:
    print 'Invalid channel name'

#p=PostProcessor(".",["../../../crab/WZ_TuneCUETP8M1_13TeV-pythia8.root"],"Jet_pt>150","keep_and_drop.txt",[exampleModule()],provenance=True)

p=PostProcessor(".",filelist,None,"keep_and_drop.txt",noOut=True, modules=[module2run()],provenance=False, postfix=_postfix)

#p=PostProcessor(".",filelist,None,"keep_and_drop.txt",noOut=True, modules=[module2run()],provenance=False, jsonInput='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt', postfix=_postfix)

p.run()
