#---------------------------------------------------------------------------
# Name:        etg/kbdstate.py
# Author:      Robin Dunn
#
# Created:     15-Nov-2010
# Copyright:   (c) 2010 by Total Control Software
# License:     wxWindows License
#---------------------------------------------------------------------------

PACKAGE   = "wx"   
MODULE    = "_core"
NAME      = "kbdstate"   # Base name of the file to generate to for this script
DOCSTRING = ""

# The classes and/or the basename of the Doxygen XML files to be processed by
# this script. 
ITEMS  = [ 'wxKeyboardState' ]    
    
#---------------------------------------------------------------------------
# Parse the XML file(s) building a collection of Extractor objects

import etgtools
import etgtools.tweaker_tools as tools

module = etgtools.ModuleDef(PACKAGE, MODULE, NAME, DOCSTRING)
etgtools.parseDoxyXML(module, ITEMS)

#---------------------------------------------------------------------------
# Tweak the parsed meta objects in the module object as needed for customizing
# the generated code and docstrings.


c = module.find('wxKeyboardState')

c.addProperty("controlDown ControlDown SetControlDown")
c.addProperty("shiftDown   ShiftDown   SetShiftDown")
c.addProperty("altDown     AltDown     SetAltDown")
c.addProperty("metaDown    MetaDown    SetMetaDown")
c.addProperty("cmdDown     CmdDown")


#---------------------------------------------------------------------------
tools.ignoreAssignmentOperators(module)
tools.removeWxPrefixes(module)
#---------------------------------------------------------------------------
# Run the generators

# Create the code generator and make the wrapper code
wg = etgtools.getWrapperGenerator()
wg.generate(module)

# Create a documentation generator and let it do its thing
dg = etgtools.getDocsGenerator()
dg.generate(module)

#---------------------------------------------------------------------------