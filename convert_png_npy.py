import numpy as np
import os
import argparse
import scipy.misc as misc
import matplotlib.pyplot as plt


# python2 convert_png_npy.py -p /Users/aether/Documents/Dicom2Mesh/testing

if __name__ == '__main__':
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--path", required=True,
		help="path to the input images")
	args = vars(ap.parse_args())

	all_imgs = []

	print(args["path"])

	for dirName, subdirList, fileList in os.walk(args["path"]):
		for filename in fileList:
			print(filename)
			if ".png" in filename.lower():  # check whether the file's png
				img = plt.imread(os.path.join(dirName,filename))
				all_imgs.append(img)

	all_imgs = np.dstack(all_imgs)

	print(all_imgs.shape)

	np.save("all_img.npy", all_imgs)