# Machine learning for finding similar weather patterns in big climate datasets

## Summary

For climate science it is sometimes interesting to look for analogue synoptic situations. This could be usefull for finding similar extreme events or when you would like to study changes in the occurrence of certain weather patterns (e.g. dunkelflautes). The problem is that these datasets can be very lange and that searching for similar patterns can be computational intensive and time consuming. 

In this project a convolutional autoencoder is used for compressing the dataset. Similar weather patterns are searched in compressed space. It is shown that "nearby weather patterns" in compressed space are also "nearby" in "real nature" and that the correlation between the distance in compressed and uncompressed space is high.

The used dataset files are part of the ERA-20C atmospheric reanalysis (https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era-20c):  

- Daily mean sea level pressure (MSL) [Pa]: https://climexp.knmi.nl/ERA-20C/era20c_msl_daily
- Daily 500 hPa geopotential height (Z500) [m2/s2]: https://climexp.knmi.nl/ERA-20C/era20c_z500_daily.nc

## Install

Clone this repository by:
```
git clone https://gitlab.com/kdg-ti/geertdepaepe/era20c.git
```
Create a "data" subdirectory and copy the MSL and Z500 files from the ERA-20C reanalysis in this directory.

Create a Jupyter Lab environment (see 7_annex1 for the installation of the toolkit) and connect to the cloned map. Read the 0_introduction notebook as introduction.
