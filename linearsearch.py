def LinearSearch(data,value):
    start = 0
    temp = True
    while start <= len(data) and temp:
        if data[start] == value:
            print(f'{value} Berada di index {start}')
            temp = False
        elif start == len(data) -1:
            print("data tidak di temukan")
            temp = False
        else:
            start += 1

database = [23,21,2,1,5,9,34,56]
print(f'Jumlah index12 data= {len(database) -1 }')
LinearSearch(database,56)
