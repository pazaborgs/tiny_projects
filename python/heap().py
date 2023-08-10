import random
vetor = random.sample(range(0,50),10)
print(vetor)
mid = (len(vetor) - 1) //2
while mid >= 0:
    if vetor[mid] < vetor[2*mid + 1]:
        temp = vetor[mid]
        vetor[mid], vetor[2*mid + 1] = vetor[2*mid + 1], temp
        mid -= 1
    elif vetor[2*mid + 2] == None:
        mid -= 1
    elif vetor[mid] < vetor[2*mid + 2]:
        temp = vetor[mid]
        vetor[mid], vetor[2*mid + 2] = vetor[2*mid + 2], temp
        mid -= 1
    else:
        mid -= 1

print(vetor)
        
