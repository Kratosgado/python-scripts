import os
import sys

# check a file was passed as an argument
if (len(sys.argv) != 2):
    print("Usage: python run_assembly.py <nasm_file>")
    sys.exit(1)

# get the nasm file from the command line argument
nasm_file = sys.argv[1]

# check if the file exist
if not os.path.isfile(nasm_file):
    print(f"Error: {nasm_file} does not exist")
    sys.exit(1)

# extract the file basename
basename = nasm_file.split('.')[0]

# assemble the nasm code
os.system(f"nasm -f elf64 {nasm_file} -o {basename}.o")

# link the object file generated
os.system(f"ld {basename.o} -o {basename}")

# run the executable created
os.system(f"./{basename}")