from psd_tools import PSDImage
import sys
import os
import argparse
import glob
import re


def get_args():
    parser = argparse.ArgumentParser()

    if sys.stdin.isatty():
        parser.add_argument("directory", help="please set directory", type=str)

    # 結果を受ける
    args = parser.parse_args()

    return(args)

def get_psd_files(dir):
    # Get all file & dirs
    psd_files=glob.glob(dir+"/*.psd" , recursive=True)
    return psd_files

def jpg_path(path):
    jpg=".jpg"[::-1]
    psd=".psd"[::-1]
    return path[::-1].replace(psd,jpg,1)[::-1]

def psd_to_jpg(file_path):
    psd=PSDImage.load(file_path)
    pil_image=psd.as_PIL()
    print(jpg_path(file_path))
    pil_image.save(jpg_path(file_path))




if __name__ == '__main__':
    args=get_args()
    if hasattr(args,"directory"):
        dir=args.directory
    else:
        print("Please input directory")
        exit()
    psd_files=[]
    if os.path.exists(dir):
        psd_files=get_psd_files(dir)
    else:
        print("Please input directory")
        exit()

    for x in psd_files:
        psd_to_jpg(x)