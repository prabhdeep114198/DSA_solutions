import java.util.Arrays;

class Solution {
    public int[] singleNum(int[] arr) {
        Arrays.sort(arr);

        int[] ans = new int[2];
        int a = 0;

        for (int i = 0; i < arr.length; i++) {
            if ((i == 0 || arr[i] != arr[i - 1]) && (i == arr.length - 1 || arr[i] != arr[i + 1])) {

                ans[a++] = arr[i];
            }
        }

        return ans;
    }
}