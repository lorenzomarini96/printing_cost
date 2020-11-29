"""Calculate the cost of a black and white print and compare the 
convenience between the cost of a standard copy shop and a home-made
 print with a laser printer."""


import numpy as np
import matplotlib.pyplot as plt
#from Image import PIL 
import cv2 

from skimage.util.dtype import dtype_range
from skimage.util import img_as_ubyte
from skimage import exposure
from skimage.morphology import disk
from skimage.filters import rank


def image_analysis(file_path, toner_cost=None, npage=None, copyshop_cost=None, verbose=True):
    """Function to analyze an image, converting it into a
    two-dimensional array. The mean value of the matrix, 
    that is the mean gray value of the image is then calculated.
    Simple conversions are applied to 
    calculate the cost of any black and white printing.
    
    Parameters
    ----------
    file_path:     path to the file containing the image to be analyzed.
    toner_cost:    int or float. Cost of toner
    npage:         int. Number of printable pages declared with 5% coverage
    copyshop_cost: int or float. cost of a single print at a copy shop

    Returns:
    --------
    print_cost     float. Total cost to print the image.

    Notes
    -----
    Make sure that

    Esamples
    --------

    >>> image_analysis(images_folder/Lena.jpg)
    # Image Information:
    -----------------------------
    Size            = (567, 567)
    Mode            = L
    Format          = JPEG
    Image Shape     = (567, 567)
    Number of pixel = 321489
    -----------------------------
    # Histogram Information:
    -----------------------------
    Counts              321489
    Mean                114.758
    Standard Deviation  55.670
    Mean Error          0.098
    Min                 0.000
    Max                 255.000
    -----------------------------
    # Print Information:
    Page Coverage       54.997%
    Cost of printing    0.175 €

    It's cheaper to go to the copy shop!
    You would save (0.17 - 0.035)€ = 0.14€
    See also
    --------    

    """

    # Get image info.
    #img = cv2.imread(file_path)
    img = plt.imread(file_path)

    # Convert an image to unsigned byte format, with values in [0, 255]
    img = img_as_ubyte(img)
    number_of_pixel = img.shape[0] * img.shape[1]
    # Compute Entries, Mean, Standard Deviation and error on the mean 
    counts = img.shape[0] * img.shape[1]
    mean, std = np.mean(img.ravel()), np.std(img.ravel())
    mean_error = std/np.sqrt(len(img.ravel()))
    min_value = np.min(img)
    max_value = np.max(img)

    if verbose:
        print("----------------------------")
        print("# Image Information:\n")
        #print(f"Size {img.size}")
        #print(f"Mode {img.mode}")
        print(f"Image shape     {img.shape}") # returns a tuple of number of␣ 􏰀→rows, columns and channels
        print(f"Number of pixel {number_of_pixel}")
        print("----------------------------")
        print("# Histogram Information\n")
        print(f"Counts             {counts:12.3f}")
        print(f"Mean               {mean:12.3f}")
        print(f"Standard Deviation {std:12.3f}")
        print(f"Min                {min_value:12.3f}")
        print(f"Max                {max_value:12.3f}")

    # PLOT

    #return total_cost

if __name__ == "__main__":
    image_analysis("images_folder/Lena.jpg")