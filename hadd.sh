channel=${1}

echo $channel

datasetname=""

if [ $channel = "mutau" -o $channel = "muele" -o $channel = "mumu" ]; then

    datasetname="SingleMuon"

elif [ $channel = "eletau" ]; then
    
    datasetname="SingleElectron"


elif [ $channel = "tautau" ]; then

    datasetname="Tau"
    
else

    echo "unknown dataset name ..."
fi

mkdir -p ${datasetname}
hadd ${datasetname}/${channel}.root ${datasetname}_*/${channel}.root




mkdir -p ZTT
hadd ZTT/${channel}.root DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8__RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14*__NANOAODSIM/${channel}.root