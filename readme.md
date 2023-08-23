
# Collage Creator

This project allows users to generate a unique collage from a collection of images. The collage consists of slices from each image, either taken from a random location within each image or centered. After creating the main collage, the program also generates low-quality preview versions of each image used in the collage.

## Features
- Creates a collage from a directory of images.
- Option to sample random parts of an image or use the middle for the collage.
- Generates low-quality previews of each image with watermark.

## Requirements
- Python 3.x
- PIL (Python Imaging Library)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/streek/collage-creator.git
   ```
2. Install the required packages:
   ```bash
   pip install pillow
   ```

## Usage

1. Place your images in a directory (e.g., `./images`).
2. Run the script:
   ```bash
   python collage_creator.py
   ```
3. By default, the collage will be saved as `collage.jpg` and the previews will be saved as `image_1.jpg`, `image_2.jpg`, etc.

## Customization

You can customize the output by adjusting the following parameters when calling the `create_collage` function:

- `directory`: The directory containing the images.
- `output_filename`: The filename for the output collage.
- `width` & `height`: Dimensions of the collage.
- `text_position`: Position of the watermark on the collage (`'center'` or `'bottom_right'`).
- `font_size`: Font size of the watermark.
- `random_sample`: Set to `True` for random sampling or `False` to use the middle of each image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## Acknowledgements

- Thanks to OpenAI for initial guidance.
