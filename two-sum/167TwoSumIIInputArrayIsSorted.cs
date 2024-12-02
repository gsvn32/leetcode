//Two pointer pattern
// pass through array, based on sum do operation
//Time: O(n) space: O(1)
// Runtime: 0ms, Beats 100%
public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        //Initial conditions
        int[] result = [0,0];
        int left=0;
        int right=numbers.Length-1;

        while(left<right){
            if(numbers[left]+numbers[right]==target){
                result[0]=left+1;
                result[1]=right+1;
                return result;
            }
            else if(numbers[left]+numbers[right]>target){
                right--;
            }
            else{
                left++;
            }
        }
        return result;

    }
}
