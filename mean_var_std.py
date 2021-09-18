import numpy as np

def calculate(list1):

  if len(list1) != 9:
    raise ValueError("List must contain nine numbers.\n")
  
  else:
    splitList = np.split(list1, 3);

    mean1 = splitList.mean(axis = 0)
    mean2 = splitList.mean(axis = 1)
    mean3 = list1.mean

    var1 = splitList.var(axis = 0)
    var2 = splitList.var(axis = 1)
    var3 = list1.var

    std1 = splitList.std(axis = 0)
    std2 = splitList.std(axis = 1)
    std3 = list1.std

    max1 = np.amax(splitList, 0)
    max2 = np.amax(splitList, 1)
    max3 = np.amax(list1, 0)

    min1 = np.amin(splitList, 0)
    min2 = np.amin(splitList, 1)
    min3 = np.amin(list1)

    sum1 = np.sum(splitList, 0)
    sum2 = np.sum(splitList, 1)
    sum3 = np.sum(list1)

    calculations = {
      'mean': [mean1, mean2, mean3], 
      'variance:': [var1, var2, var3], 
      'standard deviation': [std1, std2, std3], 
      'max': [max1, max2, max3], 
      'min': [min1, min2, min3], 
      'sum': [sum1, sum2, sum3]
    }

    return calculations
