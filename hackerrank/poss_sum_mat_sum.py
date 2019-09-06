# Python3 program to find the sum of all 
# possible submatrices of a given Matrix 
n = 3

# Function to find the sum of all 
# possible submatrices of a given Matrix 
def matrixSum(arr) : 
	
	# Variable to store the required sum 
	sum = 0

	# Nested loop to find the number of 
	# submatrices, each number belongs to 
	for i in range(n) : 
		for j in range(n) : 

			# Number of ways to choose 
			# from top-left elements 
			top_left = (i + 1) * (j + 1)
			print(top_left)
			# Number of ways to choose 
			# from bottom-right elements 
			bottom_right = (n - i) * (n - j)
			print(bottom_right)
			sum += (top_left * bottom_right *arr[i][j])

	return sum

# Driver Code 
if __name__ == "__main__" : 
	arr = [[ 1, 1, 1 ], 
		[ 1, 1, 1 ], 
		[ 1, 1, 1 ]]

	print(matrixSum(arr)) 
	

