class Solution {
    public int removeDuplicates(int[] nums) {
        //we are given an array of numbers 
        // our task is to remove duplicates and return the elements in the same non-descending order 
        //two pointer concept 
        int i=0;
        for(int j=i+1;j<nums.length;j++)
        {
            if(nums[j]!=nums[i])
            {
                i++;
                nums[i]=nums[j];
            }
        }
        

        return i+1;
    }
}