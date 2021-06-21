import math
import statistics as stats 
from stat_python import mean,standard_deviation
import csv

with open("/home/priyanka/statistics/computersales.csv",newline="") as csv_file:
    reader = csv.reader(csv_file)
    sales_data = list(reader)

    
    


def get_string_data_from_csv(index):
    data_list =[0]*40
    data_dict = {}
    
    for i in range(len(sales_data)):
        data_list[i] = sales_data[i][index]
        

    del data_list[0]

    data_set = set(data_list)
    
    unique_list = list(data_set)
    
    
    for i in range(0,len(unique_list)):
        num_of_items = data_list.count(unique_list[i])
        data_dict[unique_list[i]] = num_of_items
        
    return data_dict
print(get_string_data_from_csv(2))


def get_key_profit_list(index,data_dict):
    profit_dict = {}
    for key in data_dict.keys():
        profit_dict[key] = []
        #import pdb; pdb.set_trace()
        for i in range(1,len(sales_data)):
            if key == sales_data[i][index]:
                profit_dict.setdefault(key,[]).append(float(sales_data[i][8]))

    return profit_dict  

dic = get_string_data_from_csv(2)
a = get_key_profit_list(2,dic)
print(a)

def get_standard_deviation(data_dict):
    sd_dict = {}
    for key in data_dict.keys():
        sd_dict[key] = stat_python.standard_deviation(*data_dict[key])
    return sd_dict


def get_profit_mean_category_dict(data_dict):
    profit_mean_dict = {}
    for key in data_dict.keys():
        profit_mean_dict[key] = mean(*data_dict[key])
        #import pdb; pdb.set_trace()
    return profit_mean_dict



b = get_profit_mean_category_dict(a)
print(b)



def get_profit_std_dev_dict(data_dict):
    profit_std_dev_dict = {}
    for key in data_dict.keys():
        profit_std_dev_dict[key] = standard_deviation(*data_dict[key])
    return profit_std_dev_dict

sd_dev = get_profit_std_dev_dict(a)
print(sd_dev)


def get_coffecient_variation(data_dict):
    coef_var = {}
    for key in data_dict.keys():
        coef_var[key] = standard_deviation(*data_dict[key])
    return coef_var

cof_var = get_profit_std_dev_dict(a)
print(cof_var)


# def get_mean_profit_data(title,index):
#     print(title + "Data")
    
#     category_dict = get_string_data_from_csv(index)
#     print(category_dict)
#     print(f"{title} Profit List :{get_key_profit_list(3,category_dict)}")      
#     print(f"{title} Profit Mean :{get_profit_mean_category_dict(get_key_profit_list(3,category_dict))}\n")      

# get_mean_profit_data("Sex",3)
# get_mean_profit_data("State",6)
# get_mean_profit_data("Product Company",7)
# get_mean_profit_data("Product Type",9)
# get_mean_profit_data("Lead Source",14)
# get_mean_profit_data("Sex",3)

def get_range_data(index,max_rng_list):
    range_dict = {}
    range_index = 0
    for i in range(0,len(max_rng_list)):
        rng_key = "rng_" + str(range_index) + "_" +str(max_rng_list[i])
        range_dict[rng_key] = 0
        range_index = int(max_rng_list[i]+1)
        
    for key in range_dict.keys():
        rng_list = key.split("_")
        low_range = rng_list[1]
        high_range = rng_list[2]
        
        for i in range(1,len(sales_data)):
            
            if int(low_range)<int(sales_data[i][index]) <= int(high_range):
                 range_dict[key] += 1
                 
        return range_dict

my_list = [29,39,49,59]
age_dict =get_range_data(3,my_list)
print(age_dict)

def get_range_profit_list(index,data_dict):
    profit_dict={}
    for key in data_dict.keys():
        profit_dict[key] = []
        rng_list = key.split("_")
        low_range =rng_list[1]
        high_range = rng_list[2]

        for i in range(1,len(sales_data)):
            if int(low_range) < int(sales_data[i][index]) <= int(high_range):
                profit_dict.setdefault(key,[]).append(float(sales_data[i][13]))
        return profit_dict

def get_range_profit_mean_category_dict(index,data_dict):
    profit_mean_dict = {}
    for key in data_dict.keys():
        profit_mean_dict[key]= []
        
        rng_list = key.split("_")
        low_range =rng_list[1]
        high_range = rng_list[2]
        for i in range(1,len(sales_data)):
            if int(low_range) < int(sales_data[i][index]) <= int(high_range):
                profit_mean_dict.setdefault(key,[]).append(float(sales_data[i][13]))
                import pdb ; pdb.set_trace()
                profit_mean_dict[key] = stats.mean(*profit_mean_dict[key])
        return profit_mean_dict
print(get_key_profit_list(4,age_dict))
print(get_range_profit_mean_category_dict(3,age_dict))





