/* Structure of a Linked List Node
class Node {
	int data;
	Node next;
	
	Node(int x) {
		data = x;
		next = null;
	}
} */

class Solution {
	Node divide(Node head) {
		// code here
		Node resHead = null;
		Node resTail = null;
		
		Node curr = head;
		Node prev = null;
		
		while (curr != null) {
			if (curr.data%2 == 0) {
				if (prev != null) {
					prev.next = curr.next;
				}
				else {
					head = curr.next;
				}
				if (resHead == null) {
					resHead = curr;
					resTail = resHead;
				}
				else {
					resTail.next = curr;
					resTail = resTail.next;
				}
				curr = curr.next;
			}
			else {
				prev = curr;
				curr = curr.next;
			}
		}
		if(resHead == null){
		    return head;
		}
		resTail.next = head;
		return resHead;
	}
}
