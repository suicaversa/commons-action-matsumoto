#!/usr/bin/env python3
"""
Create a horizontal OGP image from the vertical logo image.
This script converts the vertical logo to a 1200x630 horizontal format suitable for social media.
"""

try:
    from PIL import Image, ImageDraw
    
    # Open the original vertical image
    original = Image.open("/tmp/github-images/image-1754609896104-0.png")
    
    # Create a new image with OGP dimensions (1200x630)
    ogp_width, ogp_height = 1200, 630
    ogp_image = Image.new('RGB', (ogp_width, ogp_height), color='#f5f5f5')  # Light gray background
    
    # Calculate scaling to fit the logo nicely in the horizontal space
    # We want to scale the image to fit within a reasonable portion of the OGP image
    max_logo_height = int(ogp_height * 0.8)  # Use 80% of height
    scale = min(max_logo_height / original.height, 1.0)
    
    # Resize the original image
    new_width = int(original.width * scale)
    new_height = int(original.height * scale)
    resized_logo = original.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Center the logo in the OGP image
    x_offset = (ogp_width - new_width) // 2
    y_offset = (ogp_height - new_height) // 2
    
    # Paste the logo onto the OGP image
    if resized_logo.mode == 'RGBA':
        ogp_image.paste(resized_logo, (x_offset, y_offset), resized_logo)
    else:
        ogp_image.paste(resized_logo, (x_offset, y_offset))
    
    # Save the result
    ogp_image.save("/home/runner/work/commons-action-matsumoto/commons-action-matsumoto/assets/ogp-image.png", "PNG")
    print("OGP image created successfully at assets/ogp-image.png")
    
except ImportError:
    print("PIL not available, will use alternative method")
    # Copy the original image as fallback
    import shutil
    shutil.copy("/tmp/github-images/image-1754609896104-0.png", 
                "/home/runner/work/commons-action-matsumoto/commons-action-matsumoto/assets/ogp-image.png")
    print("Copied original image as assets/ogp-image.png")
    
except Exception as e:
    print(f"Error creating OGP image: {e}")
    # Fallback: copy original image
    import shutil
    shutil.copy("/tmp/github-images/image-1754609896104-0.png", 
                "/home/runner/work/commons-action-matsumoto/commons-action-matsumoto/assets/ogp-image.png")
    print("Used fallback: copied original image as assets/ogp-image.png")