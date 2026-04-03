class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> lst = new HashSet();
        for (int i=0;i < nums.length;i++){
            if (lst.contains(nums[i])){
                return true;
            }
            lst.add(nums[i]);
        }
        return false;
    }
}
