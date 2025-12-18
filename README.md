# Image Tool

A simple Python script for resizing and converting images in bulk. This tool allows you to resize images to a specific resolution, convert them to a different format, or do both at once.

## Features

- Resize images to a custom width and height.
- Convert images to `png`, `jpg`, or `webp` formats.
- Resize and convert images in a single step.
- Supports common image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`, `.webp`.
- Outputs processed images to separate folders (`resized`, `converted`, `processed`).

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) library

Install Pillow via pip:

```bash
pip install pillow
````

## Usage

1. Run the script:

```bash
python main.py
```

2. Select an option from the menu:

```
[1] Resize images
[2] Convert format
[3] Resize + Convert
[4] Exit
```

3. Follow the prompts:

* **Folder path**: Enter the path to the folder containing images.
* **Size**: Enter the new size in `WIDTHxHEIGHT` format (default: 512x512).
* **Target format**: Enter the desired format (`png`, `jpg`, `webp`).

4. Processed images will be saved in new folders inside the selected directory:

* `resized` — for resized images.
* `converted` — for converted images.
* `processed` — for resized and converted images.

## Notes

* Images that cannot be processed will be skipped with an error message.
* When converting to `jpg` or `jpeg`, images are automatically converted to RGB mode to ensure compatibility.
