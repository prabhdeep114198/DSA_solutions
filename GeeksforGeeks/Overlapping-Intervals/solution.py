class Solution {
    public ArrayList<ArrayList<Integer>> mergeOverlap(int[][] arr) {
        // Code here
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
        
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        int start = arr[0][0];
        int end = arr[0][1];
        for(int i=0;i<arr.length;i++){
            if(arr[i][0] <= end){
                end = Math.max(arr[i][1] , end);
            }
            else{
                ArrayList<Integer> temp = new ArrayList<>();
                temp.add(start);
                temp.add(end);
                result.add(temp);
                
                start = arr[i][0];
                end = arr[i][1];
            }
            
        }
        ArrayList<Integer> temp = new ArrayList<>(); 
        temp.add(start); 
        temp.add(end); 
        result.add(temp); 
        return result;
    }
}