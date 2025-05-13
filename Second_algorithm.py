def distinct_recursion_second(array, index=None, dicto=None):
    if index is None:
        index = len(array) - 1

    if dicto is None:
        dicto = {}

    if index < 0: #this is the base case in my code
        return len(dicto)

    if array[index] not in dicto:
        dicto[array[index]] = index

    return distinct_recursion_second(array, index - 1, dicto)

if __name__ =="__main__":
    array=['a','b','a','c','d']
    print(distinct_recursion_second(array))
