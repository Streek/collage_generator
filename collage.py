from PIL import Image, ImageDraw, ImageFont
import os
import random
import subprocess


def create_collage(directory, output_filename, width=1024, height=1024, text_position='bottom_right', font_size=20, random_sample=True):
    # Find image files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(
        os.path.join(directory, f)) and f.endswith(('.png', '.jpg', '.jpeg'))]
    images = [Image.open(os.path.join(directory, f)) for f in files]

    # Calculate the slice width for each image to maintain the square collage size
    slice_width = width // len(images)

    # Create a new, empty image with the correct size
    collage = Image.new('RGB', (width, height))

    # Loop over the images, take a slice from either a random location or the middle and add it to the collage
    for i, img in enumerate(images):
        w, h = img.size

        # Calculate scaling factors for width and height
        scaling_factor_width = slice_width / w
        scaling_factor_height = height / h

        # Choose the greater scaling factor to ensure the image slice fills the region
        scaling_factor = max(scaling_factor_width, scaling_factor_height)
        img = img.resize((int(w * scaling_factor), int(h * scaling_factor)), Image.ANTIALIAS)
        
        w, h = img.size  # Update the dimensions after resizing

        # Calculate the start and end coordinates for the slice
        if random_sample:
            start_x = random.randint(0, w - slice_width)
        else:
            start_x = (w - slice_width) // 2
        end_x = start_x + slice_width

        # Crop the slice from the chosen location in the image
        slice = img.crop((start_x, 0, end_x, height))

        # Paste the slice into the collage
        collage.paste(slice, (i * slice_width, 0))

    # Add watermark to the collage
    draw = ImageDraw.Draw(collage)
    font = ImageFont.truetype('font.ttf', font_size)
    text = "canvasByConnolly"
    textwidth, textheight = draw.textsize(text, font)
    margin = 10

    if text_position == 'center':
        x = (width - textwidth) // 2
        y = (height - textheight) // 2
    else:  # default to 'bottom_right'
        x = width - textwidth - margin
        y = height - textheight - margin

    draw.text((x, y), text, font=font, fill="white")

    # Save the collage image
    collage.save(output_filename)

    # Create and save low-quality versions of each image with watermark
    for i, img in enumerate(images):
        # Resize the image
        img = img.resize((250, 250), Image.ANTIALIAS)

        # Add watermark
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('font.ttf', 20)  # Adjust font size for smaller image
        text = "canvasByConnolly"
        textwidth, textheight = draw.textsize(text, font)
        margin = 5  # Adjust margin for smaller image
        x = 250 - textwidth - margin
        y = 250 - textheight - margin
        draw.text((x, y), text, font=font, fill="white")

        # Save the image
        img.save(f'image_{i+1}.jpg', quality=20)  # Adjust quality as needed

    # Open the collage image with the default program
    subprocess.call(['open', output_filename])


# Usage:
create_collage('./images', 'collage.jpg', text_position='center', font_size=90, random_sample=False)
