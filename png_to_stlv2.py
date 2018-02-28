import numpy as np
import os
import argparse
import scipy.misc as misc
import matplotlib.pyplot as plt
from scipy.ndimage import imread
import os
import numpy
import mcubes
from pymesh import stl, obj
import vtkInterface
import vtk



# python2 png_to_stlv2.py -p /Users/aether/Documents/Dicom2Mesh/testing -o testing
# python2 png_to_stlv2.py -p /Users/aether/Downloads/male_female_dcm_vishuman/male_dcm/Pelvis/pelvis_png -o pelvis

if __name__ == '__main__':
	'''
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--path", required=True,
		help="path to the input images")
	ap.add_argument("-o", "--output", required=True,
		help="output file name excluding file extension")
	args = vars(ap.parse_args())

	all_imgs = []

	print(args["path"])

	for dirName, subdirList, fileList in os.walk(args["path"]):
		for filename in fileList:
			print(filename)
			if ".png" in filename.lower():  # check whether the file's png
				img = misc.imread(os.path.join(dirName,filename), flatten=True)
				print(img.shape)
				all_imgs.append(img)

	all_imgs = np.dstack(all_imgs)

	print(all_imgs.shape)

	np.save("all_img.npy", all_imgs)

	ArrayDicom = np.load("all_img.npy")

	print(ArrayDicom.shape)


################################################################

	# verts, faces, normals, values = measure.marching_cubes_lewiner(ArrayDicom, 0.0)
	verts, faces, normals, values = measure.marching_cubes_lewiner(ArrayDicom, 0.0, allow_degenerate=False) # takes away triangles with 0 area, slows down algo
	'''


	# pip2 install vtk
	# pip2 install vtkInterface
	# Filetype must be either "ply", "stl", "g3d" or "vtk"
	# http://vtkinterface.readthedocs.io/en/latest/polydata.html#mesh-manipulation-and-plotting
	# mesh = vtkInterface.PolyData(args["output"] + ".stl")

	# mesh = vtkInterface.PolyData()
	# mesh = mesh.MakeFromArrays(vertices=verts, faces=faces)

	mesh = vtkInterface.PolyData("pelvis_thresh_full.stl")

	# Cleans mesh by merging duplicate points, removed unused points, and/or remove degernate cells
	mesh.Clean()
	# Returns an all triangle mesh
	mesh = mesh.TriFilter()


	# -------------------- Remove small islands of certain threshold of biggest region -------------------------------------
	connectivity = vtk.vtkPolyDataConnectivityFilter()
	connectivity.SetInputData(mesh)
	connectivity.SetExtractionModeToAllRegions()
	connectivity.Update()

	# remove objects consisting of less than ratio vertexes of the biggest object
	regionSizes = connectivity.GetRegionSizes()

	maxSize = 0
	regions = 0
	# find object with most vertices
	while regions < connectivity.GetNumberOfExtractedRegions():
		if regionSizes.GetValue(regions) > maxSize:
			maxSize = regionSizes.GetValue(regions)
		regions += 1
	# append regions of sizes over the threshold
	connectivity.SetExtractionModeToSpecifiedRegions()
	regions1 = 0
	ratio = 0.1
	while regions1 < connectivity.GetNumberOfExtractedRegions():
		if regionSizes.GetValue(regions1) > (maxSize * ratio):
			connectivity.AddSpecifiedRegion(regions1)
		regions1 += 1

	connectivity.Update()
	mesh.DeepCopy(connectivity.GetOutput())
	# ----------------------------------------------------------------------------------------------
	nbrOfSmoothingIterations = 20
	smoother = vtk.vtkSmoothPolyDataFilter()
	smoother.SetInputData(mesh)
	smoother.SetNumberOfIterations(nbrOfSmoothingIterations)
	smoother.SetFeatureAngle(45)
	smoother.SetRelaxationFactor(0.05)
	smoother.Update()
	mesh.DeepCopy(smoother.GetOutput())

	mesh.Plot(color='orange')
