# def bubbleSort(arr):
#     n = len(arr)

#     # Traverse through all array elements
#     for i in range(n):

#         # Last i elements are already in place
#         for j in range(0, n-i-1):

#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j+1] :
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)