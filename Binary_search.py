def binary_search(number,search):
	low = 0
	high = len(number)-1
	found = False
	while( low <=high and not found):
		mid = (low + high)//2
		if number[mid] == search :
			found = True
		else:
			if search < number[mid]:
				high = mid - 1
			else:
				low = mid + 1	
	return found

number = [6, 12, 17, 23, 38, 45, 77, 84, 90]
print(binary_search(number, 45))
print(binary_search(number, 41))