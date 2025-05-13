def distinct_first(array) :
    if not array :
        return 0
    # first we sort the array with pubble sort
    length=len(array)
    for i in range(length):
        swap=False
        for j in range(0,length-i-1): #-1 to avoid index out of range
            if array[j] > array[j+1]:
                array[j] , array[j + 1] = array[j+1] , array[j]
                swap=True
        if not swap :
            break
    # loop to count the distinct elements
    print(array)
    count = 1
    for i in range(length-1):
        if array[i] != array[i+1]:
            count+=1
    return count


if __name__ =="__main__":
    array=['d','c','b','a']
    print(distinct_first(array))
