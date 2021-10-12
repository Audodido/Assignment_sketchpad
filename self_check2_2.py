# Write two Python functions to find the minimum number in a list. The first function should
# compare each number to every other number on the list. 𝑂(𝑛2). The second function should be
# linear 𝑂(𝑛).


import random

lister = [random.randint(1, 50) for i in range(10)] #makes a list of 10 random numbers

def finder(list):

    first = list[0]

    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[i] > first and list[i] > j:
                break
            else:
                first = list[i]

    return first


def finder2(list):

    least = list[0]

    for l in list:
        if l <= least:
            least = l

    return least

    # list.sort()

    # return list[0]

if __name__ == "__main__":

    print("O(N^2): ", finder(lister))
    print("O(N): ", finder2(lister))
    print("Full List: ", lister)




