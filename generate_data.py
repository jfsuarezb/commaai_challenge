from utilities import Download_File

import os

#Constants for training/testing data retrieval
training_data_dir = "training_data"
testing_data_dir = "testing_data"

training_mp4_link = "https://github.com/commaai/speedchallenge/raw/master/data/train.mp4"
training_mp4_file = "training.mp4"

training_text_link = "https://github.com/commaai/speedchallenge/raw/master/data/train.txt"
training_text_file = "training.txt"

testing_mp4_link = "https://github.com/commaai/speedchallenge/raw/master/data/test.mp4"
testing_mp4_file = "testing.mp4"

#Generate Data For Training
def Generate_Trainning_Data():
	print("Deleting old Data")
	if os.path.isdir(training_data_dir):
		for f in os.listdir(training_data_dir):
			os.remove(os.path.join(training_data_dir, f))
	os.rmdir(training_data_dir)	
	
	print("Beginning Download")
	os.mkdir(training_data_dir)
	Download_File(training_mp4_link, training_data_dir, training_mp4_file)
	Download_File(training_text_link, training_data_dir, training_text_file)
	print("Succesfully Downloaded trainning data")

Generate_Trainning_Data()
