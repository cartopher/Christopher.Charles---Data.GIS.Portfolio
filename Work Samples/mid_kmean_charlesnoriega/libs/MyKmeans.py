import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np

import os

os.listdir('../Landsat8/')
# import bands as separate 1 band raster
band4 = rasterio.open('../LC08_L1TP_097011_20211104_20211104_02_RT_B4')  # red
band5 = rasterio.open('../LC08_L1TP_097011_20211104_20211104_02_RT_B5')  # nir
# number of raster rows
var1 = band4.height
# number of raster columns
var2 = band4.width
# plot band
plot.show(band4)
# type of raster byte
var3 = band4.dtypes[0]
# raster sytem of reference
var4 = band4.crs
# raster transform parameters
var5 = band4.transform
# raster values as matrix array
band4.read(1)
# multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(band4, ax=ax1, cmap='Blues')  # red
plot.show(band5, ax=ax2, cmap='Blues')  # nir
fig.tight_layout()
# generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

nir
# ndvi calculation, empty cells or nodata cells are reported as 0
ndvi = np.where(
    (nir + red) == 0.,
    0,
    (nir - red) / (nir + red))
var6 = ndvi[:5, :5]
# export ndvi image
ndviImage = rasterio.open('../Output/ndviImage.tiff', 'w', driver='Gtiff',
                          width=band4.width,
                          height=band4.height,
                          count=1, crs=band4.crs,
                          transform=band4.transform,
                          dtype='float64')
ndviImage.write(ndvi, 1)
ndviImage.close()

ndvi = rasterio.open('../Output/ndviImage.tiff')
fig = plt.figure(figsize=(18, 12))
plot.show(ndvi)
