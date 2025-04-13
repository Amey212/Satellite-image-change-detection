import numpy as np
from PIL import Image
import cv2

def load_image(image_path):
    """
    Load an image from the specified path and convert it to a numpy array.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        numpy.ndarray: Image as a numpy array in RGB format
    """
    try:
        # Read image using PIL
        image = Image.open(image_path)
        
        # Convert to RGB if image is in a different mode
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        # Convert to numpy array
        image_array = np.array(image)
        
        return image_array
    except Exception as e:
        raise Exception(f"Error loading image from {image_path}: {str(e)}")