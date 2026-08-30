class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] arr = s.toCharArray();
        boolean[] hash = new boolean[128];
        int ans =0;
        int left =0;
        for(int i=0; i<arr.length;i++){
            while(hash[arr[i]]){
                hash[arr[left]] = false;
                left++;
            }
            hash[arr[i]] = true;
            if(i - left +1 > ans){
            ans = i-left+1;
        }
        }
        
        return ans;
    }
}