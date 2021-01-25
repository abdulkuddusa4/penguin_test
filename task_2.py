def efficientJanitor(weight):
	n = 5
	weight = [1.01, 1.01, 1.01, 1.4, 2.4,3.0,1.0]
	weight.sort(reverse=True)
	count = 0
	while len(weight):
		for i in range(1,len(weight)):
			if weight[0]+weight[i] <=3.0:
				weight.remove(weight[i])
				weight.remove(weight[0])
				count+=1
				break
		else:
			weight.remove(weight[0])
			print(weight)
			count+=1
	return count
