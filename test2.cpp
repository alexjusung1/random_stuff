#include <iostream>
#include <stdexcept>

struct Node;

Node* Xor(Node* prev, Node* next) {
    return reinterpret_cast<Node*>(reinterpret_cast<uintptr_t>(prev) ^ reinterpret_cast<uintptr_t>(next));
}

struct Node {
    int val;
    Node* diff;
    Node(int val, Node* prev, Node* next) : val(val), diff(Xor(prev, next)) {}

    Node* GetNext(Node* prev) {
        return Xor(diff, prev);
    }
    Node* GetPrev(Node* next) {
        return Xor(diff, next);
    }

    ~Node() {
        std::cout << "Deleting Node with value " << val << std::endl; // Testing for memory leaks
    }
};

void Add(Node* &head, int val) {
    if (nullptr == head) {
        head = new Node(val, nullptr, nullptr);
        return;
    }
    Node* prev = nullptr;
    Node* cur = head;
    Node* next = cur->GetNext(prev);
    while (next != nullptr) {
        prev = cur;
        cur = next;
        next = cur->GetNext(prev);
    }
    cur->diff = Xor(prev, new Node(val, cur, nullptr));
}

int Get(Node* cur, int index) {
    Node* prev = nullptr;
    while (index && cur != nullptr) {
        Node* next = cur->GetNext(prev);
        prev = cur;
        cur = next;
        --index;
    }
    if (index != 0) {
        throw std::out_of_range("index out of range");
    }
    return cur->val;
}

void Delete(Node* cur) {
    Node* prev = nullptr;
    while (cur != nullptr) {
        Node* next = cur->GetNext(prev);
        delete prev;
        prev = cur;
        cur = next;
    }
    delete prev;
}

std::ostream &operator<<(std::ostream &os, Node* cur) {
    os << '[';
    Node* prev = nullptr;
    while (cur != nullptr) {
        os << cur->val << ", ";
        Node* next = cur->GetNext(prev);
        prev = cur;
        cur = next;
    }
    os << ']';
    return os;
}

int main() {
    Node* head = nullptr;
    Add(head, 1000);
    Add(head, 100);
    Add(head, 10);
    Add(head, 1);
    std::cout << head << std::endl;
    std::cout << Get(head, 2) << std::endl;

    using somefunc = void(*)(int, int); // function pointer syntax
    somefunc f = [] (int a, int b) { std::cout << a << ", " << b << std::endl; }; // lambda
    f(1, 2);

    auto k = [&] (int i) -> int { return Get(head, i); }; // Type is int(*)(int)
    std::cout << k(1) << std::endl;

    int i = 0, j = 0;
    // auto l = [&, i] () { std::cout << ++i << ", " << ++j << std::endl; }; l();   // Error; cannot modify i
    // auto m = [=, &i] () { std::cout << ++i << ", " << ++j << std::endl; }; m();  // Error; cannot modify j
    std::cout << ++i << ", " << ++j << std::endl;

    Delete(head);
    return 0;
}