import common

def main():
	print("Input the version code of the new release.(e.g. 0.1.1)")
	versionCode = raw_input()
	while versionCode.find(':')>=0:
		print("Version code should not have ':' charactor.")
		versionCode = raw_input()
		
	common.MakeNewVersion(versionCode)

if __name__ == "__main__":
	main()