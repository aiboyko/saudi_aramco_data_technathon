# Saudi Aramco Data Technathon - 2020
This project is related to recovery of a 3D geological data from 2D slices

1) all porous data .npy files should be stored in the ```/data``` folder.
run ```bash auto.sh``` to run solver on all ```.npy``` files for which there are no reports.

```.npy``` files may contain either float arrays or thresholded arrays.
For float arrays please note that  ```.round()``` operator is applied in the end (which is equivalent to thresholding by 0.5)

2) after


3) We did an extensive architecture search among subtypes of the Fourier-features neural network. Results are stored in the ```fourier_results.csv```.

4) We did a secondary more narrow search around the best architecture too. 