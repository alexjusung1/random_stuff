#ifndef LINKEDLIST_HPP
#define LINKEDLIST_HPP

#include <iostream>
#include "ListNode.hpp"
#include "ListException.hpp"

template <typename T>
class LinkedList {
    public:
    LinkedList() : head(nullptr), len(0) {}
    int getLength() const { return len; }
    void add(T data);
    void insert(int index, T data);
    T getData(int index);
    
    private:
    int len;
    ListNode<T> *head;
    ListNode<T> *getNode(int index);
};


// Public

template <typename T>
void LinkedList<T>::add(T data) {
    insert(len, data)
}

template <typename T>
void LinkedList<T>::insert(int index, T data) {
    if (index > len) {
        throw ListException("List index out of bounds...")
    }
    if (index == 0) {
        ListNode<T> *newHead = new ListNode<T>(data, head);
        head = newHead;
    } else {
        ListNode<T> *prevNode = getNode(index - 1);
        ListNode<T> *newNode = ListNode(data, prevNode->next);
        prevNode->next = newNode;
    }
    ++len;
}

template <typename T>
T LinkedList<T>::getData(int index) {
    return getNode(index).val;
}

// Private

template <typename T>
ListNode<T> *LinkedList<T>::getNode(int index) {
    if (index >= len) {
        throw 
    }
}

#endif