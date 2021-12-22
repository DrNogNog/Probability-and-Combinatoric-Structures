def collatz_function(a):
    a = a + 1
    if a%2==0:
        return((1/2)*a)
    else:
        return(((3 * a) + 1))
def collatz_sequence(a):
    lst = []
    while collatz_function(a) != 1:
        lst.append(collatz_function(a))
        a = a + 1
    return lst
def smallest_int_with_collatz_length(n):
    count = 0
    a = 0
    while collatz_function(a) != n:
        collatz_function(a)
        count = count + 1
        a = a + 1
    return count