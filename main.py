from PIL import Image

# Ask the user for the image file path
image_path = input("Enter the path to the image file: ")

# Open the image
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print("Error: The specified image file does not exist.")
    exit()

# Resize the image to a smaller size for better performance
image = image.resize((100, 100))

# Convert the image to grayscale
grayscale_image = image.convert("L")

# Define the characters to use for the art, with different characters for different shades of gray
characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Create a list to store the character art
character_art = []

# Loop through each pixel and replace it with a character from the list
for y in range(grayscale_image.height):
    row = ""
    for x in range(grayscale_image.width):
        pixel_value = grayscale_image.getpixel((x, y))
        row += characters[int(pixel_value / 255 * len(characters))]
    character_art.append(row)

# Add shading to the character art
shaded_character_art = []
for row in character_art:
    shaded_row = ""
    for char in row:
        if char == " ":
            shaded_row += " "
        else:
            shaded_row += char + "\u0336"  # Add the combining diacritic (iota subscript) for shading
    shaded_character_art.append(shaded_row)

# Ask the user for the output file name
output_file = input("Enter the name for the output text file (e.g., character_art.txt): ")

# Save the character art to a text file
try:
    with open(output_file, "w", encoding="utf-8") as file:
        for row in shaded_character_art:
            file.write(row + "\n")
    print(f"Character art saved to {output_file}")
except Exception as e:
    print(f"Error: {e}")