class Solution: 
    result = []
    def select(self, arr,i):
        return min(arr[i:])
    def selectionSort(self, arr,n):
        for i in range(n):
            # print(self.select(arr,i))
            selected = self.select(arr,i)
             
            arr[arr.index(selected)] = arr[i]
            arr[i] = selected
        return arr
