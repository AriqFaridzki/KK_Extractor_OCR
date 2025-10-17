import cv2
import numpy as np

# --- 1. SKEW CORRECTION (The most complex, but critical step) ---
# Skew correction must be done before simple thresholding for best results.
def deskew(image):
    """Corrects the rotation (skew) of the image using the minimum bounding box method."""
    
    # 1. Convert to grayscale and apply an inverse binary threshold (text: white, background: black)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use GaussianBlur to reduce noise before thresholding
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    
    # Use Otsu's method to automatically find the best threshold, inverting colors
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # 2. Find coordinates of all foreground (white) pixels
    coords = np.column_stack(np.where(thresh > 0))
    
    # 3. Compute the minimum area bounding box
    angle = cv2.minAreaRect(coords)[-1]

    # 4. Correct the angle value (cv2.minAreaRect returns angle in [-90, 0) range)
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    # 5. Rotate the image to correct the skew
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Use INTER_CUBIC for higher quality rotation
    # BORDER_REPLICATE fills the new edges with replicated border pixels (prevents black borders)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    print(f"[INFO] Detected Skew Angle: {angle:.2f} degrees")
    return rotated

# --- 2. NOISE REMOVAL AND SCALING ---
def scale_and_denoise(image):
    """Scales up the image for better small-text recognition and removes noise."""
    
    # Tesseract generally performs better on images > 300 DPI. Scaling up is a simple fix.
    # Scale factor (e.g., 1.5x original size)
    scale_factor = 1.5 
    
    resized = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
    
    # Use a median filter to remove 'salt-and-pepper' noise (small dots/smudges)
    # Kernel size 3 or 5 is generally good for documents.
    denoised = cv2.medianBlur(resized, 3) 
    
    return denoised

# --- 3. FINAL BINARIZATION (Grayscale and Thresholding) ---
def binarize(image):
    """Converts image to final black-and-white for Tesseract."""
    
    # 1. Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2. Adaptive Thresholding
    # This is often better than Otsu/simple thresholding for photocopies with uneven lighting.
    # ADAPTIVE_THRESH_GAUSSIAN_C calculates a different threshold for small regions (15x15 block)
    # The C value (2 in this case) is subtracted from the mean to fine-tune the threshold.
    binary = cv2.adaptiveThreshold(
        gray, 
        255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 
        15, # Block size
        2   # C value
    )
    
    # Invert colors so text is BLACK and background is WHITE (often preferred by Tesseract)
    # If using cv2.THRESH_BINARY_INV, this is not needed. With THRESH_BINARY, you may need it.
    # Check your image result; if text is white, uncomment the line below.
    # binary = cv2.bitwise_not(binary) 
    
    return binary

# =========================================================
# MAIN PROCESSING PIPELINE
# =========================================================
def preprocess_kartu_keluarga(image_path):
    """Loads image and applies the full preprocessing pipeline."""
    
    # 1. Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return None
    
    # 2. Deskew the original color image
    # straight_img = deskew(img)
    
    # 3. Scale and Denoise the straightened image
    # clean_img = scale_and_denoise(img)
    
    # 4. Convert to final black and white image
    # final_binary_img = binarize(clean_img)
    imS = cv2.resize(img, (960, 540))     
    return imS

processedImage = preprocess_kartu_keluarga('KK/halaman_1_kk.png')
# Example Usage:
# processed_image = preprocess_kartu_keluarga('path/to/your/kartu_keluarga.jpg')
# if processed_image is not None:
#     # Save the preprocessed image
#     cv2.imwrite('processed_kk.png', processed_image) 
    
#     # Then pass 'processed_kk.png' to Tesseract for OCR
#     # text = pytesseract.image_to_string(processed_image) 
#     # print(text)

cv2.imshow("Test window", processedImage)
# cv2.imshow("Publish Date", box_additional_info)
cv2.waitKey(0)
cv2.destroyAllWindows()
