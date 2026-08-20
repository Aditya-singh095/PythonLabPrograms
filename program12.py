from PIL import Image


def grayscale(image):
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Convert RGB to grayscale
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)

            pixels[x, y] = (gray, gray, gray)

    return image


def threshold(image, limit=128):
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            gray = int(0.299 * r + 0.587 * g + 0.114 * b)

            if gray >= limit:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)

    return image


def blur(image):
    width, height = image.size
    original = image.copy()
    old_pixels = original.load()
    new_pixels = image.load()

    for y in range(1, height - 1):
        for x in range(1, width - 1):

            r = g = b = 0

            # 3x3 neighborhood
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    pr, pg, pb = old_pixels[x + dx, y + dy]

                    r += pr
                    g += pg
                    b += pb

            # Average the 9 pixels
            new_pixels[x, y] = (
                r // 9,
                g // 9,
                b // 9
            )

    return image


def main():
    filename = input("Enter image filename: ")

    try:
        image = Image.open(filename).convert("RGB")
    except FileNotFoundError:
        print("Image not found.")
        return

    print("\nChoose an operation:")
    print("1. Grayscale")
    print("2. Black & White")
    print("3. Blur")

    choice = input("Enter choice: ")

    if choice == "1":
        result = grayscale(image)
        output = "grayscale.png"

    elif choice == "2":
        limit = int(input("Enter threshold (0-255): "))
        result = threshold(image, limit)
        output = "threshold.png"

    elif choice == "3":
        result = blur(image)
        output = "blur.png"

    else:
        print("Invalid choice.")
        return

    result.save(output)

    print(f"Processed image saved as: {output}")


if __name__ == "__main__":
    main()
