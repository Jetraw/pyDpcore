import os
import numpy as np
import dpcore
import pathlib
import tifffile


def prepare_image_tif(input_filename, output_filename):
    # Read Input Image (non-prepared)
    image = tifffile.imread(input_filename)
    # Load calibration file
    dpcore.load_parameters(str(pathlib.Path(__file__).parent.joinpath("test\\pco_3a2dd3a.dat")))
    # Prepare image buffer with dpcore
    dpcore.prepare_image(image, "PCO_3A2DD3A")
    # Save dpcore prepared image using tiffile
    tifffile.imsave(output_filename, data=image.astype(np.uint16))


def process_dir(sourcedir, destdir):
    assert os.path.isdir(sourcedir), "Source directory does not exist."
    prepared_dir = os.path.join(destdir, "prepared_tif")
    os.makedirs(prepared_dir, exist_ok=True)
    for root, dirs, files in os.walk(sourcedir):
        if (root == sourcedir):
            tiffs = [f for f in files if not f.startswith(".")
                     and f.rpartition(".")[2].lower() == "tif"]
            if len(tiffs) == 0:
                print("  -- Nothing to do. --")
                continue
            for tif in tiffs:
                prepare_image_tif(os.path.join(sourcedir, tif), os.path.join(prepared_dir, tif))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--srcdir", help="Directory containing input TIF files.")
    parser.add_argument("-d", "--destdir", help="Directory for output files. Defaults to srcdir.")

    args = parser.parse_args()
    if args.destdir is None:
        args.destdir = args.srcdir

    process_dir(args.srcdir, args.destdir)
