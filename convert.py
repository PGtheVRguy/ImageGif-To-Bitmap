import time

from PIL import Image
from PIL import GifImagePlugin
import sys
import os
from ascii_magic import AsciiArt





print("Running Image Converter")
try:
    fname = sys.argv[1]
    if "--no-preview" in sys.argv:
        nogif = True
    else:
        nogif = False
    print(f"Attempting convert of {fname}")
    if (".gif" not in fname):
        print("Static image...")
        im = Image.open(fname).convert("RGB")
        print("Converted")
        nfName = fname[:-3]

        nfName = nfName + "bmp"
        print(f"Image saved as {nfName}")
        if not nogif:
            asci = AsciiArt.from_image(f"{nfName}")
            asci.to_terminal(columns=64)

        im.save(nfName)
    else:
        print("Gif detected")
        im = GifImagePlugin.Image.open(fname)
        nfName = fname[:-4]
        frames = im.n_frames
        try:
            os.mkdir(f"{nfName}")
            print("Made a directory for your gif")
        except FileExistsError:
            print("Directory already exists")
            print("Warning, this will overwrite existing files!")
            print(f"There are {frames} frames!")
            time.sleep(1)
        for i in range(frames):
            im.seek(i)
            subi = im.convert("RGB")
            subi.save(f"{nfName}/gif{i}.bmp")
            if not nogif:
                asci = AsciiArt.from_image(f"{nfName}/gif{i}.bmp")
                asci.to_terminal(columns=64)


            print("Frame made...")
        print("All frames saved!")


except IndexError:
    print("Error! Please run with the file you want as an argument, and make sure its in the same directory!")