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

# python2 png_to_stlv2.py -p /Users/aether/Documents/Dicom2Mesh/testing -o testing

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
	mcubes.export_obj(vertices, triangles, args["output"] + ".obj")
	print "File saved as obj"

	# Convert to stl
	m = obj.Obj(args["output"] + ".obj")
	m.save_stl(args["output"] + ".stl")
	print "Converted to stl"



	# mesh = pymesh.load_mesh(args["output"] + ".obj")
	# mesh, info = pymesh.split_long_edges(mesh, rel_threshold=0.3, preserve_feature=True)
	# mesh, info = pymesh.collapse_short_edges(mesh, rel_threshold=0.1, preserve_feature=True)
	# mesh, info = pymesh.remove_duplicated_faces(mesh)
	# mesh, info = pymesh.remove_isolated_vertices(mesh)
	# mesh, info = pymesh.remove_duplicated_vertices(mesh, tol=.1)

	# pymesh.save_mesh("filename.obj", mesh)