from scipy.ndimage import imread
import os
import numpy
import mcubes
from pymesh import stl, obj

PathPng = "/Volumes/My Passport/Medical Images Data/Visible Human Project/head/"
#PathDicom = "/Volumes/My Passport/Medical Images Data/Bones/Clavicle/combined_dcm/"
lstFilesPng = []  # store filenames
for dirName, subdirList, fileList in os.walk(PathPng):
    for filename in fileList:
        if ".png" in filename.lower():  # check whether the file's DICOM
            lstFilesPng.append(os.path.join(dirName,filename))

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (1216, 2048, 3, len(lstFilesPng))


# The array is sized based on 'ConstPixelDims'
ArrayDicom = numpy.zeros(ConstPixelDims)

# loop through all the DICOM files
for filenamePng in lstFilesPng:
    # read the file
    png_array = imread(filenamePng)
    # store the raw image data
    ArrayDicom[:, :, :, lstFilesPng.index(filenamePng)] = png_array
    print "Done with" + str(lstFilesPng.index(filenamePng)) + "out of" + str(len(lstFilesPng))

print ArrayDicom.shape #(512,512,#images)
#print type(ArrayDicom) #nparray
print "Done loading dicom images to np array"

# Extract #-isosurface
vertices, triangles = mcubes.marching_cubes(ArrayDicom, 33)
#print type(vertices) #nparray
#print type(triangles) #nparray
print "Done with marching cubes algorithm"

# Export the result
mcubes.export_obj(vertices, triangles, "clavicle-33.obj")
print "File saved as obj"


# Convert to stl
m = obj.Obj("clavicle-33.obj")
m.save_stl("clavicle.stl")
print "Converted to stl"
