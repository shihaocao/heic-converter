import glob, os, subprocess

cmd = "heif-convert"
QUALITY = "-q"
QUALITY_ARG = "99"

for file in glob.glob("*.heic"):
    base_file = file[:-5]
    new_file = base_file + ".jpg"
    args = [cmd, QUALITY, QUALITY_ARG, file, new_file]
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    string_output = output.decode("utf-8")
    print(string_output)

    # delete the aux file
    aux_file_name = base_file + "-urn:com:apple:photo:2020:aux:hdrgainmap" + ".jpg"
    os.remove(aux_file_name)

    print(f"Deleting aux file: {aux_file_name}\n")

