#######################################################################
# Copyright (C) Blosc Development team <blosc@blosc.org>
# All rights reserved.
#######################################################################

# Usage
# python gather_data.py path_to_compiled_gather_perf_data path_to_b2nd_file
import os
import pathlib
import sys


if len(sys.argv) != 3:
    print("Usage example: python gather_data.py ../build/generator/gather_perf_data path_to.b2nd")
    raise Exception("You must pass the path to the compiled entropy_probe file"
                    " and the path to the b2nd file with the data")

entropy_file = sys.argv[1]
b2nd_file = sys.argv[2]

# Generate entropy data
os.system(entropy_file + ' -e ' + b2nd_file)
# Generate real data
os.system(entropy_file + ' ' + b2nd_file)
# Compress data files
os.system('gzip *.csv')
# Store them in a new directory
parent_name = pathlib.Path(b2nd_file).parent
dir_name = parent_name / "measurements3"
print("Moving measurements to:", dir_name)
os.system('mkdir ' + str(dir_name))
os.system('mv *.csv.gz ' + str(dir_name))
