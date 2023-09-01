##############################################################################
# Btune for Blosc2 - Automatically choose the best codec/filter for your data
#
# Copyright (c) 2023 The Blosc Developers <blosc@blosc.org>
# https://btune.blosc.org
# License: GNU Affero General Public License v3.0
# See LICENSE.txt for details about copyright and rights to use.
##############################################################################

# Usage
# python gather_data.py path_to_blosc2_file
import os
from pathlib import Path
import sys
import btune_training as bt


if len(sys.argv) != 2:
    print("Usage example: python gather_data.py data_files/temp.b2nd")
    raise Exception("You must pass the path to the .b2frame/.b2nd file")

entropy_file = bt.package_path() + "/gather_perf_data"
blosc2_file = sys.argv[1]

# Generate entropy data
os.system(entropy_file + ' -e ' + blosc2_file)
# Generate real data
os.system(entropy_file + ' ' + blosc2_file)
# Compress data files
os.system('gzip *.csv')
# Store them in a new directory
dir_name = str(Path(blosc2_file).parent / Path(blosc2_file).name) + ".meas"
print("Creating a directory for CSV files at:", dir_name)
os.system('mkdir ' + dir_name)
os.system('mv *.csv.gz ' + dir_name)
