from PIL import Image
import sys

def get_dominant_color(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    # Get the color of the first pixel as it's a solid color image
    color = img.getpixel((0, 0))
    return '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])

if __name__ == "__main__":
    path = r'C:/Users/shafi/.gemini/antigravity/brain/002c60bd-d9cf-40cb-adbc-c21b4a97c30a/uploaded_media_1769419637445.png'
    print(get_dominant_color(path))
