import random

lst = random.sample(range(0, 100),15)
print(lst)

def quick_sort(vetor, start, fim):
    mid = (start + fim) // 2
    pivo = vetor[mid]
    i = start
    j = fim


    while i < j:
        while vetor[i] < pivo:
            i += 1
        while vetor[j] > pivo:
            j -= 1

        if i <= j:
            vetor[i], vetor[j] = vetor[j], vetor[i]
        i += 1
        j -= 1

        if j > start:
            quick_sort(vetor, start, j)
        if i < fim:
            quick_sort(vetor, i, fim)

        print(lst)
