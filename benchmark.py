import time 
import gc 
import random

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot] 
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quicksort(left) + middle + quicksort(right)

def perform_iterations(n):
	# Generate a random list of integers
	arr = [random.randint(0, 1000000) for _ in range(n)] 
	quicksort(arr) # Perform quicksort on the list
	
def benchmark():
	iterations = 1000000 # Adjust this value based on your experiment 
	gc.collect() # Clear any lingering garbage
	start_time = time.time()
	perform_iterations(iterations)
	end_time = time.time()

	return end_time - start_time # Return the elapsed time
	
if __name__ == "__main__":
	# Perform the benchmark once and print the elapsed time 
	elapsed_time = benchmark()
	print(f"Elapsed time: {elapsed_time:.5f} seconds")
