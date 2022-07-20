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
            firstNode.prev = tailNode;
            size++;
        }
    }

    boolean remove(Object o){
        Node<E> findNode = firstNode;
        for(int i = 0;i < size; findNode = findNode.next){
            if(o.equals(findNode.data)){
                break;
            }
        }

        if(findNode == null){
            return false;
        }
        else{
            findNode.prev.next = findNode.next;
            findNode.next.prev = findNode.prev;
            findNode.data = null;
            findNode.next = null;
            findNode.prev = null;
        }
        size--;
        return true;

    }
    
    // boolean contains(Object value){
    //     return indexOf(value) >= 0;
    // }

    // int size(){

    // }

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
    }
    
//     E set(int index, E elements){

//     }
    
//     boolean isEmpty(){

//     }

//     boolean equals(Object o){

//     }

//     int indexOf(Object o){

//     }

//     void clear(){

//     }
    void show() {
        Node<E> temp = firstNode;
        do {
            System.out.println(temp.data);
            temp = temp.next;
        } while (temp != firstNode);
    }
}


public class DoublyLinkedListMain{
    public static void main(String[] args) {
        DoublyLinkedList<Integer> v = new DoublyLinkedList<>();
        v.add(4);
        v.add(3);
        v.remove(4);
        v.show();
    }
}