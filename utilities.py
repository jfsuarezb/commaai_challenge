import requests
import os
import cv2
from matplotlib import pyplot as plt

#Downloads files from internet
def Download_File(url, path, name):
	response = requests.get(url, stream=True)
	print("DownloadFile: Connection Established")
	with open(os.path.join(path, name), "wb") as f:
		print("DownloadFile: Writting File")
		for chunk in response.iter_content(chunk_size=1024):
			f.write(chunk)
	return os.path.join(path, name)

#Pair images into tuples for proper input
def Pair_Images_From_Video(path):
	temp_dir = "frame_tmp"
	frame_file = "frame"

	os.mkdir(temp_dir)

	print("Pair_Images_From_Video: Capturing video")
	cap = cv2.VideoCapture(path)
	
	print("Pair_Images_From_Video: Reading frames into temp dir")
	i = 0
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == False:
			break
		cv2.imwrite(os.path.join(temp_dir, frame_file + str(i)))
		i += 1

	cap.release()
	cv2.destroyAllWindows()

	Img_Array = []

	print("Pair_Images_From_Video: Reading images from files into array")
	for i in range(len(os.listdir(temp_dir))):
		Img_Array.append(plt.imread(os.path.join(temp_dir, frame_file + str(i))))
		os.remove(os.path.join(temp_dir, frame_file + str(i)))
	
	os.rmdir(temp_dir)

	print("Pair_Images_From_Video: Reshaping array to pair images")
	
	New_Img_Array = []

	for i in range(len(Img_Array)):
		if i == len(Img_Array) - 1:
			break
		New_Img_Array.append([Img_Array[i], Img_Array[i+1]])

	return New_Img_Array