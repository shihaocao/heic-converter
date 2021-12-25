import os, subprocess

cmd = "heif-convert"
QUALITY = "-q"
QUALITY_ARG = "99"

origs = os.listdir('.')
heics = os.listdir('.')

i = 0

while i < len(heics):
    heics[i] = heics[i].lower()
    if not heics[i].endswith(".heic"):
        heics.pop(i)
        origs.pop(i)
        i -= 1
    i += 1

for file in origs:
    base_file = file[:-5]
    new_file = base_file + ".JPG"
    args = [cmd, QUALITY, QUALITY_ARG, file, new_file]
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    string_output = output.decode("utf-8")
    print(string_output)

    # delete the aux file
    aux_file_name = base_file + ".HEIC"
    os.remove(aux_file_name)

    print(f"Deleting aux file: {aux_file_name}\n")

