# Arrow-Detection
Submission for the Arrow Detection Mini project for Anveshak Software Module

The solution employs multiscale template matching. The input image is rescaled to multiple sizes and a correlation value is obtained between the scaled input image and a known image of a right arrow.
The process is repeated for an image of a left arrow.
Finally the input image is labelled accorrding to the highest correlation value.
