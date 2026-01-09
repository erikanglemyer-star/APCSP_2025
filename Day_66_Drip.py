from PIL import Image
import requests
from io import BytesIO

# Load an image from a URL
def load_image_from_url(url):
    response = requests.get(url)
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
    resolution_mapping = {
        "320x213": "320px-Cute_dog.jpg",
        "640x427": "640px-Cute_dog.jpg",
        "800x533": "800px-Cute_dog.jpg",
        "1024x683": "1024px-Cute_dog.jpg",
        "1280x853": "1280px-Cute_dog.jpg",
        "2560x1706": "2560px-Cute_dog.jpg",
        "3176x2117": "Cute_dog.jpg" # Original resolution
    }
    return base_url + resolution_mapping[resolution]

# Main function
def main():
    base_url = "https://www.shutterstock.com/image-photo/cute-french-bulldog-puppy-eight-260nw-2322351863.jpg"
    print("Available resolutions: 320x213, 640x427, 800x533, 1024x683, 1280x853, 2560x1706, 3176x2117")
    resolution = input("Enter the desired resolution: ")
    try:
        image_url = get_resolution_url(base_url, resolution)
        print(f"Loading image at resolution {resolution}...")
        original_image = load_image_from_url(image_url)
        modified_image = modify_image(original_image)
        # Show and save the image
        modified_image.show()
        modified_image.save(f"modified_image_{resolution}.png")
        print(f"Modified image saved as 'modified_image_{resolution}.png'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()