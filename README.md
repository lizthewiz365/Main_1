# Task 5 

**What are mask filters?**
Mask filters are small images or matrices of k by k elements, which are used to smoothen or sharpen an image.  They are rotated through 180 degrees and moved in a raster pattern across an input image of M by M pixels.  An equation for calculating an image with a mask filter can be show below:
G = F * H

where G is the output image, F is the input image, and H is the mask filter applied to the input image.

**What do mask filters do?**
Mask filters are used to smoothen or sharpen an image.

**What are non-linear filters?**
Non-linear filters are mask filters that smooth noise but don't blur the edges of an image.  An example of a non-linear filter is a median filter, which returns the median of pixels in it.  This filter uses the median value to reduce local fluctuations among the pixel values of an image, smoothening the image. 

**What is a Laplacian filter?**
A Laplacian filter is a combination of the second derivatives in the x and y directions of an image.  

**What does a Laplacian filter do?**
A Laplacian filter computes the second derivatives of an image, measuring the rate of change of the first derivatives.  It determines the change in nearby pixel values due to edge or continuous progression.  This allows for the edges of an image to be detected.

# Task 6

**What is the frequency domain of an image?**
The frequency domain of an image is the space in which the pixel values of an image change within the spatial domain.  The spatial domain is the space where the image pixel values change concerning position.  

**What is the histogram of an image?**


