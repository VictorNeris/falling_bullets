import common
import os, shutil

from settings import *

def main():
	if os.path.exists(UPDPKG_PATH): shutil.rmtree(UPDPKG_PATH)
	os.mkdir(UPDPKG_PATH)
	common.CompareCache()

if __name__ == "__main__":
	main()