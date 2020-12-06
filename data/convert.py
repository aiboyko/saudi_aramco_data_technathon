import argparse
import numpy as np
from pathlib import Path


def save_3d_to_dat(data3d: np.array, filename="data1.dat"):
    np.savetxt(filename, data3d.flatten(), fmt="%1.0f")
    

parser = argparse.ArgumentParser(description='.npy binary to ELAS3D .dat file')
parser.add_argument('in_file', type=str, help='Input file (.npy)')
parser.add_argument('out_file', type=str, help='Output file (.dat)', default='current_rock.dat')
args = parser.parse_args()

if args.out_file:
    outfile = args.out_file
else:
    inname = Path(args.in_file).stem
    print('inname', inname)
    outfile = inname + '.dat'

outfile = args.out_file
arr = np.load(args.in_file).round()
Ns = arr.shape

# elas_folder = '/home/ab/Documents/DISK2TB/SaudiAramco/results_fourier/'
elas_filepath = 'current_elas.PAM'
with open(elas_filepath, "r") as f:
    s = f.read()
f.close()

lines = s.strip().split("\n")
lines[1] = ' '.join(map(str, Ns))
for i, _ in enumerate(lines):
    lines[i] += '\n'

with open(elas_filepath, "w") as f:
    f.writelines(lines)    
  

save_3d_to_dat(arr, outfile)
print('Saved as', outfile)
