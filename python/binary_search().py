import random

l = random.sample(range(0, 100), 10)
l.sort()
print(l)

def busca_binaria(l, x, start, fim):
    meio = (start + fim) // 2
    
    if x == l[meio]:
        return meio
    
    elif x < l[meio]:
        busca_binaria(l, x, start, meio-1)
        
    elif x > l[meio]:
        busca_binaria(l, x, meio, fim)

