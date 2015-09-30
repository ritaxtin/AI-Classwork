>>> import math
>>> list= [23,34,56,78,123,45,67,89,12,56] # generates list
>>> mean=(sum(list)/len(list)) #formulae for computing the mean

>>> def findvar(list, mean): # calculating the variance
	var=0 # initialize var
	for value in list:
		var+=(value-mean)**2 # computer the difference of the value on list from mean and squares the answer
	variance=(var)/len(list) 
	print variance
	finddev(variance)

	
>>> def finddev(variance):
	dev= math.sqrt(variance)
	print dev

	
>>> findvar(list, mean)
