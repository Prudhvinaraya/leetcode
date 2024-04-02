class Solution {
    public int search(int[] nums, int target) {
        //writing logic for O(n)
        // for(int i=0;i<nums.length;i++)
        // {
        //     if(nums[i] ==target)
        //     {
        //         return i;
        //     }
        // }
        // return -1;

        //for O(logn) logic we do have binary search algorithm 
        //we will have left and right poinitng to ends of array
        //calculate the mid
        // Initialize left and right pointers as indices
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return mid;
            }
            
            // If the left half is sorted
            if (nums[left] <= nums[mid]) {
                // If the target is within the sorted left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // If the right half is sorted
            else {
                // If the target is within the sorted right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}