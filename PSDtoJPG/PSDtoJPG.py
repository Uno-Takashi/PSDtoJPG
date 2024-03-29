from psd_tools import PSDImage
import sys
import os
import argparse
import glob
import re
from pathlib import Path

# arg parser
def get_args():
    parser = argparse.ArgumentParser()

    if sys.stdin.isatty():
        parser.add_argument("directory", help="please set directory", type=str)
    args = parser.parse_args()

    return args

# get psd files list
def get_psd_files(dir):
    # Get all file & dirs
    p = Path(dir)
    pre_files=list(p.glob("**/*"))
    psd_files=[]
    for x in pre_files:
        if x.suffix==".psd":
            psd_files.append(x)
    return psd_files

def jpg_path(path):
    jpg=".jpg"[::-1]
    psd=".psd"[::-1]
    return path[::-1].replace(psd,jpg,1)[::-1]

def psd_to_jpg(file_path):
    try:
        psd=PSDImage.load(file_path)
        pil_image=psd.as_PIL()
        pil_image.save(jpg_path(file_path))
        os.remove(file_path)
    except :
        pass




if __name__ == '__main__':
    args=get_args()
    if hasattr(args,"directory"):
        dir=args.directory
    else:
        print(">> Please input directory")
        exit()
    psd_files=[]
    if os.path.exists(dir):
        psd_files.extend(get_psd_files(dir))
    else:
        print(">> Directory not exist")
        exit()

    for x in psd_files:
        print(">> Converting "+str(x))
        psd_to_jpg(str(x))

    print(">> All files converted")