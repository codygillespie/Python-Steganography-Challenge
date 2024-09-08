from PIL import Image
import numpy as np

INPUT_IMAGE_PATH = './images/source.bmp'

def set_lsb(value, bit):
    """
    Sets the least significant bit of a value.
    """
    return (value & ~1) | (bit & 1)

def embed_message(image_path, message, output_path):
    """
    Embeds a message into the least significant bit of the image pixels.
    """

    # Load the pixel data, this can be accessed as a 2D array,
    # e.g. pixels[x, y] = (R, G, B)
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels: np.ndarray = img.load() 

    # Convert message to binary and append a delimiter
    binary_message = ''
    for char in message:
        binary_char = format(ord(char), '08b')
        binary_message += binary_char
    binary_message += '00000000'
     
    # Check if the image is large enough to hold the message
    max_message_length = img.size[0] * img.size[1] * 3 // 8
    print(f'Checking if message fits in image: {len(binary_message)} <= {max_message_length}')
    if len(binary_message) > max_message_length:
        raise ValueError("Message is too long to fit in the image.")
    
    # Embed the binary message into the image
    binary_index = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            
            if binary_index >= len(binary_message):
                break
           
            # Embed bits into the least significant bit of each color component
            r, g, b = pixels[x, y]

            if binary_index < len(binary_message):
                r = set_lsb(r, int(binary_message[binary_index]))
                binary_index += 1

            if binary_index < len(binary_message):
                g = set_lsb(g, int(binary_message[binary_index]))
                binary_index += 1

            if binary_index < len(binary_message):
                b = set_lsb(b, int(binary_message[binary_index]))
                binary_index += 1

            # Update pixel
            pixels[x, y] = (r, g, b)

    # Save the modified image
    img.save(output_path)

def main():
    
    output_image_name = input("Enter the name of the output image (do not include path traversal characters): ")
    if not output_image_name.endswith('.bmp'):
        output_image_name += '.bmp'
    output_image_path = f'./images/{output_image_name}'

    message = input("Enter the message to embed: ")

    # Embed message
    embed_message(INPUT_IMAGE_PATH, message, output_image_path)
    print(f"Message '{message}' has been embedded in {output_image_path}")

if __name__ == '__main__':
    main()
