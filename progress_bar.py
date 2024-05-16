import sys
from tqdm import tqdm
import time
import progress_bar

def progress_bar(stream, chunk, bytes_remaining):
    pbar = progress_bar.pbar
    pbar.update(len(chunk))
