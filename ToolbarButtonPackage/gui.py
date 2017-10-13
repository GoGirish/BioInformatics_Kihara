import os

print (os.getcwd())
import chimera
import ToolbarButtonPackage
chimera.tkgui.app.toolbar.add('ToolbarButton.tiff', ToolbarButtonPackage.mainchain, 'Show Main Chain', None)
