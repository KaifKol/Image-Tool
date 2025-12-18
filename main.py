import os
from PIL import Image

VALID_EXT = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")
DEFAULT_SIZE = (512, 512)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to return to menu...")

def get_folder():
    folder = input("Input folder: ").strip('"').strip()
    if not folder or not os.path.isdir(folder):
        print("Invalid folder.")
        pause()
        return None
    return folder

def parse_size(size_input):
    if not size_input.strip():
        return DEFAULT_SIZE
    try:
        return tuple(map(int, size_input.lower().split("x")))
    except ValueError:
        return None

def resize_images():
    folder = get_folder()
    if not folder:
        return

    size_input = input("Size (WIDTHxHEIGHT) [default: 512x512]: ")
    size = parse_size(size_input)
    if not size:
        print("Invalid size format.")
        return

    w, h = size
    out = os.path.join(folder, "resized")
    os.makedirs(out, exist_ok=True)

    for f in os.listdir(folder):
        if not f.lower().endswith(VALID_EXT):
            continue
        try:
            with Image.open(os.path.join(folder, f)) as img:
                img.resize((w, h), Image.LANCZOS).save(os.path.join(out, f))
                print(f"Resized: {f}")
        except Exception as e:
            print(f"Skipped {f}: {e}")

def convert_images():
    folder = get_folder()
    if not folder:
        return

    target = input("Target format (png, jpg, webp): ").lower().strip(".")
    out = os.path.join(folder, "converted")
    os.makedirs(out, exist_ok=True)

    for f in os.listdir(folder):
        if not f.lower().endswith(VALID_EXT):
            continue
        name, _ = os.path.splitext(f)
        try:
            with Image.open(os.path.join(folder, f)) as img:
                if target in ("jpg", "jpeg"):
                    img = img.convert("RGB")
                img.save(os.path.join(out, f"{name}.{target}"))
                print(f"Converted: {f}")
        except Exception as e:
            print(f"Skipped {f}: {e}")

def resize_and_convert():
    folder = get_folder()
    if not folder:
        return

    size_input = input("Size (WIDTHxHEIGHT) [default: 512x512]: ")
    target = input("Target format (png, jpg, webp): ").lower().strip(".")

    size = parse_size(size_input)
    if not size:
        print("Invalid size format.")
        return

    w, h = size
    out = os.path.join(folder, "processed")
    os.makedirs(out, exist_ok=True)

    for f in os.listdir(folder):
        if not f.lower().endswith(VALID_EXT):
            continue
        name, _ = os.path.splitext(f)
        try:
            with Image.open(os.path.join(folder, f)) as img:
                img = img.resize((w, h), Image.LANCZOS)
                if target in ("jpg", "jpeg"):
                    img = img.convert("RGB")
                img.save(os.path.join(out, f"{name}.{target}"))
                print(f"Processed: {f}")
        except Exception as e:
            print(f"Skipped {f}: {e}")

def show_menu():
    while True:
        clear_console()
        print("""
====================================
        IMAGE TOOL
   Resize & Convert Images
====================================
""")

        choice = input("""
 [1] Resize images
 [2] Convert format
 [3] Resize + Convert
 [4] Exit

 Enter choice: """)

        if choice == "1":
            resize_images()
        elif choice == "2":
            convert_images()
        elif choice == "3":
            resize_and_convert()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
            pause()

show_menu()
