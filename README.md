# TomoTwin_coords_to_WarpTools_STARfile
TomoTwin is a particle picking software tool used in cryoET. At the end of a TomoTwin pipeline, a .coords coordinate file is produced which is not in a compatible format for exporting particles from WarpTools. This script will convert the .coords file produced from TomoTwin to a WarpTools 3 dev36-compatible STAR file.

The converted WarpTools coordinates are in fractional normalized coordinate format (meaning from 0 to 1, rather than in angstroms or pixels) with the origin of the coordinate system being considered the bottom left-hand corner of the tomogram.

Useage:

1. First, acquire the .coords coordinate file from TomoTwin by running whichever TomoTwin pipeline you like. The coordinates will be nested into a folder called /coord/ inside your current working directory. Check they are truly there with `ls /coords/`. 

2. Rename the .coords file in the /coords/ directory after the tomogram name. For example, if your tomogram is called l40t05_5.mrc, rename cluster.coords to l40t05_5.coords.
   
3. Run tomotwin_coords_to_warp.py in the working directory by typing `python3 tomotwin_coords_to_warp.py`. 
