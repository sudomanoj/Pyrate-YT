import sys
import os
from pytube import YouTube
from banner import banner
# from progress_bar import progress_bar
from vdownload import video_download
from time_calc import calculate_time
from url_validation import url_validation


current_dir = os.getcwd()


def main():
    arguments = sys.argv[1:]
    if len(arguments) == 2:
    	url = arguments[1]
    	cleaned_url = url_validation(url)
    if len(arguments) == 0:
        banner()
    elif arguments[0] in ['-h', '--help']:
        banner()
    elif arguments[0] in ['-p', '--playlist']:
        banner()
        playlist_download(cleaned_url)
    elif arguments[0] in ['-v', '--video']:
        banner()
        video_download(cleaned_url)
        
    else:
        print("Invalid option. Use -h or --help for help.")

if __name__ == '__main__':
    main()
	
