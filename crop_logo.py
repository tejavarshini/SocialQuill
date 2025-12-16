from PIL import Image
import sys

def crop_whitespace(input_path, output_path):
    """Crop white space from an image"""
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGB if necessary
        if img.mode == 'RGBA':
            # Create a white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
            img = background
        
        # Convert to grayscale for easier processing
        gray = img.convert('L')
        
        # Get bounding box (removes white/near-white pixels)
        # Invert the image so white becomes black
        bbox = gray.point(lambda x: 0 if x > 250 else 255).getbbox()
        
        if bbox:
            # Crop the image
            cropped = img.crop(bbox)
            # Save the cropped image
            cropped.save(output_path)
            print(f"✓ Image cropped successfully!")
            print(f"  Original size: {img.size}")
            print(f"  Cropped size: {cropped.size}")
            print(f"  Saved to: {output_path}")
        else:
            print("No content found to crop")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_path = r"c:\Users\tejas\OneDrive\Documents\Desktop\SocialQuill\client\src\assets\SocialQuill.png"
    output_path = r"c:\Users\tejas\OneDrive\Documents\Desktop\SocialQuill\client\src\assets\SocialQuill.png"
    
    print("Cropping white space from SocialQuill.png...")
    crop_whitespace(input_path, output_path)
