import common

def main():
	print("Are you sure you want to clear the cache? This will remove all your releases and updates in the cache!")
	print("Press 0 to cancel, else to proceed.")
	input = raw_input()
	if input=='0': return
	common.ClearCache()
	common.PrepareCache()

if __name__ == "__main__":
	main()