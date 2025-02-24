
import csv
import os
n0_ex1={}
n5_ex1={}
t_ex1={}
with open("./experiments_1.csv") as exp1_file:
    exp1_data= csv.DictReader(exp1_file)
    cntr1=0
    for row in exp1_data:
        n0_ex1[cntr1]= float(row['n0'])
        t_ex1[cntr1]= float(row['t'])
        n5_ex1[cntr1]= float(row['n5']) 
        cntr1+=1

#print(n0)
#print(t) 

n5exp={}
##n5exp= function with formula * n0!!

def growth_function(temp,lastday_mass,endday):  ##This is the function from the boss. ##This function calculates the mass at ith day (nextday_mass)
    nextday_mass=temp*lastday_mass
    if endday == 0:
        return ValueError 
    if endday == 1: 
        return float(nextday_mass) 
    if endday >=2: 
        return (growth_function(temp, nextday_mass, (int(endday)-1)))

def growth_fun_under_pressure(temp,pressure,lastday_mass,endday):       ##This is the function for the pressure-inclusive formula. 
    nextday_mass= (temp*lastday_mass)-(pressure*(lastday_mass ** 2))
    if endday == 0:
        return ValueError 
    if endday == 1: 
        return float(nextday_mass)
    if endday >=2: 
        return (growth_function(temp, nextday_mass, (int(endday)-1))) 
    
'''for i in range(1,6):
    print(growth_function(2,1,i))
    print(growth_fun_under_pressure(2,0.5,1,i)) '''

for j in range(0,cntr1):
    n5exp[j]= (growth_function(t_ex1[j],n0_ex1[j],5))
 

##Next function writes everynext column of the input .csv file with the data from a dictionary!! ##

def add_new_csv_column(file_path,column_name,dict_data): 
    new_column_values=[]
    local_dic=dict_data
    with open(file_path, 'r', newline='') as exp1_file:
        reader= list(csv.reader(exp1_file))
        header= reader[0]+[column_name]
        for i,row in enumerate(reader[1:]):
            
            new_value=local_dic[i]
            new_column_values.append(new_value)             #This line is not necessary. it just has the values of n5exp dic without the keys as a list. 
            row.append(str(new_value))
        
    with open(file_path, 'w', newline='') as exp1_file:
    
            writer = csv.writer(exp1_file)
            writer.writerow(header)             # Write updated header
            writer.writerows(reader[1:])        # Write updated data
    return print('column added:', column_name,'values added:', new_column_values)

#add_new_csv_column("./experiments_1.csv", "n5expected", n5exp)  ##THIS COMMANDS WRITES RESULTS FOR PART1


###NEXT STEP --> I need to statistically check if expected results match observed results. ?Maybe not? RESULTS seem way too off
###and the formua probably wasn't correct. 

##Part 2
underpressure={}

n0_ex2={}
n5_ex2={}
t_ex2={}
prsr_ex2={}
with open("./experiments_2.csv") as exp2_file:
    exp2_data= csv.DictReader(exp2_file)
    cntr2=0
    for row in exp2_data:
        n0_ex2[cntr2]= float(row['n0'])
        t_ex2[cntr2]= float(row['t'])
        n5_ex2[cntr2]= float(row['n5']) 
        prsr_ex2[cntr2]=float(row['p']) 
        cntr2+=1

for j in range(0,cntr2): 
    underpressure[j]=growth_fun_under_pressure(t_ex2[j], prsr_ex2[j], n0_ex2[j], 5)

print(underpressure)

#add_new_csv_column("./experiments_2.csv", "n5_expected", underpressure) ##THIS COMMANDS WRITES RESULTS FOR PART1



###I THINK that result she is getting should be after two days with this formula. So result or formula is wrong. 
###Basically results for day=inf are almost the same as for day 5 meaning that already at day 5 the cells have reach their maxim growth state and cannot 
###actually grow more. 
###The cells are very likely to have reached their max growth even before day 5. Knowing that bac have an exponential growth we should be treating the 
### formula with caution and understand that most likely it is relevant onl for part of the life cycle of th bact cuture. 