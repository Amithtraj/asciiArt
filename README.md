# Character Art Generator

The Character Art Generator is a Python script that converts any image into character art, a form of digital art where images are represented using text characters. The script utilizes the Pillow library to process the image and generate the character art.

## Features

- Convert any image into character art
- Customize the characters used for the art
- Adjust the resolution of the output character art
- Add shading effect to the character art for a more realistic appearance
- Save the character art to a text file

## Installation

1. Clone the repository:
2. pip install pillow
   
## Usage

1. Run the script:
2. Enter the path to the image file when prompted.
3. Enter the name for the output text file when prompted (e.g., `character_art.txt`).
4. The character art will be generated and saved to the specified text file.

## Customization

You can customize the script by modifying the following variables:

- `characters`: This list defines the characters used to represent different shades of gray in the character art. You can add or remove characters from this list to change the appearance of the art.

- `image.resize((100, 100))`: This line resizes the input image to 100x100 pixels for better performance. You can adjust the resolution by changing the values inside the parentheses.



## Contributing

Contributions to the Character Art Generator are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
