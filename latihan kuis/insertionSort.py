def insertionSort(data):
    for index in range(1,len(data)):
        currentvalue = data[index]
        position = index
        while position>0 and data[position-1]>currentvalue:
            data[position]=data[position-1]
            position = position-1
        data[position]=currentvalue
        
data = [54,26,93,17]
print(sorted(data))
print(data)

data.sort()
print(data)
print(data)
print(data)
print(data)

# insertionSort(data)
# print(data)
