#!/bin/bash
shopt -s nullglob

npy_data_path="~/Documents/DISK2TB/SaudiAramco/results_fourier"
npy_data_path='.'
solver_data_path="../elas3d_linux"

#FILES="${npy_data_path}*.npy"

cd $npy_data_path
FILES=*.npy

for fullname in $FILES
do
  purename="$(basename -s .npy $fullname)"
  reportname="${purename}.txt"
  #if there is $purename.txt -> skip, go to next file
  if [ -f "$reportname" ]
  then
    echo "Report $reportname exists."
  else
    echo "Report $reportname does not exist. Preparing data"
    python convert.py $fullname current_rock.dat #creates current_rock.dat AND re-writes current_els.PAM with proper cube sizes

    echo "Running ELAS3D"
    bash -c "${solver_data_path}/Elas3DCsharp ${npy_data_path}/current_elas.PAM  | tee ${npy_data_path}/${reportname}"
    echo "Saved as $reportname"
    echo "-----"
  fi

  # python convert npy to dat, save as current.dat
  # bash run 
  
done




echo All done

#    python prepare_npy_for_ELAS.py -n $fullname -o "current_file.dat"
