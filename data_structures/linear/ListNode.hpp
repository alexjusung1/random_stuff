#ifndef LISTNODE_HPP
#define LISTNODE_HPP

template <typename T>
struct ListNode {
    T val;
    ListNode<T> *next;
    ListNode(T val, ListNode *next) : val(val), next(next) {}
    ListNode(T val) : ListNode(val, nullptr) {}
};

#endif