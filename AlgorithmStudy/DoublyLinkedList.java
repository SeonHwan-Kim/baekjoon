package AlgorithmStudy;

class Node<E>{
    Node(){
    }
    Node(E data){
        this.data = data;
    }
    E data;
    Node<E> next = null;
    Node<E> prev = null;
}

class DoublyLinkedList<E>{
    private Node<E> firstNode;
    private Node<E> tailNode;
    private int size;

    DoublyLinkedList(){
        this.firstNode = null;
        this.tailNode = null;
        this.size = 0;
    }

    void add(E data){
        if(firstNode == null){
            firstNode = tailNode = new Node<E>(data);
            size += 1;
        }
        else{
            tailNode.next = new Node<E>(data);
            tailNode.next.prev = tailNode;
            tailNode = tailNode.next;
            tailNode.next = firstNode;
            size++;
        }
    }

    void remove(Object o){
        
    }
    
    boolean contains(Object value){
        return indexOf(value) >= 0;
    }

    int size(){

    }

    Node<E> search(int index){
        if(index > size / 2){
            Node<E> x = tailNode;
            for(int i = size - 1; i > index; i--){
                x = x.prev;
            }
            return x;
        }
        else{
            Node<E> x = firstNode;
            for(int i = 0; i < index; i++){
                x = x.next;
            }
            return x;
        }
    }2
    
    E set(int index, E elements){

    }
    
    boolean isEmpty(){

    }

    boolean equals(Object o){

    }

    int indexOf(Object o){

    }

    void clear(){

    }
}