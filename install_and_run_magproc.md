How to use magproc in Windows

This is designed for channel names in MAG_channel_list_DGGS_v20240305.csv

The output can be viewed in Oasis Montaj with these three DB views, all found within the "OM_views" folder.  
> 1_drape_speed_x_y_utc_DEM_laptop.dbview  
> 2_diurnal_utc_magcom_qc.dbview  
> 3_0p05_noise_comp_4th_10Hz_clip.dbview  


  
Windows Instructions:
- Install python (≥3.10)

- Open a python prompt:

- deactivate any other running pythons
    - `deactivate`

- Create a new virtual environment
    - `python -m virtualenv <your_ve_name_here>`

- Activate the virtual environment
    - `<path_to_your_ve_here>\Scripts\activate`

- Clone github repo to local machine
    - `git clone https://github.com/SagebrushGeoTools/magproc.git`

- Install magproc:
    - `pip install .`

If using a Jupyter notebook:
- Install jupyter
    - `pip install jupyter`

- Create Jupyter kernel from virtual environment:
    - `python -m ipykernel install --name <your_ve_name_here> --user`

- Copy example notebook to project working directory:

- From your working directory start Jupyter:
    - `jupyter lab`

- Change the input and output file paths in the notebook. Use shift enter to run cells.
