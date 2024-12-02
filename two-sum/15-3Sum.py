# Three sum 
# Time: O(n^2) Space O(n)
# Runtime 742ms, Beats 29.31%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numdic={}
        res=[]
        for n in nums:
            if n in numdic:
                numdic[n]+=1
            else:
                numdic[n]=1
        # for i in numdic:
        #     print(f"{i}:{numdic[i]}")
        if 0 in numdic:
            if len(nums) == numdic[0]:
                return [[0,0,0]]
            if numdic[0] >=3:
                res.append([0,0,0])
            for i in numdic:
                if -i in numdic and i!=0:
                    temp=[i,0,-i]
                    temp.sort()
                    res.append(temp)
        for i in numdic:
            if numdic[i]>=2 and i!=0:
                if -(2*i) in numdic:
                    temp=[i,i,-(2*i)]
                    temp.sort()
                    res.append(temp)
        for i in numdic:
            if i>0:
                for j in numdic:
                    if j>0 and i!=j:
                        if -(i+j) in numdic:
                            temp=[i,j,-(i+j)]
                            temp.sort()
                            res.append(temp)
            if i<0:
                for j in numdic:
                    if j<0 and i!=j:
                        if -(i+j) in numdic:
                            temp=[i,j,-(i+j)]
                            temp.sort()
                            res.append(temp)
        res_dic={}
        for i in res:
            if tuple(i) not in res_dic:
                res_dic[tuple(i)]=i

        return list(res_dic.values())
