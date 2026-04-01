from PIL import Image

def grayscale(image):
    return image.convert("L").convert("RGB")

def sepia(image):
    image = grayscale(image)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            red, green, blue = pixels[x, y]

            if red < 63:
                red = int(red * 1.1)
                blue = int(blue * 0.9)
            elif red < 192:
                red = int(red * 1.15)
                blue = int(blue * 0.85)
            else:
                red = min(int(red * 1.08), 255)
                blue = int(blue * 0.93)

            pixels[x, y] = (red, green, blue)

    return image

if __name__ == "__main__":
    img = Image.open("cat.jpg")
    sepia_img = sepia(img)
    sepia_img.show()
    sepia_img.save("output_sepia.jpg")