class Solution {
    public ArrayList<Integer> bfs(ArrayList<ArrayList<Integer>> adj) {
        // code here
        ArrayList<Integer> ans = new ArrayList<>();
        int V = adj.size();
        boolean visited[] = new boolean[V];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        visited[0] = true;
        
        while(!q.isEmpty()){
            Integer node = q.poll();
            ans.add(node);
            
            for(Integer it : adj.get(node)){
                if(visited[it] == false){
                    visited[it] = true;
                    q.add(it);
                }
            }
        }
        return ans;
    }
}