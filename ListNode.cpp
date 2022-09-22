#include "ListNode.hpp"
#include <iostream>

ListNode::~ListNode() {
    std::cout << "Destroyed" << std::endl;
}