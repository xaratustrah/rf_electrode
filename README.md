# A parametric RF electrode

This script uses [solidpython](https://github.com/SolidCode/SolidPython) and [OpenSCAD](http://www.openscad.org/) to 
create a fully parametric model of an rf electrode,
based on the following paper:

F. Caspers, CERN-ATS-Note-2011-075 TECH, [http://cds.cern.ch/record/1380889](http://cds.cern.ch/record/1380889).

Basically it is possible to export this in [STL format](https://en.wikipedia.org/wiki/STL_(file_format)) and import it
directly to to your favourite electromagnetic calculator. The second possibility is to export to CSG format in OpenSCAD then convert it to [STEP](https://de.wikipedia.org/wiki/Standard_for_the_exchange_of_product_model_data) using [FreeCAD](https://en.wikipedia.org/wiki/FreeCAD).

I have tested both methods and finally imported them into [CST Studio Suite<sup>&reg;</sup>](https://www.cst.com/). The import handles both STL and STEP very well, whereas the curves are much better represented in case of STEP file import.


![rf_electrode](https://raw.githubusercontent.com/xaratustrah/rf_electrode/master/rf_electrode.png)

