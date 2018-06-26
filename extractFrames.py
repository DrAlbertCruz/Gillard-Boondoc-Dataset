from os import listdir, makedirs
from os.path import isfile, join, exists, splitext, isdir
import cv2

# Video path, change this as needed
videopath = 'G:\\Gillard-Boondoc-Dataset\\raw_movies'
framepath = 'G:\\Gillard-Boondoc-Dataset\\frames'
# Get list of files in videopath
files = [f for f in listdir(videopath) if isfile(join(videopath, f))]

# Display list of video files
print('List of videos:')
print(list(files))

# Load the file
for video in files:
	# Use opencv's video capture object to load the video
	vidcap = cv2.VideoCapture(join(videopath,video))
	success,image = vidcap.read() 		# Attempt to read the first frame
	fps = vidcap.get(cv2.CAP_PROP_FPS) 	# Display FPS
	print('Video has ',fps,' fps.')		# Notify FPS to term
	count = 0							# Initialize frame counter
	success = True 						# Probably need to check here in case a first frame read fails
	savefolder = join(framepath,splitext(video)[0])
	# Create save folder path
	print('The folder to save in will be ',savefolder)
	
	# Make the folder if it doesn't exists
	if not exists(savefolder):
		print(savefolder, ' didnt exist, creating it.')
		makedirs(savefolder)
		
	while success:
		# Filename in milliseconds
		timestamp = count * 1000 // fps
		filename = str(int(timestamp)).zfill(10) + '.jpg'
		print('The file name will be ', filename)
		cv2.imwrite(join(savefolder,filename), image)
		success,image = vidcap.read()
		print('Read a new frame: ', success)
		count += 1