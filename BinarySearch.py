def BinarySearch(data,value):
    low = 0
    high = len(data) 
    print(high)
    temp = True
    while low <= high and temp:
        mid = low + high
        mid = mid // 2
        print(mid)
        if value == data[mid]:
            print(f"Nilai {value} Berada Pada Index {mid}")
            temp = False
        else:
            if value < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        

lst = [20,23,10,31,46,38,93,30,34,90]
lst.sort()
print(lst)
BinarySearch(lst,30)
