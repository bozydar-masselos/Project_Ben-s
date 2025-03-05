I have created 2 functions that calculate day5 results for each formula and 1 more function that writes the results one the next empty column of the
analyzed csv file.

Part1:
As you can see in ./experiments_1.csv  column: n5 expected, the result expected from 
the formula is much different than that of experimental data. Formula from the boss was not correct.

Part2
##The expected result after 5 days matches exactly the result observed by Melissa. 4-decimal digit round was used at each
step of the recursive function to obtain this result. So the pressure inclusive formula is correct.

Part3 time=inf
So to see if expected values correspond to time travellers' data I manually run the function for 10, 30, 50, 150 days and
the results are saved in columns named respecitvely, in the same file (./experiments_2.csv). For the 150days time mark the
output strongly approaches the TimeTravellers' measurement. So the data is correct. 