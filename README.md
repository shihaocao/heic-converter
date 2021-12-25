# heic-converter
A python3 script using heif-convert to batch convert heic files

# Installation
Install `heif-convert` using: https://ubuntuhandbook.org/index.php/2021/06/open-heic-convert-jpg-png-ubuntu-20-04/

Copy the included python3 script to the target directory that you are doing the conversion.
# Usage
In the target directory of conversion, run:

```
python3 heic-conv.py

```

This will convert all `.heic` files to `.jpg` at 99% quality. Edit the script to dial your desired quality.

Use the optional command line arguments of `--daux` to delete auxiliary files, or `-dorig` to delete the original heic files too.

```
python3 heic-conv.py --daux --dorig
```