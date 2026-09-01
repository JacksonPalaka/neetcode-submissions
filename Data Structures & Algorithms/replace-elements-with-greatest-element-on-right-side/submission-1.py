class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length,new_list = len(arr),[]
        for i in range(1,length):
            new_list.append(max(arr[i:length]))
        new_list.append(-1)
        return new_list