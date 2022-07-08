database = [31,2,5,22,9,12,6,7,1,25,21]

def bublesort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
        print(database)

bublesort(database)