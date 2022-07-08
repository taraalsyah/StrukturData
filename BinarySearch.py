# melakukan pencarian dengan tekhnik Binary Search. 
def BinarySearch(data,value):
    low = 0  # low selalu berada di index 0 atau inisialisasi pointer start
    high = len(data)  # Menghitung panjang data atau inisialisai pointer end 
    temp = True
    while low <= high and temp:  # Pengulangan jika kondisi low kurang sama dengan high dan temp sama dengan True
        mid = low + high  # Inisialisasi panjang data 
        mid = mid // 2  # Setengah dari total panjang data antara low dan high atau inisialisasi pointer midle
        if value == data[mid]: 
            # JIka value yg di cari berada di pointer midle, maka print.
            print(f"Nilai {value} Berada Pada Index {mid}")
            temp = False
        else: 
            # Jika value yg di cari kurang dari pointer midle .maka nilai high atau pointer end di ubah menjadi berada di index mid - 1
            if value < data[mid]: 
                high = mid - 1
            # Jika value yg di cari lebih dari pointer midle .maka nilai low atau pointer start di ubah menjadi berada di index mid + 1
            else:
                low = mid + 1
        

lst = [20,23,10,31,46,38,93,30,34,90]  # Sebelum melakukan pencarian dengan tekhink Binary Search, harus melakukan sorting data.
lst.sort()
print(lst)
BinarySearch(lst,30)
