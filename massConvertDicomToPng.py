from medpy.io import load
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse
import dicom
import os
import numpy
from matplotlib import pyplot, cm
import multiprocessing

def convertDCM_PNG((start,end)):
	count = start
	for filename in lstFilesDCM[start:end]:
		print(count)
		# On-screen, things will be displayed at 80dpi regardless of what we set here
		# This is effectively the dpi for the saved figure. We need to specify it,
		# otherwise `savefig` will pick a default dpi based on your local configuration
		dpi = 80

		i, h = load(filename)
		height, width = i.shape

		# What size does the figure need to be in inches to fit the image?
		figsize = width / float(dpi), height / float(dpi)

		# Create a figure of the right size with one axes that takes up the full figure
		fig = plt.figure(figsize=figsize)
		ax = fig.add_axes([0, 0, 1, 1])

		# Hide spines, ticks, etc.
		ax.axis('off')

		# Display the image.
		ax.imshow(i, cmap = cm.Greys_r)

		# Ensure we're displaying with square pixels and the right extent.
		# This is optional if you haven't called `plot` or anything else that might
		# change the limits/aspect.  We don't need this step in this case.
		ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)

		fig.savefig('dcm_pngs/image_' +str(count) + '.png', dpi=dpi, transparent=True)
		plt.show()
		count += 1


if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-s", "--start", required=True,
		help="path to the input images")
	ap.add_argument("-e", "--end", required=True,
		help="output file directory")
	args = vars(ap.parse_args())

	#PathDicom = args["path"]
	#PathDicom = "/Volumes/Seagate Backup Plus Drive/Kaggle CT Lung Canger/stage2/"
	PathDicom = "/media/aether/My Passport/Medical Images Data/Kaggle CT Lung Canger/stage1/"
	#lstFilesDCM = []  # create an empty list
	dcmFolders = []
	folderNames = []

	# Get the dcm sub dirs
	for dirName, subdirList, fileList in os.walk(PathDicom):

		#print len(subdirList) # every subdir
		#print fileList # every .dcm file of every directory
		for folderName in subdirList:
			dcmFolders.append(os.path.join(dirName, folderName))
			folderNames.append(folderName)
		break


	start = int(args["start"])
	end = int(args["end"])
	folder_num = 0
	# Loop through all dcm folders
	for folders in dcmFolders:
		if folder_num == end: break
		# loop though every dcm file in each folder
		for dirName, subdirList, fileList in os.walk(folders):
			print "Folder " + folderNames[folder_num] + " has " + str(len(fileList)) + " files"
			print "Folder # " + str(folder_num) + "/" + str(len(dcmFolders))
			# Loop though each dcm file
			if folder_num == end: break
			if folder_num >= start:	#
				count = 0
				# looping though every dcm file in each folder
				for dcmFiles in fileList:
					print str(count) #+ " : " + dcmFiles
					filePath = os.path.join(folders, dcmFiles)

					dpi = 80

					try:
						i, h = load(filePath)
					except Exception as e:
						print("Exception - failed to load " + str(count))
						count += 1
						continue

					height, width = i.shape


					# What size does the figure need to be in inches to fit the image?
					figsize = width / float(dpi), height / float(dpi)

					# Create a figure of the right size with one axes that takes up the full figure
					fig = plt.figure(figsize=figsize)
					ax = fig.add_axes([0, 0, 1, 1])

					# Hide spines, ticks, etc.
					ax.axis('off')

					# Display the image.
					ax.imshow(i, cmap = cm.Greys_r)

					# Ensure we're displaying with square pixels and the right extent.
					# This is optional if you haven't called `plot` or anything else that might
					# change the limits/aspect.  We don't need this step in this case.
					ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)

					output_path = "/media/aether/My Passport/Kaggle CT Lung Canger/stage1_pngs/" + folderNames[folder_num]
					if not os.path.exists(output_path):
					    os.makedirs(output_path)
					fig.savefig(output_path + '/' + str(count) + '.png', dpi=dpi, transparent=True)
					#fig.savefig(output_path + '/' + dcmFiles.split('.')[0] + '.png', dpi=dpi, transparent=True)
					# plt.show()
					count += 1

			folder_num += 1
