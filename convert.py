#!/Applications/FreeCAD.app/Contents/bin/FreeCADCmd
"""
This is a convertor script which calls FreeCADCmd directly.
It would also be possible to call it in an external Python session. Didn't try it.

2017
Xaratustrah

"""

import FreeCAD
import Mesh
import Part
import sys

filename = sys.argv[1]
print('Converting {}...'.format(filename))
p = Part.read(sys.argv[1])
p.exportStep('{}'.format(filename))
print('The End')