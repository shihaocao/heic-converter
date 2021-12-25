'''A pythons script for batch converting heic files.'''


import argparse
import os
import subprocess
import time


CMD = "heif-convert"
QUALITY = "-q"
QUALITY_ARG = "99"
AUX_FILE_SUFFIX = "-urn:com:apple:photo:2020:aux:hdrgainmap"


def parse_args() -> argparse.Namespace:
    '''Get the args from the command line'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--daux", action="store_true", help="Delete aux files")
    parser.add_argument("--dorig", action="store_true", help="Delete original files")
    args = parser.parse_args()
    return args


def find_all_heics() -> None:
    '''Find all heic files in the current directory, regardless of capitalization'''
    all_files = os.listdir('.')
    heics = [x for x in all_files if x.endswith('.heic') or x.endswith('.HEIC')]
    return heics


def convert_and_delete(file_name: str, delete_aux: bool = False, delete_orig:bool = False) -> None:
    '''On the original file name, call heif-convert, and delete the aux and original files'''
    base_file = file_name[:-5]
    original_file_extension = file_name[-5:]

    # create the new file
    new_file = base_file + ".JPG"
    args = [CMD, QUALITY, QUALITY_ARG, file, new_file]
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    string_output = output.decode("utf-8")
    print(string_output)

    if delete_aux:
        # delete the auxilary file
        aux_file_name = base_file + AUX_FILE_SUFFIX + ".JPG"
        os.remove(aux_file_name)
        print(f"Deleted aux file: {aux_file_name}")

    if delete_orig:
        # delete the original file
        orig_file_name = base_file + original_file_extension
        os.remove(orig_file_name)
        print(f"Deleted original file: {orig_file_name}\n")

if __name__ == "__main__":
    start_time = time.time()
    args = parse_args()
    heics = find_all_heics()
    print(f'Found {len(heics)} heic files in this directory.')

    for file in heics:
        convert_and_delete(file, args.daux, args.dorig)
        
    end_time = time.time()
    print(f'Deleted {len(heics)} heic files in {end_time - start_time} seconds.')