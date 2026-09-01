class Solution {
    public ArrayList<ArrayList<String>> anagrams(String[] arr) {
        // code here
        Map<String, ArrayList<String>> map = new HashMap<>();
        for(String s : arr){
            int[] count = new int[26];
            for(char c : s.toCharArray()){
                count[c - 'a']++;
            }
            StringBuilder sb = new StringBuilder();
            for(int i : count){
                sb.append("#");
                sb.append(i);
            }
            String key = sb.toString();
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(s);
        }
        return new ArrayList(map.values());
    }
}