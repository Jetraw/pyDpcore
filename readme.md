# pyDpcore, the python module for Dpcore

This is a Python module to Dpcore prepare images in order to be compressed with JetRaw afterwards. For more info visit
https://www.dotphoton.com/


## Requirements
- Jetraw/Dpcore installed on a Windows computer.
- Camera calibration file. 

## Installation
First download the WHL file from [latest release](https://github.com/Jetraw/pyDpcore/releases/latest), or browse [previous releases](https://github.com/Jetraw/pyDpcore/releases). 
Once the WHL file is downloaded in order to install pyJetraw run the following command:

```python
pip install DPCore-x.y.z-py3-none-any.whl
```

## Usage
Here are some code snippets of how the module would typically be used.

```python
import dpcore

# Read Input Image (non-prepared)
image = tifffile.imread("input_filename.tif")
# Load calibration file
dpcore.load_parameters("path_to_calibration_file\\calibration.dat")
# Prepare image buffer with dpcore
for page in range(image.shape[0]):
    dpcore.prepare_image(image[page], "calibration_identifier")
# Save dpcore prepared image using tiffile
tifffile.imsave(output_filename, data=image.astype(np.uint16))
```

You will also find an example_script.py inside the example folder with a test calibration file (.dat). 

## Contact

If you have any request or doubt please do not hesitate to contact us to:
https://dotphoton.com/contact
