#! /usr/bin/env python

import time
start = time.time()
import os, sys #, ROOT
from ROOT import TFile, TTree, TObject
from math import log, pow, floor

import optparse

parser = optparse.OptionParser()

parser.add_option('-c', '--channel', action="store", type="string", default="tautau", dest='channel')
parser.add_option('-f', '--filename', action="store", type="string", default=None, dest='filename')

(options, args) = parser.parse_args() 



# https://root.cern.ch/root/html/tutorials/tree/copytree.C.html
# https://root.cern.ch/root/html/tutorials/tree/copytree3.C.html
# to get branch channel with string "channel": getattr(oldtree,"channel")


verbosity   = 0

channel = options.channel

channels  = []

channels.append(channel)


selection = '1'

if options.channel=='tautau':
    selection = 'idDecayMode_1==1 && idDecayMode_2==1 && idMVAoldDM2017v2_1 >= 3 && idMVAoldDM2017v2_2 >= 3'

elif options.channel=='mutau':
    selection = 'idDecayMode_2==1 && idMVAoldDM2017v2_2 >= 3 && pfRelIso04_all_1 < 0.1'


print '============================='
print 'channel = ', channel
print 'filename = ', options.filename
print 'skim selection = ', selection
print '============================='


    ###########
    # cutTree #
    ###########

def cutTree(oldfilename, treenames, **kwargs):
    """Extract tree from file and save in new one."""
    start_here  = time.time()
    verbosity   = kwargs.get('verbosity',0)
        
    # TREENAME
    treename = ""
    if isinstance(treenames,str): treenames = [treenames]
    if len(treenames) == 1:       treename  = "_%s"%treenames[0]
    print ">>> extracting tree(s) from file"
    N           = kwargs.get('N',-1)
    
    # CUTS
    cuts        = kwargs.get('cuts',"channel>0")
    if isinstance(cuts,str):      cuts = [cuts]*len(treenames)
    if len(treenames)!=len(cuts): print warning("cutTree: len(treenames)!=len(cuts)")
    
    # FILE OPTIONS
    newfilename = kwargs.get('newfilename',False)
    update      = kwargs.get('update',False)
    if not newfilename:
        if update: newfilename = oldfilename
        else:      newfilename = oldfilename.replace(".root","%s_string.root"%(treename))
    copycontents = kwargs.get('copycontents',False) and oldfilename!=newfilename # copy all contents of oldfile to newfile
    option      = 'read' if copycontents else ('update' if update else 'recreate')
    option      = kwargs.get('option',option)
    label       = kwargs.get('label',"_cut" if (oldfilename==newfilename) else "")
    
    # FILE
    oldfile     = TFile(oldfilename)
    if copycontents: succes = oldfile.Cp(newfilename,True)
    newfile     = TFile(newfilename,'update')
    
    # PRINT
    printVerbose(">>>   file in:    \"%s\"" % (oldfilename),verbosity)
    printVerbose(">>>   file out:   \"%s\"" % (newfilename),verbosity)
    printVerbose(">>>   tree label: \"%s\"" % (label),verbosity)
    printVerbose(">>>   settings:   update=%s, option=\"%s\", copycontents=%s" % (update,option,copycontents),verbosity)
    
    for treename, cut in zip(treenames,cuts):
        oldtree     = oldfile.Get(treename)
        newtreename = treename+label

#        if treename != newtreename and oldfile.Get(newtreename):
#            print warning("There already exists a tree of name \"%s\" => ignoring" % (newtreename),prepend="  ")
#            continue

        if verbosity>0:
            print ">>>   copying tree \"%s\" into \"%s\" with cuts" % (treename,newtreename)
            print ">>>     \"%s\"" % (cut),verbosity
        else: print ">>>   copying tree \"%s\" into \"%s\"" % (treename,newtreename)
        newtree     = None
        maxmessage  = ""
        if N>0:
            newtree    = oldtree.CopyTree(cut,"",N)
            maxmessage = " (max %i)"%N
        else:
            newtree = oldtree.CopyTree(cut)
        #newtree.SetName(newtreename)
        newtree.Write(newtreename,TObject.kOverwrite)
        print ">>>   extraction done: %i%s of %i entries copied" % (newtree.GetEntries(),maxmessage,oldtree.GetEntries())
    
    print ">>>   writing and closing new file: %s" % (newfilename)  
    #newfile.Write(TObject.kOverwrite)
    newfile.Close()
    oldfile.Close()
    
    print ">>> took %.2f seconds." % (time.time()-start_here)
    print ">>> "





    ########
    # main #
    ########

def main():
    """Main method: list files and which trees to extract."""
    
    # FILES
    files = [options.filename]
    
    # CHANNEL & TREENAMES
#    treenames = ["tree_%s"%c for c in channels]
    treenames = ["tree"]
    
    
    nFiles    = len(files)
    Nmax      = -1 #000000
    #cuts      = "channel>0 && abs(eta_1)<2.1 && %s && %s" % (isocuts,vetos)
    cuts      = selection # "channel>0 && abs(eta_1)<2.1 && %s && %s" % (isocuts_relaxed,vetos) # RELAXED #triggers
    #OUTDIR    = "%s/trimmed"%DIR; ensureDirectory(OUTDIR)
    for i, sample in enumerate(files):
        print ">>> %i/%i files: %s"%(i+1,nFiles,sample)
#        oldfilename = "%s/%s" % (DIR,sample)
        oldfilename = "%s" % (sample)

        if os.path.isfile(oldfilename):
            cutTree(oldfilename,treenames,cuts=cuts,update=True,verbosity=verbosity,label="_cut_relaxed")
        else:
            print warning("%s Does not exist!"%oldfilename)

    



    ##################
    # Help functions #
    ##################

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR

def color(string,**kwargs):
    """Color"""
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    text_color_dict = { "black"     : "0;30;",  "red"       : "1;31;",
                        "green"     : "0;32;",  "yellow"    : "1;33;", "orange"    : "1;33;",
                        "blue"      : "1;34;",  "purple"    : "0;35;",
                        "magenta"   : "1;36;",  "grey"      : "0;37;",  }
    background_color_dict = {   "black"     : "40", "red"       : "41",
                                "green"     : "42", "yellow"    : "43", "orange"    : "43",
                                "blue"      : "44", "purple"    : "45",
                                "magenta"   : "46", "grey"      : "47", }                  
    color_code = text_color_dict[kwargs.get('color',"red")] + background_color_dict[kwargs.get('background',"black")]
    return kwargs.get('prepend',"") + "\x1b[%sm%s\033[0m" % ( color_code, string )

def warning(string,**kwargs):
    return color("Warning! "+string, color="yellow", prepend=">>> "+kwargs.get('prepend',""))
    

def printVerbose(string,verbosity,**kwargs):
    """Print string if verbosity is true or verbosity int is lager than given level."""
    level = kwargs.get('level',False)
    if level:
        if verbosity>=level: print string
    elif verbosity: print string



if __name__ == '__main__':
    print
    main()
    end = time.time()
    print ">>>\n>>> done in %.2f seconds\n" % (end-start)
