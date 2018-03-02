
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

if __name__ == '__main__':

	all_imgs = []

	#paths = ["/home/aether/Desktop/Medical Image Segmentation/bones-unet/pelvis_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/shoulder_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/head_thresh_predictions/" ]
	paths = ["/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_pelvis_thresh_predictions/", "/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_shoulder_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_head_thresh_predictions/" ]
	#paths = ["/home/aether/Desktop/Medical Image Segmentation/bones-unet/BONE_CT/test/female_pelvis (perfect, begin at 51)", "/home/aether/Desktop/Medical Image Segmentation/bones-unet/BONE_CT/test/female_shoulder","/home/aether/Desktop/Medical Image Segmentation/bones-unet/BONE_CT/test/female_head" ]
	# female + hips
	#paths = ["/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_hip_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_pelvis_thresh_predictions/", "/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_shoulder_thresh_predictions/","/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_head_thresh_predictions/" ]

	count = 0
	for path in paths:
		for dirName, subdirList, fileList in os.walk(path):
			natural_sort(fileList)
			for filename in fileList:
				print(filename)
				if ".png" in filename.lower():  # check whether the file's png
					img = misc.imread(os.path.join(dirName,filename))
					misc.imsave("all_ct_thresh_pngs/img" + str(count) + ".png", img )
					count += 1
					