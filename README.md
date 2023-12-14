# Keypoint Localization using SIFT

![Project Image](link/to/your/project/image.png)

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Algorithm Overview](#algorithm-overview)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains the **MANUAL** pythonic implementation of the Scale-Invariant Feature Transform (SIFT) algorithm using basic Python packages for computer vision applications. SIFT is a powerful algorithm for detecting and describing local features in images, known for its robustness to various transformations. 

The purpose of this project is to understand the logic that enables the SIFT algorithm to produce highly reliable keypoints for image processing applications. This project is a step-by-step implementation of the work of [Lowe, 2004](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf), covering the topic of keypoint localization.

## Prerequisites

Before you begin, ensure you have the following requirements installed:

- Python 3.x
- NumPy
- OpenCV (cv2)

## Usage

Open the **keypoint-localization.ipynb** to view the manual pythonic implementation of the SIFT algorithm for keypoint localization.

If you wish to use SIFT for your own project, [OpenCV](https://opencv.org/) offers easy-to-use modules for implementing SIFT in 1-2 lines of code, but if you wish to (more easily) implement the exact steps I did in the notebook, you may refer to the **keypoint-localization-modularized.ipynb**.

## Algorithm Overview

The SIFT algorithm implemented in this project follows these main steps:

1. **Image Preprocessing:** Convert the image to grayscale.
2. **Image Pyramid:** Generate Image Pyramid by applying the Gaussian function of different intensities, across different image scales (octaves).
3. **Difference of Gaussian:** Compute the difference between two consecutive images within the same octave.
4. **Extrema Detection:** Identify extrema within a 3x3x3 cube of pixels around a point of interest.
5. **Filter Weak Keypoints:** Filter weak keypoints using Harris corner detection.

For detailed information on the SIFT algorithm, refer to [SIFT Algorithm](https://link-to-sift-algorithm-paper).

You may also read our own paper [](Image-Stitching.pdf) where we used the output of this keypoint localization project for Image Stitching.

## Results

![Detected Keypoints](/figures/detected_keypoints_filtered.png)

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. 

## License
This project is licensed under the MIT License.
