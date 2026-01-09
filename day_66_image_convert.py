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

# Main function
def main():
    # Example image URL (use a small image for better performance)
    image_url = "https://www.shutterstock.com/image-photo/cute-french-bulldog-puppy-eight-260nw-2322351863.jpg" # Replace with your image URL

    try:
        original_image = load_image_from_url(image_url)
        modified_image = modify_image(original_image)

        # Show the modified image
        modified_image.show()

        # Save the modified image to a file
        modified_image.save("modified_image.png")
        print("Modified image saved as 'modified_image.png'")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()