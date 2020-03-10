<hr>

# Masking Activity


## Code Directions:
1. Use `numpy.random.random_sample` to generate a random 2D data array in the shape of 
	20 rows and 2 columns
	- For help try to read the [API](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.random_sample.html)
2.  Use `numpy.arange(0,10,.5)` to create a time array variable
3.  Insert the time array into the random 2D data array using `numpy.insert`
	- hint start insert at `0` using `axis=1` in the arguments
4. Verify that you now have a dataframe with 20 rows and 3 columns (just like our real data)
5. Create a masking array for values in the time array between (and including) 4 & 7 
	- google python operators if unsure how to include 4 & 7 values
6. Apply this mask to every column
	- BIG hint: remove arrays from dataframe 
7. End product should be 3 masked arrays