class Solution(object):
    
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        ans = []
        for i in queries:
            if intLength==1:
                if i >=1 and i<10:
                    ans.append(i)
                else:
                    ans.append(-1)
            else:
                if intLength%2==0:
                    plain_number = intLength//2
                    firsthalf = str(10**(plain_number-1)+i-1)
                    lasthalf = firsthalf[::-1]
                else:
                    plain_number = intLength//2+1
                    firsthalf = str(10**(plain_number-1)+i-1)
                    lasthalf = firsthalf[len(firsthalf)-2::-1]
                    #print(lasthalf)
                if len(firsthalf) ==   plain_number:  
                    ans.append(int(firsthalf + lasthalf))
                else:
                    ans.append(-1)

        return ans
