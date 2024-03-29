
import random
from matplotlib import pyplot as plt
def bubbleSort(a,len):
    swaps = 0
    comparisons = 0
    for y in range(len-1):
        swap = False
        for x in range (len-1-y):
            comparisons = comparisons + 1 
            if a[x] > a[x+1]:
                swap = True
                swaps = swaps+1
                (a[x],a[x+1]) = (a[x+1],a[x])
        if swap == False:
            break
    return[swaps,comparisons]

choices = range(100, 1001, 100)
finalSwaps = []
finalComparisons = []
for x in choices:
    swaps = 0
    comparisons = 0
    for y in range(100):
        test = random.sample(range(0,1000),x)
        result1,result2 = bubbleSort(test,x)
        swaps = swaps + result1
        comparisons = comparisons + result2
    swaps = swaps/100
    comparisons = comparisons/100
    finalSwaps.append(swaps)
    finalComparisons.append(comparisons)
    

	#ChatGPT useed to help plot
plt.scatter(choices,finalComparisons)
plt.xlabel("Input size")
plt.ylabel("Number of Comparisons")
plt.title("Comparisons vs Input")
plt.savefig("ex3.comparisonsInputSize.png")
plt.clf()

plt.scatter(choices,finalSwaps)
plt.xlabel("Input size")
plt.ylabel("Number of Swaps")
plt.title("Swaps vs Input Size")
plt.savefig("ex3.swapsInputsize.png")
plt.clf()
        