#M:Successes in Population
#N:Total population
#x:Successes in Sample
#n:Total Sample from Population

# Categorical data: what makes a thing unique 
# Numerical data : Finite Infinite
# Continuous data: which can be broken down into smaller data
# Qualitative data: Ordinal Nominal Data 

import math


def mean(*args):
    val_sum=sum(args)
    return val_sum/len(args)

print(f"Mean:{mean(1,2,3,4,5,6)}")

def median(*args):
    if len(args) % 2 == 0 :
        i = round((len(args)+1)/2)
        j = i-1
        return (args[i]+args[j])/2
    else:
        k = round((len(args)+1)/2)
        return args[k]

print(f"Median:{median(1,2,3,4,5,6)}")

def mode(*args):
    dict_vals = {i: args.count(i) for i in args}
    max_list = [k for k,v in dict_vals.items() if v == max(dict_vals.values())]
    return max_list
    
                      

print(f"Mode:{mode(2,2,3,3,4,5,6)}")


def variance (*args):
    ''' deviation of the values from the mean value 
    This shows how spread our data is around our mean'''
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i-mean_val)**2
    denominator = len(args) -1 
    try:
        answer= numerator/denominator
    except ZeroDivisionError:
        answer = numerator/1
    
    return answer
    


print(f"Variance:{variance(4,6,3,5,2)}")

def standard_deviation(*args):

    ''' Because we are going to square values for variance we are
    going to get extra values for outliers.For this reason we find the square root of the variance  '''

    var = variance(*args)
    std_dev = math.sqrt(var)
    return std_dev
print(f"Standard Deviation:{standard_deviation(4,6,3,5,2)}")


def coefficient_of_variation(*args):
    '''
    When we take the standard deviation of the values of different majors like in km and in
    miles we get almost the same values for both hence coefficient_variation is used.
     This is used to compare two measures that operate on different scales
    '''
    return standard_deviation(*args)/mean(*args)
print(f"Coefficient Variation for miles:{coefficient_of_variation(3,4,4.5,3.5)}")
print(f"Coefficient Variation for km:{coefficient_of_variation(4.82,6.437,7.242,5.632)}")

def covariance(*args):
    ''' Tells us if 2 values are moving in the same direction or not
    Earnings le market capitalization lai effect gareko xaki xaina vanne kura patta lagaunu paryo vane
    cov > 0 : Moving together,
    cov < 0 : Moving Opposite ,
    cov = 0 : Independent
    '''

    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    list_1_mean = mean(*list_1[0])
    list_2_mean = mean(*list_2[0])
    numerator = 0
    if len(list_1[0]) == len(list_2[0]):
        for i in range(len(list_1[0])):
            numerator += (list_1[0][i]-list_1_mean)*(list_2[0][i]-list_2_mean)
            denominator = len(list_1[0])-1
            return numerator/denominator
    else: 
        print("Error")        




def correlation_coefficient(*args):
    ''' Adjusts covariance to see relationships .Values are between 1 AND -1 .1 means perfectly correlated and -1 means inversly correlated and 0 means not at all'''
    list_1=[i[0] for i in args]
    list_2=[i[1] for i in args]
    list_1_sd = standard_deviation(*list_1[0])
    list_2_sd = standard_deviation(*list_2[0])
    denominator = list_1_sd * list_2_sd 
    numerator = covariance(*args)
    return numerator/denominator

m_d_list = [[1532,1488,1343,928,615],[58,35,75,41,17]]

print(f"correlation_coefficient for miles:{correlation_coefficient(m_d_list)}")


def normalize_list(*args):
    sd_list = standard_deviation(*args)
    return [(i-mean(*args))/sd_list for i in args]




dice_list = [1,2,4,4,4,5,5,5,6]
print(f"Sum:{sum(dice_list)}") 
print(f"Mean:{mean(*dice_list)}") 
print(f"Standard Deviation:{standard_deviation(dice_list)}") 
normalized_list = normalize_list(*dice_list)
print(f"Normal List:{normalize_list}")


def sample_error(*args):
    sd_list = standard_deviation(*args)
    return sd_list/(math.sqrt(len(args)))

print(f"Standard Error : {sample_error(*normalize_list)}")




