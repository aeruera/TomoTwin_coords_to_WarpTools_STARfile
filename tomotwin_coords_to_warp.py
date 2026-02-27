#!/usr/bin/env python.starfile

#Important note: Make sure the .coords files in the /coords/ folder are named after the tomogram.


import numpy as np
import pandas as pd
import starfile
from pathlib import Path

# === User parameters ===
input_dir = Path("coords/")           # where your .coords files live
output_dir = Path("output_stars/")  # where to save .star files
output_dir.mkdir(exist_ok=True)

# tomogram dimensions in pixels (unbinned)
tomo_x = 4400
tomo_y = 4400
tomo_z = 1200


# Pixel size info for scaling (TomoTwin picks on tomograms with pixel size 10)
apix = 1.56                # physical pixel size of dataset
apix_match_template = 10.0 # pixel size of TomoTwin tomogram
scale = apix_match_template / apix 

# === Main processing ===
for coords_file in sorted(input_dir.glob("*.coords")):
    tomo_name = coords_file.stem        # e.g. myTomo.coords → myTomo
    print(f"Processing {tomo_name} ...")

    # Load coordinates (assume 3 columns: x, y, z in pixels)
    coords = np.loadtxt(coords_file)

    # Ensure 2D array
    coords = np.atleast_2d(coords)

    # Convert to fractional (0–1) from bottom-left corner
    frac_x = coords[:, 0] * scale / tomo_x
    frac_y = coords[:, 1] * scale / tomo_y
    frac_z = coords[:, 2] * scale / tomo_z

    # Build DataFrame for starfile
    df = pd.DataFrame({
        "rlnCoordinateX": frac_x,
        "rlnCoordinateY": frac_y,
        "rlnCoordinateZ": frac_z,
        "rlnAngleRot": 0.0,
        "rlnAngleTilt": 0.0,
        "rlnAnglePsi": 0.0,
        "rlnMicrographName": f"{tomo_name}.tomostar",
        "rlnAutopickFigureOfMerit": 0.0
    })

    # Write the star file
    star = {"particles": df}
    out_path = output_dir / f"{tomo_name}_fractional.star"
    starfile.write(star, out_path, overwrite=True)
    print(f"  → wrote {out_path}")

print("✅ All done.")
