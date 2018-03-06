from medpy.io import load
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import argparse

# # On-screen, things will be displayed at 80dpi regardless of what we set here
# # This is effectively the dpi for the saved figure. We need to specify it,
# # otherwise `savefig` will pick a default dpi based on your local configuration
# dpi = 80

# # i, h = load("dicom/series-000001/image-000002.dcm")
# # i, h = load("dicom/CT-MONO2-16-brain")
# # i, h = load("dicom/Lung CT/DOI/LCTSC-Test-S1-101/1.3.6.1.4.1.14519.5.2.1.7014.4598.492964872630309412859177308186/1.3.6.1.4.1.14519.5.2.1.7014.4598.106943890850011666503487579262/000000.dcm")
# i, h = load("dicom/02ef8f31ea86a45cfce6eb297c274598/series-000002/image-000002.dcm")
# height, width = i.shape

# # What size does the figure need to be in inches to fit the image?
# figsize = width / float(dpi), height / float(dpi)

# # Create a figure of the right size with one axes that takes up the full figure
# fig = plt.figure(figsize=figsize)
# ax = fig.add_axes([0, 0, 1, 1])

# # Hide spines, ticks, etc.
# ax.axis('off')

# # Display the image.
# ax.imshow(i, cmap = cm.Greys_r)

# # Ensure we're displaying with square pixels and the right extent.
# # This is optional if you haven't called `plot` or anything else that might
# # change the limits/aspect.  We don't need this step in this case.
# ax.set(xlim=[0, width], ylim=[height, 0], aspect=1)

# fig.savefig('test3.png', dpi=dpi, transparent=True)
# plt.show()


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
	# ap = argparse.ArgumentParser()
	# ap.add_argument("-p", "--path", required=True,
	# 	help="path to the input images")
	# ap.add_argument("-o", "--output", required=True,
	# 	help="output file directory")
	# args = vars(ap.parse_args())

	#PathDicom = args["path"]
	PathDicom = "/Volumes/Seagate Backup Plus Drive/Kaggle CT Lung Canger/stage2/"
	#PathDicom = "/media/aether/My Passport/Medical Images Data/Bones/Phalanx/phalanx1_dcm/"
	lstFilesDCM = []  # create an empty list
	dcmFolders = []

	# Get the dcm sub dirs
	for dirName, subdirList, fileList in os.walk(PathDicom):

		#print len(subdirList) # every subdir
		#print fileList # every .dcm file of every directory
		for folderName in subdirList:
			dcmFolders.append(os.path.join(dirName, folderName))
		break

	#print dcmFolders

	folder_num = 7
	# Loop through all the dcm in each folder
	for folders in dcmFolders:
		if folder_num > 79:
			for dirName, subdirList, fileList in os.walk(folders):
				print "Folder has " + str(len(fileList)) + " files"
				print "Folder # " + str(folder_num) "/" + str(len(dcmF))
				# Loop though each dcm file

				count = 0
				for dcmFiles in fileList:
					print count
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

					output_path = "/Volumes/Seagate Backup Plus Drive/Kaggle CT Lung Canger/stage2_pngs/" + str(folder_num)
					if not os.path.exists(output_path):
					    os.makedirs(output_path)
					fig.savefig(output_path + '/' + str(count) + '.png', dpi=dpi, transparent=True)
					# plt.show()
					count += 1

		folder_num += 1
