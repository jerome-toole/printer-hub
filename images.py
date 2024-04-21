from PIL import Image

def prepare_image(image, width):
    # Load the image using PIL
    image = Image.open(image)

    # Calculate the new height to maintain aspect ratio
    aspect_ratio = image.width / image.height
    new_height = int(width / aspect_ratio)

    # Resize the image to fit the printer width
    image = image.resize((width, new_height), Image.BICUBIC)

    # Save the resized image temporarily (optional, you could print directly from memory)
    temp_path = "/tmp/temp_print_image.jpg"
    image.save(temp_path)

    return temp_path
