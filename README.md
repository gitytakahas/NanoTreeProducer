# NanoTreeProducer
Produce analysis tree directly from NanoAODs

Fisrt, install NanoAODTools:

```
cmsrel CMSSW_9_4_6
cd CMSSW_9_4_6/src
cmsenv
git cms-init   #not really needed unless you later want to add some other cmssw stuff
git clone https://github.com/cms-nanoAOD/nanoAOD-tools.git PhysicsTools/NanoAODTools
scram b
```

Then, install this package:

```
git clone https://github.com/gitytakahas/NanoTreeProducer
```

You might want to change analyzers and tree basic classes for whatever analysis you want.
The examples below are for the mu-tau analysis

```
MuTauModule.py
TreeProducerBaseMuTau.py
```

For job submission, you need to modify samples to which you want to process

```
samples.cfg
```

and then do, something like, 

```
python submit_qsub.py -c mutau
```

