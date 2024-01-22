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
The histogram of an image is a graph representing the number of pixels in an image as a function of pixel intensity.  It consists of bins, where each bin represents a certain intensity value range.  It is produced by examining all pixels in an image and assigning each pixel to a bin based on pixel intensity.

***Contrast Enchancement***
Contrast Enhancement is a technique that improves how objects are seen in an image by enhancing the brightness difference between the objects and their backgrounds.

***Histogram Equalization***
Histogram Equalization is a technique used to improve the contrast in an image. This is done by spreading out the most frequent pixel intensity values within an image histogram until it achieves a desired histogram.

***Histogram Matching***
Histogram Matching is where an image is transformed such that its histogram matches a specific histogram.  This is achieved by calculating the cumulative distribution functions of the input and target images' histograms, F1 and F2 respectively.  Then for each gray level of the input image, G1, the gray level of the target image G2 is found, such that F1(G1) = F2(G2).  Finally, this leads to the desired result.

***Contrast Stretching***
Contrast Stretching involves improving the contrast of an image by stretching the intensity range to span a desired range of values.

# Task 7

**Frequency Operations**

***The Frequency Domain***
The frequency domain of an image is the space in which the pixel values of an image change within the spatial domain.  The spatial domain is the space where the image pixel values change concerning position.  

***Window Functions***
A window function is a mathematical function that is zero-valued outside of a certain interval.  It can be used to reduce the unwanted high-frequencies in the image Fourier transform.  A Fourier transform represents an image as a combination of various frequencies.

***Frequency Domain Filters***
A frequency domain filter is a filter that is multiplied by the Fourier transform of an image in the frequency domain.  

***Back projection***
Back projection helps with recording how well pixels in an image fit the pixel distribution in a histogram model.

