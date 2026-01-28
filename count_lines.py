import sys
import os
from PIL import Image

def count_vertical_lines(image_path):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    if not image_path.lower().endswith(".jpg"):
        raise ValueError("Invalid file type. Only .jpg images are supported.")

    img = Image.open(image_path).convert("L") 
    width, height = img.size
    pixels = img.load()

    BLACK_THRESHOLD = 50  # 0 = black, 255 = white, increase to ~100 if you want a more loose tolerance, less for lower tolerance
    has_black = False #this is going to be a flag to keep track of pxiel colour
    black_columns = []

    for x in range(width): #scan the image by pixels to find black 
        has_black = False
        for y in range(height):
            if pixels[x, y] < BLACK_THRESHOLD:
                has_black = True
                break
        black_columns.append(has_black)

    # Count continuous runs of black columns. In_line flag will make sure we don't count every pixel as a seperate column.
    line_count = 0
    in_line = False

    for is_black in black_columns: 
        if is_black and not in_line:
            line_count += 1
            in_line = True
        elif not is_black:
            in_line = False

    return line_count


def main():
    try:
        # Validate argument count
        if len(sys.argv) != 2:
            print("Error: Exactly one argument (absolute image path) is required.")
            return

        image_path = sys.argv[1]
        result = count_vertical_lines(image_path)
        print("Found", result, "black vertical line(s).")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
