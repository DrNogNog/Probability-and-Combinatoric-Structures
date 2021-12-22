def are_parts_nonoverlapping(p):
    for i in range(0, len(p)):
      s = p[i]
      for elem in s:
          for others in range(0,i):
              if elem in p[others] :
                  return False
          for otherss in range(i+1,len(p)):
              if elem in p[otherss] :
                  return False

    return True

def do_parts_contain_element(x, p):
    for e in p:
        if x in e:
            return True
    return False
    
def do_parts_cover_set(s, p):
    for x in s:
        found = False
        for e in p:
            if x in e:
                found = True
        if not found:
            return False
            
    return True


def do_parts_have_nothing_extra(s, p):
    for x in p:
        for b in x:
            if b not in s:
                return False
    return True

def is_partition(s, p):
    if do_parts_contain_element(s, p):
        return False
    if not do_parts_have_nothing_extra(s, p):
        return False
    if not do_parts_cover_set(s, p):
        return False
    if not are_parts_nonoverlapping(p):
        return False
    return True

"""print(do_parts_contain_element({1, 2 ,3}, [{1}, {2,3}]))"""
