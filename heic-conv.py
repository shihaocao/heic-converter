import os, subprocess


CMD = "heif-convert"
QUALITY = "-q"
QUALITY_ARG = "99"


def find_all_heics() -> None:
    '''Find all heic files in the current directory, regardless of capitalization'''
    all_files = os.listdir('.')
    heics = [x for x in all_files if x.endswith('.heic') or x.endswith('.HEIC')]
    return heics


def convert_and_delete(file_name: str) -> None:
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

    # delete the auxilary file
    aux_file_name = base_file + "-urn:com:apple:photo:2020:aux:hdrgainmap" + ".JPG"
    os.remove(aux_file_name)
    print(f"Deleted aux file: {aux_file_name}")

    # delete the original file
    orig_file_name = base_file + original_file_extension
    os.remove(orig_file_name)
    print(f"Deleted original file: {orig_file_name}")

    print("\n")

if __name__ == "__main__":
    heics = find_all_heics()
    for file in heics:
        convert_and_delete(file)