def js(A,B):
    int = 0
	for i in A:
		for x in B:
			if i == x :
				int += 1
				break
	union = 0 
	for i in A:
		union += 1
	
	for x in B:
		if x in A:
			union = union
		else:
			union += 1
    return(int/union)
def jd(A,B):
    return (1-(js(A,B)))
