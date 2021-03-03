# This code is the Bronze winner of the Saudi Aramco Innovations Data Technathon - 2020
Recovery of a 3D geological data from 2D slices by Alexey Boyko and Daria Fokina.

## User Manual and Authors' comments

1) all porous data .npy files should be stored in the ```/data``` folder.

Run ```bash auto.sh``` to run solver on all ```.npy``` files for which there are no reports.

```.npy``` files may contain either float arrays or thresholded arrays.
For float arrays please note that  ```.round()``` operator is applied in the end (which is equivalent to thresholding by 0.5)

2) run ```report_fourier.ipynb``` for assemblying all results from ELAS3D solver in one ```.csv```.

3) We did an extensive architecture search among subtypes of the Fourier-features neural network. Results are stored in the ```fourier_results.csv```.

4) The code and an example of a relatively good recovery from 4 slices per dimension can be found in the ```fourier_to_show_nice_pictures.ipynb```. In it, there is a button with a link to run it on Colab. Some data paths may need to be changed to actually find the data on your computer (or Colab)

We also introduced porosity matching procedure, which adaptively selects threshold such that it matches the training data, and did second (more narrow) ablation studies. Results can be found in the ```results2.csv```

5) We provided some examples of the data cubes to show the work of the automation scripts.

6) Since without a supercomputer any properly thorough ablation studies are impossible on resolutions higher than around ```128^3```, we did in on a downscaled data. Because it is a Neural model, some peculiarities (such as learning rate) may be changed depending on the resolution. But the automatino pipeline should help you discover that if you have access to a cluster.
