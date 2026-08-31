class Solution {
    public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
        // code here
        ArrayList<Integer> ans = new ArrayList<>();
        boolean visited[] = new boolean[adj.size()];
        DFS(0,adj,visited, ans);
        
        return ans;
    }
    
    private void DFS(int node,ArrayList<ArrayList<Integer>> adj , 
    boolean[] visited, ArrayList<Integer> ans ){
        visited[node] =true;
        ans.add(node);
        for(int it : adj.get(node)){
            if(!visited[it]){
                DFS(it, adj, visited, ans);
            }
        }
    }
}