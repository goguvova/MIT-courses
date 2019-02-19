
def del_ete(L):
    for i in range(len(L)): 
        i += 1
        L.remove(i)
    return L
    
print(del_ete([1,2,3,4,5,6]))
