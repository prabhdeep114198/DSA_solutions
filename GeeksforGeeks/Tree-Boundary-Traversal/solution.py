/* Node Structure
class Node {
    int data;
    Node left, right;

    Node(int val) {
        data = val;
        left = right = null;
    }
} */

class Solution {
    public ArrayList<Integer> boundaryTraversal(Node root) {
        // code here
        ArrayList<Integer> ans = new ArrayList<>();
        if(isLeaf(root) == false){
            ans.add(root.data);
        }
        
        addLeft(root, ans);
        addLeaf(root, ans);
        addRight(root,ans);
        
        return ans;
        
    }
    
    private void addLeft(Node root, ArrayList<Integer> ans){
        Node current = root.left;
        while(current != null){
            if(isLeaf(current) == false)  ans.add(current.data);
            if(current.left != null) current = current.left;
            else{
                current = current.right;
            }
        }
    }
    
    private void addLeaf(Node root, ArrayList<Integer> ans){
        if(isLeaf(root) == true){
            ans.add(root.data);
            return;
        }
        if(root.left != null) addLeaf(root.left, ans);
        if(root.right != null) addLeaf(root.right, ans);
    }
    
    private void addRight(Node root, ArrayList<Integer> ans){
        Stack<Integer> stk = new Stack<>();
        Node current = root.right;
        while(current != null){
            if(isLeaf(current) == false)  stk.push(current.data);
            if(current.right != null) current = current.right;
            else{
                current = current.left;
            }
        }
        
        while(!stk.isEmpty()){
            ans.add(stk.pop());
        }
    }
    
    public boolean isLeaf(Node node) {
    return node != null && node.left == null && node.right == null;
}   
    
}