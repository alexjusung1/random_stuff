#include <iostream>
#include "ListNode.hpp"

int main(int argc, char **argv) {
    ListNode *t = new ListNode();
    std::cout << t->val << std::endl;
    delete t;
    return 0;
}