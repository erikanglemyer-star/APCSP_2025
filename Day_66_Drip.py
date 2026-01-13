from PIL import Image
import requests
from io import BytesIO
import time

# Load an image from a URL
def load_image_from_url(url):
    print(f"Fetching URL: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    print(f"Response status: {response.status_code}")
    print(f"Content type: {response.headers.get('content-type')}")
    img = Image.open(BytesIO(response.content))
    return img

# Modify the image by swapping and adjusting color channels
def modify_image(img):
    # Convert the image to RGB mode if its not already
    img = img.convert("RGB")
    pixels = img.load() # Access the pixel data.

    # Iterate over all pixels in the image
    for x in range(img.width):
        for y in range(img.height):
            red, green, blue = pixels[x, y] # Get the RGB values of the pixel

            # Swap red and green channelsm and adjust blue
            new_red = green
            new_green = blue
            new_blue = red

            # Assign the new color back to the pixel
            pixels[x, y] = (new_red, new_green, new_blue)

    return img

def get_resolution_url(base_url, resolution):
    # Split resolution into width and height
    width, height = resolution.split('x')
    return f"https://picsum.photos/{width}/{height}"

# Main function
def main():
    base_url = ""  # Not needed anymore, but keeping for compatibility
    print("Available resolutions: 320x213, 640x427, 800x533, 1024x683, 1280x853, 2560x1706, 3176x2117")
    resolution = input("Enter the desired resolution: ")
    
    try:
        image_url = get_resolution_url(base_url, resolution)
        print(f"Loading image at resolution {resolution}...")
        
        # Start timing
        start_time = time.time()
        
        original_image = load_image_from_url(image_url)
        modified_image = modify_image(original_image)
        
        # End timing
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Show and save the image
        modified_image.show()
        modified_image.save(f"modified_image_{resolution}.png")
        print(f"Modified image saved as 'modified_image_{resolution}.png'")
        print(f"Processing time: {processing_time:.4f} seconds")  # Shows 4 decimal places
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()