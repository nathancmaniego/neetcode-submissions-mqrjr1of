class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int check = target - nums[i];
            if (prevMap.containsKey(check)) {
                int[] indexes = {prevMap.get(check), i};
                return indexes;
            }
            prevMap.put(nums[i], i);
        }
        return new int[]{};
    }
}
