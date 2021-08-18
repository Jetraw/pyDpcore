# pyDpcore, the Python Module for Dpcore
This is the Dpcore Python Module which offers the option to dpcore prepare images, allowing to use Jetraw's compression afterwards. For more info visit https://www.dotphoton.com/

## Requirements
- Jetraw/Dpcore installed on a Windows computer.<br/>
*Note:* if you do not have Jetraw installed visit https://www.jetraw.com/downloads/software and for usage information https://github.com/Jetraw/Jetraw
- Camera calibration file. 

## Installation Windows
First download the WHL file from [latest (pre-)release](https://github.com/Jetraw/pyDpcore/releases/download/21.06.23.1/DPCore-0.9.0-py3-none-any.whl), or browse [previous (pre-)releases](https://github.com/Jetraw/pyDpcore/releases). 
Once the WHL file is downloaded in order to install pyJetraw run the following command:

```python
pip install DPCore-x.y.z-py3-none-any.whl
```

## Installation Linux
The WHL file needs to be installed like in the previous section but an extra step is necessary. 

You need to add to the LD_LIBRARY_PATH variable the dpcore and jetraw libraries location so pyDpcore is able to find them:

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path_to_jetraw_folder/lib/
```

It is recommended to **add this instruction in your bashrc (/home/user/.bashrc)** file, then everytime a bash environment is created everything is set up to use pyDpcore. Remember that if you are using an IDE to run python, you will need to launch it from the Terminal. If not the enviroment will not be correctly configured.  

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

You will also find an example_script.py inside the example folder with a calibration file (.dat). 

## Contact
Feel free to use the [issues section](https://github.com/Jetraw/pyDpcore/issues) to report bugs or request new features. You can also ask questions and give comments by visiting the [discussions](https://github.com/Jetraw/pyDpcore/discussions), or following the contact information at https://jetraw.com.
