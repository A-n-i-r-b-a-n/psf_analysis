# Introduction

This is a small project that does a psf analysis of the Nancy Grace Roman 
Space Telescope, and determines its diffraction pattern.

To obtain this repository run the following command on a terminal (Powershell for windows)
```bash
git clone https://github.com/A-n-i-r-b-a-n/psf_analysis.git

```

# Installation and use 
The use of this project requires Jupyter notebook and python installed in 
user's system. 
## Install jupyter notebook
On a preferred code editor like VS code, install the jupyter notebook extension. 

## Create a virtual environment
Open a terminal and run the following commands (for windows open Powershell)

```bash
cd psf_analysis
python -m venv env

```
Note: Instead of "env" you can use any environment name of your choice.

If windows does not recognise "python" as a command try the following:

```bash
py -m venv env

```

## Installing the required python packages
From the project directory whre the virtual environment was created activate the
python environment.

For MacOs and Linux, open a terminal and run;

```bash
source env/bin/activate
python -m pip install -r requirements.txt

```
Note: instead of "env" you need to use the name of your virtual environment. 

For windows, open Powershell and run the following commands:

```bash
.\env\Scripts\Activate.ps1
py -m pip install -r requirements.txt

```

## The notebook

Open the notebook (.ipynb) file. Select the virtual environment you created as the jupyter kernel to run the notebook file. Run all the cells, generate your own star field and generate your own simulated JWST and Roman space telescope images. The notebook 
contains all the necessary instructions.


# The image_convert.py file

There is no need to alter or run this file, this file is only there to create the 
gray-scale binary image of the Roman space telescope aperture, as the code main code
relies on binary grayscale aperture image to extract the aperture functuion. The binary image is already available on the resources folder, therefore running this python file is not required.

