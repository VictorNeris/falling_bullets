import common, compare, update, release, clear
import os

functionTable = {
	1: common.main,
	2: compare.main,
	3: update.main,
	4: release.main,
	5: clear.main,
}

if __name__ == "__main__":
	print("BF2 Version Control Script v1.0")
	print("By worldlife123")
	idx = -1
	while idx!=0:
		print("Input number to select your choice.")
		print("0. Quit")
		print("1. Test")
		print("2. Compare")
		print("3. Update")
		print("4. Release")
		print("5. Clear")
		input = raw_input()
		print("Input is:"+input)
		try:
			idx = int(input)
			if not idx in functionTable:
				print("Invalid index.")
				continue
		except:
			print("Invalid input.")
			continue
		functionTable[idx]()