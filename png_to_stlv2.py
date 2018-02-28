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
from skimage import measure

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from skimage import measure
from skimage.draw import ellipsoid

# python2 png_to_stlv2.py -p /Users/aether/Documents/Dicom2Mesh/testing -o testing
# python2 png_to_stlv2.py -p /Users/aether/Downloads/male_female_dcm_vishuman/male_dcm/Pelvis/pelvis_png -o pelvis

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

	# # Extract #-isosurface
	# vertices, triangles = mcubes.marching_cubes(ArrayDicom, 0)
	# #print type(vertices) #nparray
	# #print type(triangles) #nparray
	# print "Done with marching cubes algorithm"

	# # Export the result
	# mcubes.export_obj(vertices, triangles, args["output"] + ".obj")
	# print "File saved as obj"

	# # Convert to stl
	# m = obj.Obj(args["output"] + ".obj")
	# m.save_stl(args["output"] + ".stl")
	# print "Converted to stl"


################################################################

	verts, faces, normals, values = measure.marching_cubes_lewiner(ArrayDicom, 0.0) 

	import numpy as np
	import dicom
	import os
	import matplotlib.pyplot as plt
	from glob import glob
	from mpl_toolkits.mplot3d.art3d import Poly3DCollection
	import scipy.ndimage
	from skimage import morphology
	from skimage import measure
	from skimage.transform import resize
	from sklearn.cluster import KMeans
	from plotly import __version__
	from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
	from plotly.tools import FigureFactory as FF
	from plotly.graph_objs import *

	def plotly_3d(verts, faces):
		x,y,z = zip(*verts) 
		
		print "Drawing"
		
		# Make the colormap single color since the axes are positional not intensity. 
	#    colormap=['rgb(255,105,180)','rgb(255,255,51)','rgb(0,191,255)']
		colormap=['rgb(236, 236, 212)','rgb(236, 236, 212)']
		
		fig = FF.create_trisurf(x=x,
							y=y, 
							z=z, 
							plot_edges=False,
							colormap=colormap,
							simplices=faces,
							backgroundcolor='rgb(64, 64, 64)',
							title="Interactive Visualization")
		iplot(fig)

	def plt_3d(verts, faces):
		print "Drawing"
		x,y,z = zip(*verts) 
		fig = plt.figure(figsize=(10, 10))
		ax = fig.add_subplot(111, projection='3d')

		# Fancy indexing: `verts[faces]` to generate a collection of triangles
		mesh = Poly3DCollection(verts[faces], linewidths=0.05, alpha=1)
		face_color = [1, 1, 0.9]
		mesh.set_facecolor(face_color)
		ax.add_collection3d(mesh)

		ax.set_xlim(0, max(x))
		ax.set_ylim(0, max(y))
		ax.set_zlim(0, max(z))
		ax.set_axis_bgcolor((0.7, 0.7, 0.7))
		plt.show()


	plt_3d(verts, faces)


################################################################

	# import vtkInterface
	# # pip2 install vtk
	# # pip2 install vtkInterface
	# # Filetype must be either "ply", "stl", "g3d" or "vtk"
	# # http://vtkinterface.readthedocs.io/en/latest/polydata.html#mesh-manipulation-and-plotting
	# # mesh = vtkInterface.PolyData(args["output"] + ".stl")
	# mesh = vtkInterface.PolyData("pelvis.stl")
	# mesh.Clean()
	# mesh = mesh.TriFilter()
	# # mesh = mesh.Subdivide(1, subfilter="loop")
	# mesh.Plot(color='orange')

################################################################

	# mesh = pymesh.load_mesh(args["output"] + ".obj")
	# mesh, info = pymesh.split_long_edges(mesh, rel_threshold=0.3, preserve_feature=True)
	# mesh, info = pymesh.collapse_short_edges(mesh, rel_threshold=0.1, preserve_feature=True)
	# mesh, info = pymesh.remove_duplicated_faces(mesh)
	# mesh, info = pymesh.remove_isolated_vertices(mesh)
	# mesh, info = pymesh.remove_duplicated_vertices(mesh, tol=.1)

	# pymesh.save_mesh("filename.obj", mesh)