#!/usr/bin/env python
import os, sys
#import ROOT
#ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from TauTauModule import *

channel = 'mutau'
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
    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/70000/BEA974A4-3E42-E811-85BF-3417EBE51A24.root']


_postfix = channel

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
