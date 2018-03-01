
'''
shoulder_mesh = vtkInterface.PolyData("f_shoulder_full_smooth.stl")
head_mesh = vtkInterface.PolyData("head_full_smooth.stl")

vtkappend = vtk.vtkAppendPolyData()
vtkappend.AddInputData(shoulder_mesh)
vtkappend.AddInputData(head_mesh)
vtkappend.Update()
head_shoulder = vtkInterface.PolyData(vtkappend.GetOutput())

head_shoulder.Plot(color='orange')
'''

import numpy as np
import os
import argparse
import scipy.misc as misc
from scipy.ndimage import imread
from skimage import measure
from pymesh import stl, obj
import vtkInterface
import vtk
import re
import mcubes
from stl import mesh


def tryint(c):
	try:
		return int(c)
	except:
		return c

# turn a string into a list of string and number chunks
def alphanum_key(s):
	return [tryint(c) for c in re.split('([0-9]+)', s)]

# sort the given list
def natural_sort(list):
	list.sort(key=alphanum_key)


# python2 png_to_stlv2.py -p /Users/aether/Documents/Dicom2Mesh/testing -o testing
# python2 png_to_stlv2.py -p /Users/aether/Downloads/male_female_dcm_vishuman/male_dcm/Pelvis/pelvis_png -o pelvis

if __name__ == '__main__':

	# # construct the argument parse and parse the arguments
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-p", "--path", required=True,
	# 	help="path to the input images")
	# ap.add_argument("-o", "--output", required=True,
	# 	help="output file name excluding file extension")
	# args = vars(ap.parse_args())
    #
	all_imgs = []
    #
	# print(args["path"])

    paths = ["/home/aether/Desktop/Medical Image Segmentation/bones-unet/head_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_shoulder_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/pelvis_thresh_predictions/"]
    for path in paths:
        for dirName, subdirList, fileList in os.walk(path):
    		natural_sort(fileList)
    		for filename in fileList:
    			print(filename)
    			if ".png" in filename.lower():  # check whether the file's png
    				img = misc.imread(os.path.join(dirName,filename), flatten=True)
    				all_imgs.append(img)

	ArrayPNG = np.dstack(all_imgs)

	# verts, faces, normals, values = measure.marching_cubes_lewiner(ArrayDicom, 0.0)
	verts, faces, normals, values = measure.marching_cubes_lewiner(ArrayPNG, 0.0, allow_degenerate=False) # takes away triangles with 0 area, slows down algo
	# print type(verts), verts.shape # (V,3)
	# print type(faces), faces.shape # (F,3)

	# ---------- Convert to stl ----------
	output_filename = args["output"] + ".stl"
	solid = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
	for i,f in enumerate(faces):
		for j in range(3):
			solid.vectors[i][j] = verts[f[j],:]
	solid.save(output_filename)
	print "Converted to stl"


	# ---------- Save as obj and convert to stl ----------
	# mcubes.export_obj(verts,faces,args["output"]+".obj")
	# print "File saved as obj"
    #
    #
	# m = obj.Obj(args["output"]+".obj")
	# m.save_stl(output_filename)
	# print "Converted to stl"

	mesh = vtkInterface.PolyData(output_filename)
	#mesh.Plot(color='white')

	# ---------- Fill holes ----------
	fill = vtk.vtkFillHolesFilter()
	fill.SetInputData(mesh)
	fill.SetHoleSize(100)
	fill.Update()
	mesh.DeepCopy(fill.GetOutput())
	#mesh.Plot(color='white')


	# ---------- Clean and triangulate mesh ----------
	# Cleans mesh by merging duplicate points, removed unused points, and/or remove degernate cells
	mesh.Clean()
	# Returns an all triangle mesh
	mesh = mesh.TriFilter()
	print "Done with cleaning and triangle meshing"
	#mesh.Plot(color='orange')

	# ---------- Remove small islands compared to number vertices of biggest region ----------
	connectivity = vtk.vtkPolyDataConnectivityFilter()
	connectivity.SetInputData(mesh)
	connectivity.SetExtractionModeToAllRegions()
	connectivity.Update()

	nregions = connectivity.GetNumberOfExtractedRegions()
	regionSizes = connectivity.GetRegionSizes()
	maxSize = 0
	regions = 0
	# find object with most vertices
	while regions < nregions:
		if regionSizes.GetValue(regions) > maxSize:
			maxSize = regionSizes.GetValue(regions)
		regions += 1

	# append regions of sizes over the threshold
	connectivity.SetExtractionModeToSpecifiedRegions()

	regions1 = 0
	ratio = 0.01 # pelvis -.02
	reduced_regions = []
	while regions1 < nregions:
		if regionSizes.GetValue(regions1) > (maxSize * ratio):
			connectivity.AddSpecifiedRegion(regions1)
			reduced_regions.append(regions1)
		regions1 += 1

	connectivity.Update()


	# ---------- Remove small islands compared to volume of biggest region ----------
	regions_and_volume = []
	max_volume = 0
	count = 1

	for region in reduced_regions:
		#if region == 139: continue # for head
		# f_shoulder keep all regions
		connectivity.InitializeSpecifiedRegionList()
		connectivity.AddSpecifiedRegion(region)
		connectivity.Update()

		# Turns region into polydata
		p = vtk.vtkPolyData()
		p.DeepCopy(connectivity.GetOutput())

		# Get volume of region
		measured_p = vtk.vtkMassProperties()
		measured_p.SetInputData(p)
		measured_p_vol = measured_p.GetVolume()

		print(str(region) + " " + str(count) + " out of " + str(len(reduced_regions)) + " vol: " + str(measured_p_vol))
		count += 1

		if measured_p_vol > max_volume:
			max_volume = measured_p_vol

		regions_and_volume.append((region, measured_p_vol))

	connectivity.InitializeSpecifiedRegionList()
	ratio = .05
	for region,volume in regions_and_volume:
		if volume > (ratio * max_volume):
			 connectivity.AddSpecifiedRegion(region)

	connectivity.Update()
	mesh.DeepCopy(connectivity.GetOutput())

	# ---------- Smooth regions ----------
	nbrOfSmoothingIterations = 40
	smoother = vtk.vtkSmoothPolyDataFilter()
	smoother.SetInputData(mesh)
	smoother.SetNumberOfIterations(nbrOfSmoothingIterations)
	smoother.SetFeatureAngle(45)
	smoother.SetRelaxationFactor(0.05)
	smoother.Update()
	mesh.DeepCopy(smoother.GetOutput())
	print "Done Smoothing"

	mesh.Plot(color='orange')


	# ---------- Save to stl ----------
	writer = vtk.vtkSTLWriter()
	writer.SetFileName(output_filename)
	writer.SetInputData(mesh)
	writer.SetFileTypeToASCII()
	writer.Write()
	print "Saved file as stl"
