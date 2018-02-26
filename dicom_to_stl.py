import dicom
import os
import numpy
import mcubes
from pymesh import stl, obj

#PathDicom = "/Volumes/My Passport/Medical Images Data/Visible Human Project/head/"
PathDicom = "/Volumes/My Passport/Medical Images Data/Bones/Clavicle/combined_dcm/"
lstFilesDCM = []  # store filenames
for dirName, subdirList, fileList in os.walk(PathDicom):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))

# Get ref file
RefDs = dicom.read_file(lstFilesDCM[0], force=True)
#print RefDs

# Load dimensions based on the number of rows, columns, and slices (along the Z axis)
ConstPixelDims = (int(RefDs.Rows), int(RefDs.Columns), len(lstFilesDCM))

# Load spacing values (in mm)
ConstPixelSpacing = (float(RefDs.PixelSpacing[0]), float(RefDs.PixelSpacing[1]), float(RefDs.SliceThickness))

# The array is sized based on 'ConstPixelDims'
ArrayDicom = numpy.zeros(ConstPixelDims, dtype=RefDs.pixel_array.dtype)

# loop through all the DICOM files
for filenameDCM in lstFilesDCM:
    # read the file
    ds = dicom.read_file(filenameDCM, force=True)
    # store the raw image data
    ArrayDicom[:, :, lstFilesDCM.index(filenameDCM)] = ds.pixel_array

#print ArrayDicom.shape #(512,512,#images)
#print type(ArrayDicom) #nparray
print "Done loading dicom images to np array"

# Extract #-isosurface
iso_num = 70
vertices, triangles = mcubes.marching_cubes(ArrayDicom, iso_num)
#print type(vertices) #nparray
#print type(triangles) #nparray
print "Done with marching cubes algorithm"

# Export the result
mcubes.export_obj(vertices, triangles, "clavicle-" + str(iso_num) + ".obj")
print "File saved as obj"


# Convert to stl
m = obj.Obj("clavicle-" + str(iso_num) + ".obj")
m.save_stl("clavicle-" + str(iso_num) + ".stl")
print "Converted to stl"
