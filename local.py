#!/usr/bin/env python
import os, sys
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

import optparse

parser = optparse.OptionParser()

parser.add_option('-c', '--channel', action="store", type="string", default="tautau", dest='channel')
parser.add_option('-t', '--type', action="store", type="string", default="mc", dest='type')

(options, args) = parser.parse_args() 

print 'channel  =', options.channel

#channel = 'tautau'
#channel = 'mutau'
#channel = 'eletau'
channel = options.channel
#channel = 'muele'

DataType = options.type
#DataType = 'data'

#print len(sys.argv)

#if len(sys.argv)>1:
#    channel = sys.argv[1]

#if len(sys.argv)>2:
#    DataType = sys.argv[2]

print 'channel = ', channel 
print 'DataType = ', DataType

if DataType=='data':
    filelist = ['root://cms-xrd-global.cern.ch//store/data/Run2017B/Tau/NANOAOD/31Mar2018-v1/10000/04463969-D044-E811-8DC1-0242AC130002.root']
else:
#    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/10000/0A5AB04B-4B42-E811-AD7F-A4BF0112BDE6.root']
#    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/20000/82C67179-0942-E811-9BA7-001E67FA3920.root']
#    filelist = ['root://cms-xrd-global.cern.ch//store/mc/RunIIFall17NanoAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/5E621211-8B42-E811-9903-001E67F8FA2E.root']


#    filelist = ['dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/ytakahas/LQ3ToTauB_Fall2017_5f_Madgraph_LO_pair-M500/nanoAOD/v1/nanoAOD_LQ3ToTauB_Fall2017_5f_Madgraph_LO_pair-M500_1602.root']
    filelist = ['dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/ytakahas/VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000/nanoAOD/v1/nanoAOD_VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000_1036.root',
                'dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/ytakahas/VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000/nanoAOD/v1/nanoAOD_VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000_105.root',
                'dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/ytakahas/VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000/nanoAOD/v1/nanoAOD_VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M1000_1059.root',
                ]
#    filelist = ['dcap://t3se01.psi.ch:22125//pnfs/psi.ch/cms/trivcat/store/user/ytakahas/VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M500/nanoAOD/v1/nanoAOD_VectorLQ3ToTauB_Fall2017_5f_Madgraph_LO_pair_M500_133.root']


_postfix = channel + '.root'

if channel == 'tautau':

#    from TauTauModule_sync import *
    from TauTauModule import *

    module2run = lambda : TauTauProducer(_postfix, DataType)

elif channel == 'mutau':

#    from MuTauModule_sync import *
    from MuTauModule import *

    module2run = lambda : MuTauProducer(_postfix, DataType)

elif channel == 'eletau':

#    from EleTauModule_sync import *
    from EleTauModule import *

    module2run = lambda : EleTauProducer(_postfix, DataType)

elif channel == 'mumu':

    from MuMuModule import *

    module2run = lambda : MuMuProducer(_postfix, DataType)

elif channel == 'muele':

    from MuEleModule import *

    module2run = lambda : MuEleProducer(_postfix, DataType)

else:
    print 'Invalid channel name'

#p=PostProcessor(".",["../../../crab/WZ_TuneCUETP8M1_13TeV-pythia8.root"],"Jet_pt>150","keep_and_drop.txt",[exampleModule()],provenance=True)

p=PostProcessor(".",filelist,None,"keep_and_drop.txt",noOut=True, modules=[module2run()],provenance=False, postfix=_postfix)

#p=PostProcessor(".",filelist,None,"keep_and_drop.txt",noOut=True, modules=[module2run()],provenance=False, jsonInput='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt', postfix=_postfix)

p.run()
