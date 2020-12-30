import requests
import os

#Downloads files from internet
def Download_File(url, path, name):
	response = requests.get(url, stream=True)
	print("DownloadFile: Connection Established")
	with open(os.path.join(path, name), "wb") as f:
		print("DownloadFile: Writting File")
		for chunk in response.iter_content(chunk_size=1024):
			f.write(chunk)
	return os.path.join(path, name)


