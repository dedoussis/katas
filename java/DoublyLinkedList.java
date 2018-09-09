public class DoublyLinkedList {
    private class Node {
        private int value;
        private Node previous, next;

        public Node(int value, Node previous, Node next) {
            this.value = value;
            this.previous = previous;
            this.next = next;
        }

        public Node getNext(){ return this.next; }
        public Node getPrevious(){ return this.previous; }
        public void setNext(Node n){ this.next = n; }
        public void setPrevious(Node n){ this.previous = n; }
        public int getValue(){ return this.value; }
    }

    private Node head, tail;

    public DoublyLinkedList(){}

    public void addToHead(int value){
        Node tmp = new Node(value, null, this.head);
        if (this.head != null) { this.head.setPrevious(tmp); }
        this.head = tmp;
        if (this.tail == null) { this.tail = tmp; }
    }

    public void addToTail(int value){
        Node tmp = new Node(value, this.tail, null);
        if (this.tail != null) { this.tail.setNext(tmp); }
        this.tail = tmp;
        if (this.head == null) { this.head = tmp; }
    }

    public void remove(int value){
        Node tmp = this.head;
        while(true) {
            if (tmp == null) { break; }
            else if (tmp.getValue() == value){
                if (tmp.getNext() == null && tmp.getPrevious() == null) { 
                    this.head = this.tail = null;
                    break; 
                }
                if (tmp.getNext() == null) { 
                    tmp.getPrevious().setNext(null);
                    this.tail = tmp.getPrevious(); 
                }
                else { tmp.getNext().setPrevious(tmp.getPrevious()); }
                if (tmp.getPrevious() == null) { 
                    tmp.getNext().setPrevious(null);
                    this.head = tmp.getNext();
                }
                else { tmp.getPrevious().setNext(tmp.getNext());  }
                break;
            }
            else { tmp = tmp.getNext(); }
        }
    }
}