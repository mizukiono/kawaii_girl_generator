import os
import os.path as osp
import sys
from urllib.request import urlretrieve

MODEL_URL = "https://github.com/xiong-jie-y/kawaii_girl_generator/releases/download/v0.01_model/sgan-256-ver0.01.pkl"
FILE_NAME = "sgan-256.pkl"

os.makedirs('models', exist_ok=True)

def show_progress(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

urlretrieve(
    MODEL_URL, osp.join('models', FILE_NAME), show_progress)