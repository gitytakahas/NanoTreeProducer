channel="mutau"


read -p "Are you sure to do hadd for ${channel} channel? " -n 1 -r
echo    # (optional) move to a new line

if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "OK !"

    for i in $(ls -d */)
    do 
	
	if stat --printf='' $i/*.root 2>/dev/null
	then
	    echo ${i%%/}
	else
	    continue
	fi
	
	mkdir -p /scratch/ytakahas/NanoAOD/${i%%/}
	rm -f /scratch/ytakahas/NanoAOD/${i%%/}/${channel}.root


#	haddnano.py /scratch/ytakahas/NanoAOD/${i%%/}/${channel}.root $i/*${channel}*.root

	hadd /scratch/ytakahas/NanoAOD/${i%%/}/${channel}.root $i/*${channel}*.root
    done

    echo "done"

else
    echo "Not executed"
fi





#haddnano.py /scratch/thaarres/NANO_06feb/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/SingleMuon_Run2017B-17Nov2017-v1.root thaarres-SingleMuon_Run2017B-17Nov2017-v1-351ed72508aa977f1c65d26f45752bf7/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/SingleMuon_Run2017C-17Nov2017-v1.root thaarres-SingleMuon_Run2017C-17Nov2017-v1-351ed72508aa977f1c65d26f45752bf7/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/SingleMuon_Run2017D-17Nov2017-v1.root thaarres-SingleMuon_Run2017D-17Nov2017-v1-351ed72508aa977f1c65d26f45752bf7/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/SingleMuon_Run2017E-17Nov2017-v1.root thaarres-SingleMuon_Run2017E-17Nov2017-v1-351ed72508aa977f1c65d26f45752bf7/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/SingleMuon_Run2017F-17Nov2017-v1.root thaarres-SingleMuon_Run2017F-17Nov2017-v1-351ed72508aa977f1c65d26f45752bf7/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8.root TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WW_TuneCP5_13TeV-pythia8.root WW_TuneCP5_13TeV-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/WZ_TuneCP5_13TeV-pythia8.root WZ_TuneCP5_13TeV-pythia8/*.root
#haddnano.py /scratch/thaarres/NANO_06feb/ZZ_TuneCP5_13TeV-pythia8.root ZZ_TuneCP5_13TeV-pythia8/*.root
