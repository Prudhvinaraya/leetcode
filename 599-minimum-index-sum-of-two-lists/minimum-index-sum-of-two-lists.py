class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ##traverse through both the lists
        lst=[]
        min=float(inf)#->infinity
        res_index={rest:i for i,rest in enumerate(list1)}
        for j,rest in enumerate(list2):
            if rest in res_index:
                i=res_index[rest] #value of i
                curr_sum=i+j
                if curr_sum<min:
                    min=curr_sum
                    lst=[rest]
                elif curr_sum ==min:
                    lst.append(rest)
                    
        # return res_index
        
        return lst
    
                        
                    