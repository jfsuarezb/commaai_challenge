import requests
import os
import cv2
import numpy as np
from skimage.transform import resize
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

	Img_Array = []
	
	print("Pair_Images_From_Video: Getting array representation from video frames")
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == False:
			break
		cv2.imwrite(os.path.join(temp_dir, frame_file + ".jpg"), frame)
		Img_Array.append(plt.imread(os.path.join(temp_dir, frame_file + ".jpg")))
		os.remove(os.path.join(temp_dir, frame_file + ".jpg"))

	cap.release()
	cv2.destroyAllWindows()
	
	os.rmdir(temp_dir)

	print("Pair_Images_From_Video: Reshaping array to pair images")
	New_Img_Array = []

	for i in range(len(Img_Array)):
		if i == len(Img_Array) - 1:
			break
		New_Img_Array.append([Img_Array[i], Img_Array[i+1]])

	del Img_Array

	return np.array(New_Img_Array)

def Resize_Paired_Images(array):
	print("Resize_Paired_Images: Resizing images to 255,255")
	return [[resize(image_pair[0], (255,255)).astype("float32"), resize(image_pair[1], (255,255)).astype("float32")]for image_pair in array]

def Load_Sampled_Data(data):
	sampled_data_dir = "testing_data"
	sampled_data_file = "testing.txt"
	with open(os.path.join(sampled_data_dir, sampled_data_file), "w") as data_file:
		for data_point in data:
			data_file.write("%s\n" % str(data))
