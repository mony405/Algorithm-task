def distinct_third(array):

    listo = []
    for item in array:
        if item not in listo:
            listo.append(item)

    return len(listo)


if __name__ == '__main__':
    print(distinct_third([1,2,5,5,6,2]))