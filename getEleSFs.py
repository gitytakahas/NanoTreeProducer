import ROOT
import math

path = '/mnt/t3nfs01/data01/shome/ytakahas/work/Leptoquark/CMSSW_9_4_4/src/PhysicsTools/NanoAODTools/NanoTreeProducer/leptonSF'

class getEleSFs :
    

    def __init__( self ):

        # Load the TH1s containing the bin by bin values
        self.f = ROOT.TFile( path + '/gammaEffi.txt_EGM2D_runBCDEF_passingMVA94Xwp90iso.root', 'r')
        self.electron = self.f.Get('EGamma_SF2D')

        self.f_reco = ROOT.TFile( path + '/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root', 'r')
        self.electron_reco = self.f_reco.Get('EGamma_SF2D')


    # Make sure we stay on our histograms
    def getEleWeight( self, pt, eta ) :
#        abseta = math.fabs(eta)

        if pt > 500:
            pt = 490

        xbin = self.electron.GetXaxis().FindBin(eta)
        ybin = self.electron.GetYaxis().FindBin(pt)

        sf = self.electron.GetBinContent(xbin, ybin)
#        print 'pt = ', pt, '(bin id = ', xbin, '), eta = ', eta, '(bin id = ', ybin, ') => ', sf


        xbin_reco = self.electron_reco.GetXaxis().FindBin(eta)
        ybin_reco = self.electron_reco.GetYaxis().FindBin(pt)

        sf_reco = self.electron_reco.GetBinContent(xbin_reco, ybin_reco)

#        print 'sf = ', sf, 'sf_reco = ', sf_reco
        
        return sf*sf_reco
