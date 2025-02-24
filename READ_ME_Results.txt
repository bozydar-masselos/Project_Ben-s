I have created 2x functions that calculates day5 results for each formula and 1 more function that writes the results one the next empty column of the
analyzed csv file.

Part1:
As you can see in ./experiments_1.csv  column: n5 expected, the result expected from the formula is much different than that of experimental data.

Part2
##I THINK that result she is observing is similar to the expected growth after two days (not five), given the formula. So experimenal result or formula 
is wrong. ## 

#Basically results for day=inf are almost the same as for day 5 meaning that already at day 5 the cells have reach their maxim growth state and cannot 
actually grow more. The cells are very likely to have reached their max growth even before day 5. Knowing that bac have an exponential growth we should
be treating the formula with caution and understand that most likely it is relevant only for part of the life cycle of th bacterial cuture. 