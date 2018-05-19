import ROOT
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from TreeProducerEleTau import *


class declareVariables(TreeProducerEleTau):
    
    def __init__(self, name):

        super(declareVariables, self).__init__(name)


class EleTauProducer(Module):

    def __init__(self, name, DataType):

        self.name = name
        self.out = declareVariables(name)

        if DataType=='data':
            self.isData = True
        else:
            self.isData = False

        self.Nocut = 0
        self.Trigger = 1
        self.GoodElectrons = 2
        self.GoodTaus = 3
        self.GoodDiLepton = 4
        self.TotalWeighted = 15

    def beginJob(self):
        pass

    def endJob(self):
        self.out.outputfile.Write()
        self.out.outputfile.Close()
#        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):        
        pass
        
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

#        electrons = Collection(event, "Electron")


        #####################################
        self.out.h_cutflow.Fill(self.Nocut)
        #####################################

        #####################################
        if not self.isData:
            self.out.h_cutflow.Fill(self.TotalWeighted, event.genWeight)
        else:
            self.out.h_cutflow.Fill(self.TotalWeighted, 1.)
        #####################################

        if not event.HLT_Ele32_WPTight_Gsf:
            return False

        #####################################
        self.out.h_cutflow.Fill(self.Trigger)
        #####################################

        idx_goodelectrons = []
        
        for ielectron in range(event.nElectron):

            if event.Electron_pt[ielectron] < 33: continue
            if abs(event.Electron_eta[ielectron]) > 2.1: continue
            if abs(event.Electron_dz[ielectron]) > 0.2: continue
            if abs(event.Electron_dxy[ielectron]) > 0.045: continue
            if event.Electron_convVeto[ielectron] !=1: continue
            if ord(event.Electron_lostHits[ielectron]) > 1: continue
            if event.Electron_mvaFall17Iso_WP80[ielectron] < 0.5: continue

            idx_goodelectrons.append(ielectron)


        if len(idx_goodelectrons)==0:
            return False

        #####################################
        self.out.h_cutflow.Fill(self.GoodElectrons)
        #####################################



        idx_goodtaus = []
        
        for itau in range(event.nTau):

            if event.Tau_pt[itau] < 20: continue
            if abs(event.Tau_eta[itau]) > 2.3: continue
            if abs(event.Tau_dz[itau]) > 0.2: continue
            if event.Tau_decayMode[itau] not in [0,1,10]: continue
            if abs(event.Tau_charge[itau])!=1: continue

            idx_goodtaus.append(itau)



        if len(idx_goodtaus)==0:
            return False


        #####################################
        self.out.h_cutflow.Fill(self.GoodTaus)
        #####################################

        
        # to check dR matching

        electrons = Collection(event, "Electron")
        taus = Collection(event, "Tau")
        dileptons = []

        for idx1 in idx_goodelectrons:
            for idx2 in idx_goodtaus:
                
                if idx1 >= idx2: continue

                dR = taus[idx2].p4().DeltaR(electrons[idx1].p4())
                if dR < 0.5: continue
                
                electron_reliso = event.Electron_pfRelIso03_all[idx1]
                
                _dilepton = DiLeptonBasicClass(idx1, event.Electron_pt[idx1], electron_reliso, idx2, event.Tau_pt[idx2], event.Tau_rawMVAoldDM[idx2])

                dileptons.append(_dilepton)

        if len(dileptons)==0:
            return False


        #####################################
        self.out.h_cutflow.Fill(self.GoodDiLepton)
        #####################################

        dilepton = bestDiLepton(dileptons)

#        print 'chosen tau1 (idx, pt) = ', dilepton.tau1_idx, dilepton.tau1_pt, 'check', taus[dilepton.tau1_idx].p4().Pt()
#        print 'chosen tau2 (idx, pt) = ', dilepton.tau2_idx, dilepton.tau2_pt, 'check', taus[dilepton.tau2_idx].p4().Pt()

        jetIds = []

        jets = Collection(event, "Jet")
#        jets = filter(self.jetSel,jets):

        nfjets = 0
        ncjets = 0
        nbtag = 0

        for ijet in range(event.nJet):

#        for j in filter(self.jetSel,jets):


            if event.Jet_pt[ijet] < 30: 
                continue

            if abs(event.Jet_eta[ijet]) > 4.7: 
                continue

            dR = electrons[dilepton.tau1_idx].p4().DeltaR(jets[ijet].p4())
            if dR < 0.5: 
                continue

            dR = taus[dilepton.tau2_idx].p4().DeltaR(jets[ijet].p4())

            if dR < 0.5: 
                continue

#            print '#', ijet, 'pt = ', jets[ijet].p4().Pt(), event.Jet_pt[ijet]

            jetIds.append(ijet)
            
            if abs(event.Jet_eta[ijet]) > 2.4:
                nfjets += 1
            else:
                ncjets += 1

            if event.Jet_btagCSVV2[ijet] > 0.8838:
                nbtag += 1
            
            

#        eventSum = ROOT.TLorentzVector()
#
#        for lep in electrons :
#            eventSum += lep.p4()
#        for lep in electrons :
#            eventSum += lep.p4()
#        for j in filter(self.jetSel,jets):
#            eventSum += j.p4()


        # electron
        self.out.pt_1[0]                       = event.Electron_pt[dilepton.tau1_idx]
        self.out.eta_1[0]                      = event.Electron_eta[dilepton.tau1_idx]
        self.out.phi_1[0]                      = event.Electron_phi[dilepton.tau1_idx]
        self.out.mass_1[0]                     = event.Electron_mass[dilepton.tau1_idx]
        self.out.dxy_1[0]                      = event.Electron_dxy[dilepton.tau1_idx]
        self.out.dz_1[0]                       = event.Electron_dz[dilepton.tau1_idx]         
        self.out.q_1[0]                        = event.Electron_charge[dilepton.tau1_idx]
        self.out.pfRelIso03_all_1[0]           = event.Electron_pfRelIso03_all[dilepton.tau1_idx]
        self.out.cutBased_1[0]                 = event.Electron_cutBased[dilepton.tau1_idx]
        self.out.mvaFall17Iso_1[0]             = event.Electron_mvaFall17Iso[dilepton.tau1_idx]
        self.out.mvaFall17Iso_WP80_1[0]        = event.Electron_mvaFall17Iso_WP80[dilepton.tau1_idx]
        self.out.mvaFall17Iso_WP90_1[0]        = event.Electron_mvaFall17Iso_WP90[dilepton.tau1_idx]
        self.out.mvaFall17Iso_WPL_1[0]         = event.Electron_mvaFall17Iso_WPL[dilepton.tau1_idx]



        # tau 2
        self.out.pt_2[0]                       = event.Tau_pt[dilepton.tau2_idx]
        self.out.eta_2[0]                      = event.Tau_eta[dilepton.tau2_idx]
        self.out.phi_2[0]                      = event.Tau_phi[dilepton.tau2_idx]
        self.out.mass_2[0]                     = event.Tau_mass[dilepton.tau2_idx]
        self.out.dxy_2[0]                      = event.Tau_dxy[dilepton.tau2_idx]
        self.out.dz_2[0]                       = event.Tau_dz[dilepton.tau2_idx]         
        self.out.leadTkPtOverTauPt_2[0]        = event.Tau_leadTkPtOverTauPt[dilepton.tau2_idx]
        self.out.chargedIso_2[0]               = event.Tau_chargedIso[dilepton.tau2_idx]
        self.out.neutralIso_2[0]               = event.Tau_neutralIso[dilepton.tau2_idx]
        self.out.photonsOutsideSignalCone_2[0] = event.Tau_photonsOutsideSignalCone[dilepton.tau2_idx]
        self.out.puCorr_2[0]                   = event.Tau_puCorr[dilepton.tau2_idx]
        self.out.rawAntiEle_2[0]               = event.Tau_rawAntiEle[dilepton.tau2_idx]
        self.out.rawIso_2[0]                   = event.Tau_rawIso[dilepton.tau2_idx]
        self.out.rawMVAnewDM2017v2_2[0]        = event.Tau_rawMVAnewDM2017v2[dilepton.tau2_idx]
        self.out.rawMVAoldDM_2[0]              = event.Tau_rawMVAoldDM[dilepton.tau2_idx]
        self.out.rawMVAoldDM2017v1_2[0]        = event.Tau_rawMVAoldDM2017v1[dilepton.tau2_idx]
        self.out.rawMVAoldDM2017v2_2[0]        = event.Tau_rawMVAoldDM2017v2[dilepton.tau2_idx]
        self.out.q_2[0]                        = event.Tau_charge[dilepton.tau2_idx]
        self.out.decayMode_2[0]                = event.Tau_decayMode[dilepton.tau2_idx]
        self.out.rawAntiEleCat_2[0]            = event.Tau_rawAntiEleCat[dilepton.tau2_idx]
        self.out.idAntiEle_2[0]                = ord(event.Tau_idAntiEle[dilepton.tau2_idx])
        self.out.idAntiMu_2[0]                 = ord(event.Tau_idAntiMu[dilepton.tau2_idx])
        self.out.idDecayMode_2[0]              = event.Tau_idDecayMode[dilepton.tau2_idx]
        self.out.idDecayModeNewDMs_2[0]        = event.Tau_idDecayModeNewDMs[dilepton.tau2_idx]
        self.out.idMVAnewDM2017v2_2[0]         = ord(event.Tau_idMVAnewDM2017v2[dilepton.tau2_idx])
        self.out.idMVAoldDM_2[0]               = ord(event.Tau_idMVAoldDM[dilepton.tau2_idx])
        self.out.idMVAoldDM2017v1_2[0]         = ord(event.Tau_idMVAoldDM2017v1[dilepton.tau2_idx])
        self.out.idMVAoldDM2017v2_2[0]         = ord(event.Tau_idMVAoldDM2017v2[dilepton.tau2_idx])

#        print type(event.Tau_genPartFlav[dilepton.tau2_idx])

        if not self.isData:
            self.out.genPartFlav_1[0]              = ord(event.Electron_genPartFlav[dilepton.tau1_idx])
            self.out.genPartFlav_2[0]              = ord(event.Tau_genPartFlav[dilepton.tau2_idx])

            genvistau = Collection(event, "GenVisTau")

            _drmax_ = 1000
            gendm = -1
            genpt = -1
            geneta = -1
            genphi = -1

            for igvt in range(event.nGenVisTau):

                _dr_ = genvistau[igvt].p4().DeltaR(taus[dilepton.tau2_idx].p4())
            
                if _dr_ < 0.5 and _dr_ < _drmax_:
                    _drmax_ = _dr_
                    gendm = event.GenVisTau_status[igvt]
                    genpt = event.GenVisTau_pt[igvt]
                    geneta = event.GenVisTau_eta[igvt]
                    genphi = event.GenVisTau_phi[igvt]

            self.out.gendecayMode_2[0]         = gendm
            self.out.genvistaupt_2[0]          = genpt
            self.out.genvistaueta_2[0]         = geneta
            self.out.genvistauphi_2[0]         = genphi


        # event weights
        self.out.run[0]                        = event.run
        self.out.luminosityBlock[0]            = event.luminosityBlock
        self.out.event[0]                      = event.event & 0xffffffffffffffff
        self.out.MET_pt[0]                     = event.MET_pt
        self.out.MET_phi[0]                    = event.MET_phi
        self.out.PuppiMET_pt[0]                = event.PuppiMET_pt
        self.out.PuppiMET_phi[0]               = event.PuppiMET_phi
        self.out.MET_significance[0]           = event.MET_significance
        self.out.MET_covXX[0]                  = event.MET_covXX
        self.out.MET_covXY[0]                  = event.MET_covXY
        self.out.MET_covYY[0]                  = event.MET_covYY
        self.out.fixedGridRhoFastjetAll[0]     = event.fixedGridRhoFastjetAll
        self.out.PV_npvs[0]                    = event.PV_npvs
        self.out.PV_npvsGood[0]                = event.PV_npvsGood

        if not self.isData:
            self.out.GenMET_pt[0]                  = event.GenMET_pt
            self.out.GenMET_phi[0]                 = event.GenMET_phi
            self.out.Pileup_nPU[0]                 = event.Pileup_nPU
            self.out.Pileup_nTrueInt[0]            = event.Pileup_nTrueInt
            self.out.genWeight[0]                  = event.genWeight
            self.out.LHE_Njets[0]                  = event.LHE_Njets


        self.out.jpt_1[0]                      = -9.
        self.out.jeta_1[0]                     = -9.
        self.out.jphi_1[0]                     = -9.
        self.out.jcsvv2_1[0]                   = -9.
        self.out.jdeepb_1[0]                   = -9.

        self.out.jpt_2[0]                      = -9.
        self.out.jeta_2[0]                     = -9.
        self.out.jphi_2[0]                     = -9.
        self.out.jcsvv2_2[0]                   = -9.
        self.out.jdeepb_2[0]                   = -9.


        if len(jetIds)>0:
            self.out.jpt_1[0]                      = event.Jet_pt[jetIds[0]]
            self.out.jeta_1[0]                     = event.Jet_eta[jetIds[0]]
            self.out.jphi_1[0]                     = event.Jet_phi[jetIds[0]]
            self.out.jcsvv2_1[0]                   = event.Jet_btagCSVV2[jetIds[0]]
            self.out.jdeepb_1[0]                   = event.Jet_btagDeepB[jetIds[0]]

        if len(jetIds)>1:
            self.out.jpt_2[0]                      = event.Jet_pt[jetIds[1]]
            self.out.jeta_2[0]                     = event.Jet_eta[jetIds[1]]
            self.out.jphi_2[0]                     = event.Jet_phi[jetIds[1]]
            self.out.jcsvv2_2[0]                   = event.Jet_btagCSVV2[jetIds[1]]
            self.out.jdeepb_2[0]                   = event.Jet_btagDeepB[jetIds[1]]


        self.out.njets[0]                      = len(jetIds)
        self.out.nfjets[0]                     = nfjets
        self.out.ncjets[0]                     = ncjets
        self.out.nbtag[0]                      = nbtag

        self.out.pfmt_1[0]                     = math.sqrt( 2 * self.out.pt_1[0] * self.out.MET_pt[0] * ( 1 - math.cos(deltaPhi(self.out.phi_1[0], self.out.MET_phi[0])) ) );
        self.out.pfmt_2[0]                     = math.sqrt( 2 * self.out.pt_2[0] * self.out.MET_pt[0] * ( 1 - math.cos(deltaPhi(self.out.phi_2[0], self.out.MET_phi[0])) ) );

        self.out.m_vis[0]                      = (electrons[dilepton.tau1_idx].p4() + taus[dilepton.tau2_idx].p4()).M()
        self.out.pt_tt[0]                      = (electrons[dilepton.tau1_idx].p4() + taus[dilepton.tau2_idx].p4()).Pt()
        
        self.out.dR_ll[0]                      = electrons[dilepton.tau1_idx].p4().DeltaR(taus[dilepton.tau2_idx].p4())
        self.out.dphi_ll[0]                    = deltaPhi(self.out.phi_1[0], self.out.phi_2[0])


        # pzeta calculation

        leg1 = ROOT.TVector3(electrons[dilepton.tau1_idx].p4().Px(), electrons[dilepton.tau1_idx].p4().Py(), 0.)
        leg2 = ROOT.TVector3(taus[dilepton.tau2_idx].p4().Px(), taus[dilepton.tau2_idx].p4().Py(), 0.)
        
#        print 'leg1 px,py,pz = ', taus[dilepton.tau1_idx].p4().Px(), taus[dilepton.tau1_idx].p4().Py(), '0'
#        print 'leg2 px,py,pz = ', taus[dilepton.tau2_idx].p4().Px(), taus[dilepton.tau2_idx].p4().Py(), '0'

        met_tlv = ROOT.TLorentzVector()
        met_tlv.SetPxPyPzE(self.out.MET_pt[0]*math.cos(self.out.MET_phi[0]), 
                           self.out.MET_pt[0]*math.cos(self.out.MET_phi[0]),
                           0, 
                           self.out.MET_pt[0])

#        print self.out.MET_pt[0]*math.cos(self.out.MET_phi[0]), self.out.MET_pt[0]*math.cos(self.out.MET_phi[0]), '0', self.out.MET_pt[0]

        metleg = met_tlv.Vect()
        zetaAxis = ROOT.TVector3(leg1.Unit() + leg2.Unit()).Unit()
        pZetaVis_ = leg1*zetaAxis + leg2*zetaAxis
        pZetaMET_ = metleg*zetaAxis
        
#        print 'pZetaVis = ', pZetaVis_, ' pZetaMET = ', pZetaMET_                                                                                           

        self.out.pzetamiss[0]  = pZetaMET_
        self.out.pzetavis[0]   = pZetaVis_
        self.out.pzeta_disc[0] = pZetaMET_ - 0.5*pZetaVis_


        # extra lepton vetos
        self.out.extramuon_veto[0], self.out.extraelec_veto[0], self.out.dilepton_veto[0]  = extraLeptonVetos(event, [-1], [dilepton.tau1_idx], self.name)

        self.out.isData[0] = self.isData

        self.out.tree.Fill() 

        return True
