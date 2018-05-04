#!/usr/bin/env python
import os, sys
#import ROOT
#ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from TauTauModule import *

channel = 'mutau'

_postfix = channel

if channel == 'tautau':

    from TauTauModule import *

    module2run = lambda : TauTauProducer(_postfix)

elif channel == 'mutau':

    from MuTauModule import *

    module2run = lambda : MuTauProducer(_postfix)

else:
    print 'Invalid channel name'

#p=PostProcessor(".",["../../../crab/WZ_TuneCUETP8M1_13TeV-pythia8.root"],"Jet_pt>150","keep_and_drop.txt",[exampleModule()],provenance=True)

p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/70000/BEA974A4-3E42-E811-85BF-3417EBE51A24.root"],None,"keep_and_drop.txt",noOut=True, modules=[module2run()],provenance=False, postfix=_postfix)

p.run()
