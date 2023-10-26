import cv2

def quick_resize(img, scale_percent):
    
    # scale_percent - percent of the original image's scale
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    return resized

def is_center_pixel_extremum(pixel_value, top_layer, curr_layer, next_layer):
    
    """
    Checks whether the point of interest / pixel is the extremum (local max or local min) within the provided region of interest
    
    args:
    pixel_value - value of the pixel in the point of interest
    top_layer, curr_layer, next_layer - region of interest (list)
    
    """
    
    # Concatenate individual regions
    region_of_interest = top_layer + curr_layer + next_layer

    # Flatten region of interest
    region_of_interest_flatten = [item for sublist in region_of_interest for item in sublist]

    # Check for extremum case
    is_extremum = any(pixel_value == [max(region_of_interest_flatten), min(region_of_interest_flatten)]) and (sum(pixel_value == region_of_interest_flatten) == 1)
    
    return is_extremum