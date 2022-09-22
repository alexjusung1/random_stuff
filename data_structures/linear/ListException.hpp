#ifndef LISTEXCEPTION_HPP
#define LISTEXCEPTION_HPP

#include <string>
#include <exception>

struct ListException : public std::exception {
    std::string message;
    ListException(std::string message) : message(message) {}
    const char* what() const noexcept {
        return message.c_str();
    }
};

#endif