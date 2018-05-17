import ROOT
import math 
import numpy as num 

from TreeProducerCommon import *

class TreeProducerMuMu(TreeProducerCommon):

    def __init__(self, name):

        super(TreeProducerMuMu, self).__init__(name)
        
        print 'TreeProducerMuMu is called', name


        # trees
        ##################
        # muon
        ##################

        self.pt_1                       = num.zeros(1, dtype=float)
        self.eta_1                      = num.zeros(1, dtype=float)
        self.phi_1                      = num.zeros(1, dtype=float)
        self.mass_1                     = num.zeros(1, dtype=float)
        self.dxy_1                      = num.zeros(1, dtype=float)
        self.dz_1                       = num.zeros(1, dtype=float)        
        self.pfRelIso04_all_1           = num.zeros(1, dtype=float)
        self.q_1                        = num.zeros(1, dtype=int)
        self.genPartFlav_1              = num.zeros(1, dtype=int)

        self.tree.Branch('pt_1'                      , self.pt_1, 'pt_1/D')
        self.tree.Branch('eta_1'                     , self.eta_1, 'eta_1/D')
        self.tree.Branch('phi_1'                     , self.phi_1, 'phi_1/D')
        self.tree.Branch('mass_1'                    , self.mass_1, 'mass_1/D')
        self.tree.Branch('dxy_1'                     , self.dxy_1, 'dxy_1/D')
        self.tree.Branch('dz_1'                      , self.dz_1, 'dz_1/D')
        self.tree.Branch('q_1'                       , self.q_1, 'q_1/I')
        self.tree.Branch('pfRelIso04_all_1'          , self.pfRelIso04_all_1, 'pfRelIso04_all_1/D')
        self.tree.Branch('genPartFlav_1'             , self.genPartFlav_1, 'genPartFlav_1/I')

        ##################
        # muon 2
        ##################

        self.pt_2                       = num.zeros(1, dtype=float)
        self.eta_2                      = num.zeros(1, dtype=float)
        self.phi_2                      = num.zeros(1, dtype=float)
        self.mass_2                     = num.zeros(1, dtype=float)
        self.dxy_2                      = num.zeros(1, dtype=float)
        self.dz_2                       = num.zeros(1, dtype=float)        
        self.pfRelIso04_all_2           = num.zeros(1, dtype=float)
        self.q_2                        = num.zeros(1, dtype=int)
        self.genPartFlav_2              = num.zeros(1, dtype=int)

        self.tree.Branch('pt_2'                      , self.pt_2, 'pt_2/D')
        self.tree.Branch('eta_2'                     , self.eta_2, 'eta_2/D')
        self.tree.Branch('phi_2'                     , self.phi_2, 'phi_2/D')
        self.tree.Branch('mass_2'                    , self.mass_2, 'mass_2/D')
        self.tree.Branch('dxy_2'                     , self.dxy_2, 'dxy_2/D')
        self.tree.Branch('dz_2'                      , self.dz_2, 'dz_2/D')
        self.tree.Branch('q_2'                       , self.q_2, 'q_2/I')
        self.tree.Branch('pfRelIso04_all_2'          , self.pfRelIso04_all_2, 'pfRelIso04_all_2/D')
        self.tree.Branch('genPartFlav_2'             , self.genPartFlav_2, 'genPartFlav_2/I')

