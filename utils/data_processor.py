import rasterio
import numpy as np
import cv2

def load_and_process_image(file_path):
    """Load and preprocess satellite image"""
    if isinstance(file_path, str):
        with rasterio.open(file_path) as src:
            img = src.read()
    else:
        # Handle uploaded file
        img = rasterio.open(file_path).read()
    
    # Normalize and preprocess
    img = np.moveaxis(img, 0, -1)
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    return img

def calculate_ndvi(image):
    """Calculate NDVI vegetation index"""
    nir = image[:, :, 3].astype(float)
    red = image[:, :, 2].astype(float)
    ndvi = (nir - red) / (nir + red + 1e-6)
    return ndvi