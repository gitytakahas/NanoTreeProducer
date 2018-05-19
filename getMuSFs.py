import ROOT
import math

path = '/mnt/t3nfs01/data01/shome/ytakahas/work/Leptoquark/CMSSW_9_4_4/src/PhysicsTools/NanoAODTools/NanoTreeProducer/leptonSF'

class getMuSFs :
    

    def __init__( self ):

        # Load the TH1s containing the bin by bin values
        self.f = ROOT.TFile( path + '/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root', 'r')
        self.muon = self.f.Get('IsoMu27_PtEtaBins/pt_abseta_ratio')


    # Make sure we stay on our histograms
    def getMuWeight( self, pt, eta ) :
        abseta = math.fabs(eta)
        xbin = self.muon.GetXaxis().FindBin(pt)
        ybin = self.muon.GetYaxis().FindBin(abseta)

        sf = self.muon.GetBinContent(xbin, ybin)
        
        return sf
