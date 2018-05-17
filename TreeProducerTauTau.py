from TreeProducerCommon import *

class TreeProducerTauTau(TreeProducerCommon):

    def __init__(self, name):

        super(TreeProducerTauTau, self).__init__(name)
        
        print 'TreeProducerTauTau is called', name


        # trees
        ##################
        # tau 1 
        ##################

        self.pt_1                       = num.zeros(1, dtype=float)
        self.eta_1                      = num.zeros(1, dtype=float)
        self.phi_1                      = num.zeros(1, dtype=float)
        self.mass_1                     = num.zeros(1, dtype=float)
        self.dxy_1                      = num.zeros(1, dtype=float)
        self.dz_1                       = num.zeros(1, dtype=float)        
        self.leadTkPtOverTauPt_1        = num.zeros(1, dtype=float)
        self.chargedIso_1               = num.zeros(1, dtype=float)
        self.neutralIso_1               = num.zeros(1, dtype=float)
        self.photonsOutsideSignalCone_1 = num.zeros(1, dtype=float)
        self.puCorr_1                   = num.zeros(1, dtype=float)
        self.rawAntiEle_1               = num.zeros(1, dtype=float)
        self.rawIso_1                   = num.zeros(1, dtype=float)
        self.rawMVAnewDM2017v2_1        = num.zeros(1, dtype=float)
        self.rawMVAoldDM_1              = num.zeros(1, dtype=float)
        self.rawMVAoldDM2017v1_1        = num.zeros(1, dtype=float)
        self.rawMVAoldDM2017v2_1        = num.zeros(1, dtype=float)
        self.charge_1                   = num.zeros(1, dtype=int)
        self.decayMode_1                = num.zeros(1, dtype=int)
        self.rawAntiEleCat_1            = num.zeros(1, dtype=float)
        self.idAntiEle_1                = num.zeros(1, dtype=int)
        self.idAntiMu_1                 = num.zeros(1, dtype=int)
        self.idDecayMode_1              = num.zeros(1, dtype=int)
        self.idDecayModeNewDMs_1        = num.zeros(1, dtype=int)
        self.idMVAnewDM2017v2_1         = num.zeros(1, dtype=int)
        self.idMVAoldDM_1               = num.zeros(1, dtype=int)
        self.idMVAoldDM2017v1_1         = num.zeros(1, dtype=int)
        self.idMVAoldDM2017v2_1         = num.zeros(1, dtype=int)
        self.genPartFlav_1              = num.zeros(1, dtype=int)
        self.gendecayMode_1             = num.zeros(1, dtype=int)
        self.genvistaupt_1              = num.zeros(1, dtype=float)
        self.genvistaueta_1             = num.zeros(1, dtype=float)
        self.genvistauphi_1             = num.zeros(1, dtype=float)
        

        
        self.tree.Branch('pt_1'                      , self.pt_1, 'pt_1/D')
        self.tree.Branch('eta_1'                     , self.eta_1, 'eta_1/D')
        self.tree.Branch('phi_1'                     , self.phi_1, 'phi_1/D')
        self.tree.Branch('mass_1'                    , self.mass_1, 'mass_1/D')
        self.tree.Branch('dxy_1'                     , self.dxy_1, 'dxy_1/D')
        self.tree.Branch('dz_1'                      , self.dz_1, 'dz_1/D')
        self.tree.Branch('leadTkPtOverTauPt_1'       , self.leadTkPtOverTauPt_1, 'leadTkPtOverTauPt_1/D')
        self.tree.Branch('chargedIso_1'              , self.chargedIso_1, 'chargedIso_1/D')
        self.tree.Branch('neutralIso_1'              , self.neutralIso_1, 'neutralIso_1/D')
        self.tree.Branch('photonsOutsideSignalCone_1', self.photonsOutsideSignalCone_1, 'photonsOutsideSignalCone_1/D')
        self.tree.Branch('puCorr_1'                  , self.puCorr_1, 'puCorr_1/D')
        self.tree.Branch('rawAntiEle_1'              , self.rawAntiEle_1, 'rawAntiEle_1/D')
        self.tree.Branch('rawIso_1'                  , self.rawIso_1, 'rawIso_1/D')
        self.tree.Branch('rawMVAnewDM2017v2_1'       , self.rawMVAnewDM2017v2_1, 'rawMVAnewDM2017v2_1/D')
        self.tree.Branch('rawMVAoldDM_1'             , self.rawMVAoldDM_1, 'rawMVAoldDM_1/D')
        self.tree.Branch('rawMVAoldDM2017v1_1'       , self.rawMVAoldDM2017v1_1, 'rawMVAoldDM2017v1_1/D')
        self.tree.Branch('rawMVAoldDM2017v2_1'       , self.rawMVAoldDM2017v2_1, 'rawMVAoldDM2017v2_1/D')
        self.tree.Branch('charge_1'                  , self.charge_1, 'charge_1/I')
        self.tree.Branch('decayMode_1'               , self.decayMode_1, 'decayMode_1/I')
        self.tree.Branch('rawAntiEleCat_1'           , self.rawAntiEleCat_1, 'rawAntiEleCat_1/D')
        self.tree.Branch('idAntiEle_1'               , self.idAntiEle_1, 'idAntiEle_1/I')
        self.tree.Branch('idAntiMu_1'                , self.idAntiMu_1, 'idAntiMu_1/I')
        self.tree.Branch('idDecayMode_1'             , self.idDecayMode_1, 'idDecayMode_1/I')
        self.tree.Branch('idDecayModeNewDMs_1'       , self.idDecayModeNewDMs_1, 'idDecayModeNewDMs_1/I')
        self.tree.Branch('idMVAnewDM2017v2_1'        , self.idMVAnewDM2017v2_1, 'idMVAnewDM2017v2_1/I')
        self.tree.Branch('idMVAoldDM_1'              , self.idMVAoldDM_1, 'idMVAoldDM_1/I')
        self.tree.Branch('idMVAoldDM2017v1_1'        , self.idMVAoldDM2017v1_1, 'idMVAoldDM2017v1_1/I')
        self.tree.Branch('idMVAoldDM2017v2_1'        , self.idMVAoldDM2017v2_1, 'idMVAoldDM2017v2_1/I')
        self.tree.Branch('genPartFlav_1'             , self.genPartFlav_1, 'genPartFlav_1/I')
        self.tree.Branch('gendecayMode_1'            , self.gendecayMode_1, 'gendecayMode_1/I')
        self.tree.Branch('genvistaupt_1'             , self.genvistaupt_1, 'genvistaupt_1/D')
        self.tree.Branch('genvistaueta_1'            , self.genvistaueta_1, 'genvistaueta_1/D')
        self.tree.Branch('genvistauphi_1'            , self.genvistauphi_1, 'genvistauphi_1/D')




        ##################
        # tau 2
        ##################

        self.pt_2                       = num.zeros(1, dtype=float)
        self.eta_2                      = num.zeros(1, dtype=float)
        self.phi_2                      = num.zeros(1, dtype=float)
        self.mass_2                     = num.zeros(1, dtype=float)
        self.dxy_2                      = num.zeros(1, dtype=float)
        self.dz_2                       = num.zeros(1, dtype=float)        
        self.leadTkPtOverTauPt_2        = num.zeros(1, dtype=float)
        self.chargedIso_2               = num.zeros(1, dtype=float)
        self.neutralIso_2               = num.zeros(1, dtype=float)
        self.photonsOutsideSignalCone_2 = num.zeros(1, dtype=float)
        self.puCorr_2                   = num.zeros(1, dtype=float)
        self.rawAntiEle_2               = num.zeros(1, dtype=float)
        self.rawIso_2                   = num.zeros(1, dtype=float)
        self.rawMVAnewDM2017v2_2        = num.zeros(1, dtype=float)
        self.rawMVAoldDM_2              = num.zeros(1, dtype=float)
        self.rawMVAoldDM2017v1_2        = num.zeros(1, dtype=float)
        self.rawMVAoldDM2017v2_2        = num.zeros(1, dtype=float)
        self.charge_2                   = num.zeros(1, dtype=int)
        self.decayMode_2                = num.zeros(1, dtype=int)
        self.rawAntiEleCat_2            = num.zeros(1, dtype=float)
        self.idAntiEle_2                = num.zeros(1, dtype=int)
        self.idAntiMu_2                 = num.zeros(1, dtype=int)
        self.idDecayMode_2              = num.zeros(1, dtype=int)
        self.idDecayModeNewDMs_2        = num.zeros(1, dtype=int)
        self.idMVAnewDM2017v2_2         = num.zeros(1, dtype=int)
        self.idMVAoldDM_2               = num.zeros(1, dtype=int)
        self.idMVAoldDM2017v1_2         = num.zeros(1, dtype=int)
        self.idMVAoldDM2017v2_2         = num.zeros(1, dtype=int)
        self.genPartFlav_2              = num.zeros(1, dtype=int)
        self.gendecayMode_2             = num.zeros(1, dtype=int)
        self.genvistaupt_2              = num.zeros(1, dtype=float)
        self.genvistaueta_2             = num.zeros(1, dtype=float)
        self.genvistauphi_2             = num.zeros(1, dtype=float)


        self.tree.Branch('pt_2'                      , self.pt_2, 'pt_2/D')
        self.tree.Branch('eta_2'                     , self.eta_2, 'eta_2/D')
        self.tree.Branch('phi_2'                     , self.phi_2, 'phi_2/D')
        self.tree.Branch('mass_2'                    , self.mass_2, 'mass_2/D')
        self.tree.Branch('dxy_2'                     , self.dxy_2, 'dxy_2/D')
        self.tree.Branch('dz_2'                      , self.dz_2, 'dz_2/D')
        self.tree.Branch('leadTkPtOverTauPt_2'       , self.leadTkPtOverTauPt_2, 'leadTkPtOverTauPt_2/D')
        self.tree.Branch('chargedIso_2'              , self.chargedIso_2, 'chargedIso_2/D')
        self.tree.Branch('neutralIso_2'              , self.neutralIso_2, 'neutralIso_2/D')
        self.tree.Branch('photonsOutsideSignalCone_2', self.photonsOutsideSignalCone_2, 'photonsOutsideSignalCone_2/D')
        self.tree.Branch('puCorr_2'                  , self.puCorr_2, 'puCorr_2/D')
        self.tree.Branch('rawAntiEle_2'              , self.rawAntiEle_2, 'rawAntiEle_2/D')
        self.tree.Branch('rawIso_2'                  , self.rawIso_2, 'rawIso_2/D')
        self.tree.Branch('rawMVAnewDM2017v2_2'       , self.rawMVAnewDM2017v2_2, 'rawMVAnewDM2017v2_2/D')
        self.tree.Branch('rawMVAoldDM_2'             , self.rawMVAoldDM_2, 'rawMVAoldDM_2/D')
        self.tree.Branch('rawMVAoldDM2017v1_2'       , self.rawMVAoldDM2017v1_2, 'rawMVAoldDM2017v1_2/D')
        self.tree.Branch('rawMVAoldDM2017v2_2'       , self.rawMVAoldDM2017v2_2, 'rawMVAoldDM2017v2_2/D')
        self.tree.Branch('charge_2'                  , self.charge_2, 'charge_2/I')
        self.tree.Branch('decayMode_2'               , self.decayMode_2, 'decayMode_2/I')
        self.tree.Branch('rawAntiEleCat_2'           , self.rawAntiEleCat_2, 'rawAntiEleCat_2/D')
        self.tree.Branch('idAntiEle_2'               , self.idAntiEle_2, 'idAntiEle_2/I')
        self.tree.Branch('idAntiMu_2'                , self.idAntiMu_2, 'idAntiMu_2/I')
        self.tree.Branch('idDecayMode_2'             , self.idDecayMode_2, 'idDecayMode_2/I')
        self.tree.Branch('idDecayModeNewDMs_2'       , self.idDecayModeNewDMs_2, 'idDecayModeNewDMs_2/I')
        self.tree.Branch('idMVAnewDM2017v2_2'        , self.idMVAnewDM2017v2_2, 'idMVAnewDM2017v2_2/I')
        self.tree.Branch('idMVAoldDM_2'              , self.idMVAoldDM_2, 'idMVAoldDM_2/I')
        self.tree.Branch('idMVAoldDM2017v1_2'        , self.idMVAoldDM2017v1_2, 'idMVAoldDM2017v1_2/I')
        self.tree.Branch('idMVAoldDM2017v2_2'        , self.idMVAoldDM2017v2_2, 'idMVAoldDM2017v2_2/I')
        self.tree.Branch('genPartFlav_2'             , self.genPartFlav_2, 'genPartFlav_2/I')
        self.tree.Branch('gendecayMode_2'            , self.gendecayMode_2, 'gendecayMode_2/I')
        self.tree.Branch('genvistaupt_2'             , self.genvistaupt_2, 'genvistaupt_2/D')
        self.tree.Branch('genvistaueta_2'            , self.genvistaueta_2, 'genvistaueta_2/D')
        self.tree.Branch('genvistauphi_2'            , self.genvistauphi_2, 'genvistauphi_2/D')




    
#        self.m_taub
#        self.m_taumub
#        self.m_tauj
#        self.m_muj
#        self.m_coll_muj
#        self.m_coll_tauj
#        self.mt_coll_muj
#        self.mt_coll_tauj
#        self.m_max_lj 
#        self.m_max_lb 
#        self.m_mub   
#    

#        self.pzetamiss
#        self.pzetavis 
#        self.pzeta_disc
        






