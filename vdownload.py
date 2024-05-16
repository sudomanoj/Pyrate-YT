from pytube import YouTube
from time_calc import calculate_time
import os
from tqdm import tqdm
import sys
import time

def progress_bar(stream, chunk, bytes_remaining):
    global pbar
    pbar.update(len(chunk))

def playlist_download(url):
	pass

def video_download(url):
	yt = YouTube(url, on_progress_callback=progress_bar)
	path = input("Enter the path to save the video or press enter to download to current directory : ")
	if path == "":
		print("Downloading to current directory.")
	else:
		print(f"Downloading to {path}")
	print("Fetching video details...")
	print(f"Title: {yt.title}")
	print(f"Views: {yt.views}")
	calculate_time(yt.length)
	try:
		print(f"Likes: {yt.likes}")
	except:
		print("Likes: Not available")
	print(f"Downloading: {yt.title}")
	stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	file_size = stream.filesize
	global pbar
	pbar = tqdm(total=file_size, unit='B', unit_scale=True, desc='Downloading: ', ascii=False, ncols=100)
	stream.download(output_path=path)
	pbar.close()
	print("Download completed!!")
