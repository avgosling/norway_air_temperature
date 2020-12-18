import netCDF4
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)




url = 'https://thredds.met.no/thredds/dodsC/mepslatest/meps_lagged_6_h_latest_2_5km_latest.nc'
dataset = netCDF4.Dataset(url)
#print(nc.variables.keys()) # to get variables's names
#air_temp = nc.variables['air_temperature_2m'][:]
#print(air_temp)

#setting the index of the variable's dimensions to get the parameter with "time zero"
air_temp_t0 = dataset.variables['air_temperature_2m'][0,0,0,:,:]

#writing a .txt with the output
not_formated = open("not_formated.txt", 'w')
not_formated.write(repr(air_temp_t0))

#formating the .txt file, replacing commas with "tab space" (\t)
with open('not_formated.txt') as not_formated,open('final_text_file.txt', 'w') as final_txt_file:
    for line in not_formated:
        final_txt_file.write(line.replace(',', '\t'))







