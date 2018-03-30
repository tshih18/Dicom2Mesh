
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

	# Female fullbody threshold images path
	paths = ["/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_ankle_thresh_predictions/",
			"/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_knee_thresh_predictions/",
			"/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_hip_thresh_predictions/",
			"/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_pelvis_thresh_predictions/", 
			"/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_shoulder_thresh_predictions/",
			"/home/aether/Desktop/Medical Image Segmentation/bones-unet/f_head_thresh_predictions/"]

	foldername = "f_ct_FullBody_thresh_pngs"
	if not os.path.exists(foldername):
		os.makedirs(foldername)

	count = 0
	for path in paths:
		for dirName, subdirList, fileList in os.walk(path):
			natural_sort(fileList)
			for filename in fileList:
				print(filename)
				if ".png" in filename.lower():  # check whether the file's png
					img = misc.imread(os.path.join(dirName,filename))
					misc.imsave(foldername + "/img" + str(count) + ".png", img )
					count += 1
					