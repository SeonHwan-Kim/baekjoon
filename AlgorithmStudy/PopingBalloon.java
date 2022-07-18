package AlgorithmStudy;

import java.util.Scanner;

public class PopingBalloon{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        for(int i = 0; i < N; i++){

        }

        scanner.close();
    }
}

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
            size += 1;
        }
    }

    private Node<E> get(int index){
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
    

}