s = {1,2,3}
def is_reflexive(A, R):
    for x in A:
        if not R(x,x):
            return False
    return True


def is_injective(domain, f):
    list1 = []
    for x in domain:
       i = f(x)
       if i in list1:
           return False
       else:
           list1+=[i]
           
    return True

def is_transitive(A,R):
    for x in A:
        for y in A:
            for z in A:
                if (R(x,y) == True) and (R(y,z) == True):
                    if (R(x,z) == False):
                        return False
    else:
        return True