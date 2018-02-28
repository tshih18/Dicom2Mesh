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
import re

# python2 png_to_stlv2.py -p /Users/aether/Documents/Dicom2Mesh/testing -o testing

# Test if a given chunk is an int
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

if __name__ == '__main__':
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
		natural_sort(fileList)
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

	# Extract #-isosurface
	vertices, triangles = mcubes.marching_cubes(ArrayDicom, 0)
	#print type(vertices) #nparray
	#print type(triangles) #nparray
	print "Done with marching cubes algorithm"

	# Export the result
	mcubes.export_obj(vertices, triangles, "3D_Models/" + args["output"] + ".obj")
	print "File saved as obj"

	# Convert to stl
	m = obj.Obj("3D_Models/" + args["output"] + ".obj")
	m.save_stl("3D_Models/" + args["output"] + ".stl")




	print "Converted to stl"
