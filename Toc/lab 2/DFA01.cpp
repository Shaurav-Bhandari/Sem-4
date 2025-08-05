#include <iostream>

typedef enum states {
    q0,
    q1,
    qf
} state;

state delta(state currentState, char character) {
    if (currentState == q0) {
        return (character == '0') ? q1 : q0;
    }
    if (currentState == q1) {
        return (character == '0') ? q1 : qf;
    }
    if (currentState == qf) {
        return (character == '0') ? q1 : q0;
    }
    return q0;
}

const char* stateName(state s) {
    switch (s) {
        case q0: return "q0";
        case q1: return "q1";
        case qf: return "qf";
        default: return "unknown";
    }
}

int main() {
    char input[20];
    std::cout << "Enter the binary string: ";
    std::cin >> input;

    int i = 0;
    char ch = input[i];
    state current_state = q0;

    while (ch != '\0') {
        state prev_state = current_state;
        current_state = delta(current_state, ch);
        std::cout << "Current state: " << stateName(prev_state)
                  << " | Input: " << ch
                  << " | Next state: " << stateName(current_state)
                  << std::endl;
        ch = input[++i];
    }

    if (current_state == qf)
        std::cout << "The string reaches the final state. Language accepted.\n";
    else
        std::cout << "REJECTED.\n";

    return 0;
}
