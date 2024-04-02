class Solution {
    public int search(int[] nums, int target) {
        //writing logic for O(n)
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] ==target)
            {
                return i;
            }
        }
        return -1;
    }
}