import os, shutil, sys, time, zipfile, logging, ctypes
from zlib import crc32

from settings import *

logging.basicConfig(level=logging.INFO, format = '%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class VersionInfo:

	def __init__(self, versionString, updateTime):
		self.versionCode = versionString.split(':')[0]
		self.updateNum = int(versionString.split(':')[1])
		self.updateTime = updateTime

class NeededZipInfo:

	def __init__(self, CRC, date_time):
		self.date_time = date_time
		self.CRC = CRC

#Not working..
def MakeSymbolicLink(src, dest):
	kdll = ctypes.windll.LoadLibrary("kernel32.dll")
	if kdll: 
		kdll.CreateSymbolicLinkA(src, dest, 0)
		return True
	else:
		return False

# cache structure
# CACHE_PATH
# |---latest.txt
# |---versions
	# |---(version1)
		# |---update1
			# |.cache files
			# ...
		# |---update2
			# |.cache files
			# ...
		# |...
	# |---(version2)
		# |...
	# |...
def PrepareCache():
	latestPath = LATEST_PATH
	if os.path.exists(latestPath):
		logging.error("Latest version already exists!")
		return
	if not os.path.exists(CACHE_PATH): os.mkdir(CACHE_PATH)
	if not os.path.exists(EXTERNAL_CACHE_PATH): os.mkdir(EXTERNAL_CACHE_PATH)
	if not os.path.exists(UPDPKG_PATH): os.mkdir(UPDPKG_PATH)
	latestFile = open(latestPath, 'w')
	WriteVersionInfoToLatestFile(latestFile, VersionInfo("0.1.0:1","1970.1.1.0.0.0"))
	MakeNewVersion("0.1.0")

def ClearCache():
	if os.path.exists(CACHE_PATH): shutil.rmtree(CACHE_PATH)
	if os.path.exists(UPDPKG_PATH): shutil.rmtree(UPDPKG_PATH)
	if os.path.exists(LATEST_PATH): os.remove(LATEST_PATH)

def UpdateCache():
	# check if latest.txt is present
	latestPath = LATEST_PATH
	if not os.path.exists(latestPath):
		logging.error("Latest version cannot be found! Please run init!")
		return
	latestFile = open(latestPath)
	# read version info
	versionInfo = ReadVersionInfoFromLatestFile(latestFile)
	if not versionInfo: return
	versionCachePath = os.path.join(CACHE_PATH, versionInfo.versionCode)
	if not os.path.exists(versionCachePath):
		logging.error("Version has not been released!")
		return
	# extract new info to a new update path
	lastUpdatePath = os.path.join(versionCachePath, "%d" % versionInfo.updateNum)
	newUpdatePath = os.path.join(versionCachePath, "%d" % (versionInfo.updateNum+1))
	if os.path.exists(newUpdatePath):
		logging.error("Update cache already exists!")
		return
	os.mkdir(newUpdatePath)
	success = ProcessFilenamesFromListFile(newUpdatePath, lastUpdatePath)
	if not success: 
		#shutil.rmtree(newUpdatePath)
		logging.info("Nothing to update!")
		return
	versionInfo.updateNum += 1
	versionInfo.updateTime = "%s.%s.%s.%s.%s.%s"%time.localtime()[0:6]
	latestFile = open(latestPath, 'w')
	WriteVersionInfoToLatestFile(latestFile, versionInfo)

def CompareCache():
	# check if latest.txt is present
	latestPath = LATEST_PATH
	if not os.path.exists(latestPath):
		print("Latest version cannot be found! Please run init!")
		return
	latestFile = open(latestPath)
	# read version info
	versionInfo = ReadVersionInfoFromLatestFile(latestFile)
	if not versionInfo: return
	versionCachePath = os.path.join(CACHE_PATH, versionInfo.versionCode)
	if not os.path.exists(versionCachePath):
		print("Version has not been released!")
		return
	# extract new info to a new update path
	lastUpdatePath = os.path.join(versionCachePath, "%d" % versionInfo.updateNum)
	externalComparePath = EXTERNAL_CACHE_PATH
	different = ProcessFilenamesFromListFile(lastUpdatePath, externalComparePath)
	if not different: 
		#shutil.rmtree(newUpdatePath)
		logging.info("Equal!")
	else:
		logging.info("Differrent! An update package has been generated!")
	
def ReadVersionInfoFromLatestFile(latestFile):
	versionString = None
	updateTime = None
	for line in latestFile.readlines():
		splits = line.strip().split('\t')
		if len(splits)>1 and splits[0].lower() == "version": versionString = splits[1]
		elif len(splits)>1 and splits[0].lower() == "time": updateTime = splits[1]
	if not (versionString and updateTime):
		logging.error("Latest file is not valid!")
		return
	return VersionInfo(versionString, updateTime)

def WriteVersionInfoToLatestFile(latestFile, versionInfo):
	latestFile.write("Version\t%s:%d\n" % (versionInfo.versionCode, versionInfo.updateNum))
	latestFile.write("Time\t%s" % versionInfo.updateTime)
	latestFile.close()

# release a new version and create the cache folder
def MakeNewVersion(versionCode):
	versionCachePath = os.path.join(CACHE_PATH, versionCode)
	if os.path.exists(versionCachePath):
		logging.error("Error! Version has been released!")
		return
	os.mkdir(versionCachePath)
	newUpdatePath = os.path.join(versionCachePath, "1")
	os.mkdir(newUpdatePath)
	ProcessFilenamesFromListFile(newUpdatePath)

def ProcessFilenamesFromListFile(outputPath, comparePath=None):
	listFile = open(FILELIST_PATH)
	isDifferent = False
	if not comparePath: isDifferent=True
	for line in listFile.readlines():
		logging.info("Processing %s ..." % line)
		input = os.path.join("../..", line.strip())
		zipFile = OpenZipFile(input)
		newInfo = ExtractZipInfo(zipFile)
		if not zipFile or not newInfo: continue
		outputFileBase = input.replace('/','~').replace('\\','~')
		outputFilename = outputFileBase+".cache"
		if comparePath:
			zipInfoFile = open(os.path.join(comparePath, outputFilename), 'r')
			lastInfo = ReadZipInfoFromFile(zipInfoFile)
			if not lastInfo: continue
			updateList, deleteList = CompareInfo(lastInfo, newInfo)
			if len(updateList)>0 or len(deleteList)>0: 
				isDifferent=True
				updatePackagePath = os.path.join(UPDPKG_PATH, outputFileBase+".zip")
				updatePackageFile = OpenZipFile(updatePackagePath, 'w', zipfile.ZIP_DEFLATED) #using compression
				MakeUpdatePackage(zipFile, updatePackageFile, updateList, deleteList)
				outputFile = open(os.path.join(outputPath, outputFilename), 'w')
				WriteZipInfoToFile(newInfo, outputFile)
			else:
				#Make a symbolic link
				#if not (MakeSymbolicLink(os.path.abspath(os.path.join(comparePath, outputFilename)), os.path.abspath(os.path.join(outputPath, outputFilename)))):
				outputFile = open(os.path.join(outputPath, outputFilename), 'w')
				WriteZipInfoToFile(newInfo, outputFile)
		else:
			outputFile = open(os.path.join(outputPath, outputFilename), 'w')
			WriteZipInfoToFile(newInfo, outputFile)
			
	listFile.close()
	return isDifferent

def OpenZipFile(input, mode='r', compression=zipfile.ZIP_DEFLATED, allowZip64=False):
	try:
		file = zipfile.ZipFile(input, mode, compression, allowZip64)
	except IOError:
		logging.warning("No such file: %s" % input)
	except zipfile.BadZipfile:
		logging.error("%s is not a valid zip file!" % input)
	except zipfile.LargeZipFile:
		logging.error("%s is too large to open!" % input)
	except RuntimeError:
		logging.error("Compress method not supported in %s!" % input)
	else:
		return file

def ExtractZipInfo(file):
	if file:
		# append crc-32 of the input filename to the cache filename
		#cacheName = '%x' % (crc32(input) & 0xffffffff)
		info = {}
		for i in file.infolist():
			info[i.filename] = i
		return info
	return

def OpenZipAndExtractInfo(file):
	file = OpenZipFile(input)
	return ExtractZipInfo(file)

def WriteZipInfoToFile(info, file):
	for filename in info:
		#TODO: find a better way to record filename
		file.write("%s\t%d\t%s\n" % (filename, info[filename].CRC, "%s.%s.%s.%s.%s.%s" % info[filename].date_time))
	file.close()

def ReadZipInfoFromFile(file):
	info = {}
	try:
		for line in file.readlines():
			(filename, CRCstring, datetimeString) = line.strip().split('\t')
			finename = filename.strip('\"')
			info[filename] = NeededZipInfo(long(CRCstring), tuple([int(num) for num in datetimeString.split('.')]))
	except:
		logging.error("Cannot read info from file %s!" % file.name)
	file.close()
	return info

# returns updateList and deleteList
def CompareInfo(lastInfo, newInfo):
	updateList = []
	deleteList = []
	# newInfoLK = {}
	# for filename in newInfo:
		# newInfoLK[filename.lower()] = newInfo[filename]
	newInfoFilenames = newInfo.keys()
	# TODO: process add list
	for filename in lastInfo:
		if filename in newInfo: # python is case sensitive
		# if filename.lower() in newInfoLK:
			if newInfo[filename].date_time != lastInfo[filename].date_time and newInfo[filename].CRC != lastInfo[filename].CRC:
				updateList.append(filename)
			newInfoFilenames.remove(filename)
		else:
			deleteList.append(filename)
	for filename in newInfoFilenames:
		updateList.append(filename)
	return updateList, deleteList

def MakeUpdatePackage(oldFile, newFile, updateList, deleteList):
	# try:
	# Add files to update
	for filename in updateList:
		bytes = oldFile.read(filename)
		newFile.writestr(filename, bytes)
	# Add files to delete
	if len(deleteList)>0:
		with open("deleteList.txt", 'w') as deleteListFile:
			for name in deleteList:
				logging.debug("File to delete: %s" % name)
				deleteListFile.write("%s\n" % name)
		newFile.write("deleteList.txt")
		os.remove("deleteList.txt")
	# except:
		# logging.error("MakeUpdatePackage failed!")
	
	oldFile.close()
	newFile.close()
	return

# Test cache
def main():
	ClearCache()
	PrepareCache()
	UpdateCache()
	CompareCache()

if __name__ == "__main__":
	main()
