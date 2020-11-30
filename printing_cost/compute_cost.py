"""Calculate the cost of a black and white print and compare the 
convenience between the cost of a standard copy shop and a home-made
 print with a laser printer."""

import numpy as np
import matplotlib.pyplot as plt
from skimage.util import img_as_ubyte


def image_analysis(file_path, toner_cost=0., toner_npage=0,
                  stack_paper_cost=0., stack_npage=0,
                  copyshop_cost=0., verbose=True):
    """Function to analyze an image, converting it into a
    two-dimensional array. The mean value of the matrix, 
    that is the mean gray value of the image is then calculated.
    Simple conversions are applied to 
    calculate the cost of any black and white printing.
    
    Parameters
    ----------
    file_path :       path to the file containing the image to be analyzed.
    toner_cost :      int or float. Cost of toner
    npage :         int. Number of printable pages declared with 5% coverage
    stack_paper_cost : 0., 
    stack_npage : 0
    copyshop_cost : int or float. cost of a single print at a copy shop
    verbose :   

    Returns:
    --------
    None

    Notes
    -----
    Make sure that

    Esamples
    --------

    >>> image_analysis(file_path="images_folder/Lena.jpg",
                    toner_cost=15.0,toner_npage=1000,stack_paper_cost=5.0,
                    stack_npage=500, copyshop_cost=0.035, verbose=True) 
    -------------------------------------------
    # Image Information:
    Image shape        (567, 567)
    Number of pixel    321489
    -------------------------------------------
    # Histogram Information
    Counts                   321489
    Mean                    114.758
    Standard Deviation       55.670
    Min                       0.000
    Max                     255.000
    -------------------------------------
    # Print Information
    Gray cover of the image 54.997 %
    -------------------------------------------
    # Cost Information
    Cost of a single page (paper)      0.010 €
    Ink cost for one print             0.165 €
    Total cost for one print           0.175 €
    -------------------------------------------
    Cheaper to print at the shop!
    Saving money: 0.175 € - 0.035 €: 0.140 €
    It's cheaper to go to the copy shop!
    You would save (0.17 - 0.035)€ = 0.14€

    See also
    --------    

    """

    # Get image info.
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
    
    # Compute coverage of print [%]
    page_cover = (1 - mean/255) * 100
    # Paper: compute cost of a single page [€]
    single_page_cost = stack_paper_cost / stack_npage 
    # Toner: compute ink cost for one print [€]
    single_ink_cost = toner_cost / toner_npage * page_cover/5.0 # Estimated value provided that the coverage of each print is 5%
    # Compute total
    total_cost = single_page_cost + single_ink_cost

    if verbose:
        print("-------------------------------------------\n")
        print("# Image Information:\n")
        print(f"Image shape        {img.shape}") # returns a tuple of number of rows, columns and channels
        print(f"Number of pixel    {number_of_pixel}")
        print("-------------------------------------------\n")
        print("# Histogram Information\n")
        print(f"Counts             {counts:12}")
        print(f"Mean               {mean:12.3f}")
        print(f"Standard Deviation {std:12.3f}")
        print(f"Min                {min_value:12.3f}")
        print(f"Max                {max_value:12.3f}")
        print("-------------------------------------")
        print("# Print Information\n")
        print(f"Gray cover of the image {page_cover:5.3f} %")
        print("-------------------------------------------\n")
        print("# Cost Information\n")
        print(f"Cost of a single page (paper) {single_page_cost:10.3f} €")
        print(f"Ink cost for one print        {single_ink_cost:10.3f} €")
        print(f"Total cost for one print      {total_cost:10.3f} €")
        print("-------------------------------------------\n")

    if total_cost < copyshop_cost:
        print("Cheaper to print at home!")
        print(f"Saving money: {copyshop_cost:.3f} € - {total_cost:.3f} €: {copyshop_cost - total_cost} €")
    else:
        print("Cheaper to print at the shop!")
        print(f"Saving money: {total_cost:.3f} € - {copyshop_cost:.3f} €: {total_cost - copyshop_cost:.3f} €")


    # PLOT
    plt.figure(1, figsize=((8,6)))
    plt.imshow(img, cmap='gray', interpolation='none')
    plt.title("Image")

    plt.figure(2, figsize=(10,6))
    plt.title("Histogram")
    bin_heights, bin_borders, _ = plt.hist(img.ravel(), bins=256, alpha=1.0, density=False)
    bin_centers = 0.5 * (bin_borders[1:] + bin_borders[:-1])
    plt.minorticks_on()
    plt.xlabel("Gray Scale Level - Pixel Intensity")
    plt.ylabel("Number of pixel with such intensity level")
    
    #fig, ax = plt.subplots(1,2, figsize=(8,6), gridspec_kw={'width_ratios': [2, 2]})
    fig, ax = plt.subplots(ncols=2, figsize=(8, 6))
    ax = ax.ravel()
    ax[0].imshow(img, cmap='gray', interpolation='none')
    ax[0].set_title("Image")
    bin_heights, bin_borders, _ = ax[1].hist(img.ravel(), bins=256, alpha=1.0, density=False)
    ax[1].minorticks_on()
    ax[1].set_xlabel("Gray Scale Level - Pixel Intensity")
    ax[1].set_ylabel("Number of pixel with such intensity level")
    ax[1].axvline(x=mean, color='r', linestyle='dashed', linewidth=2)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    image_analysis(file_path="images_folder/Lena.jpg",
                    toner_cost=15.0,toner_npage=1000,stack_paper_cost=5.0,
                    stack_npage=500, copyshop_cost=0.035, verbose=True) 