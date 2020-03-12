<hr>

# Measure RPs Activity


## Code Directions:

1. Make a function that uses a tic id as an input
2. You need to open the data files (flux, time, fluxerr)
...Don't forget to use the correct path
3. Put the data arrays into the model
4. Measure a rotation period using lomb-scargle
5. Return the rotation period


###### Test your function in increments
###### What would happen if you gave your function a star id that wasn't cleaned yet?


.
.
.





<hr>

# Handling Raised Errors




### try, except, else

-  `try` lets you try some code but instead of throwing an error will execute the `except` statment if an error occurs - so your code won't stop running at the first error
-  It is good practice to only use `except` with the exact error types you are expecting. You should also print something acknowledging why the function didn't perform as expected.
-  `else` must follow all `except` clauses and is where your code should go if the try statement works



### pass, continue

##### `pass` = there's no code to execute here
##### `continue` = there's no code to execute here, start next iteration 