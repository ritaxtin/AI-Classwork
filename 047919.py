>>> import math
>>> list= [23,34,56,78,123,45,67,89,12,56]
>>> mean=(sum(list)/len(list))

>>> def findvar(list, mean):
	var=0
	for value in list:
		var+=(value-mean)**2
	variance=(sum(var))/len(list)
	print variance
	finddev(variance)

	
>>> def finddev(variance):
	dev= math.sqrt(variance)
	print dev

	
>>> findvar(list, mean)
