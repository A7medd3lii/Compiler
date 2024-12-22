# Lexical Analyzer for C Programming Code

This program performs lexical analysis on C-style code. It identifies and classifies various tokens, such as:

- Keywords (e.g., `if`, `else`, `while`)
- Identifiers (e.g., variable names, function names)
- Operators (e.g., `+`, `-`, `=`)
- Constants (numeric, character, and string literals)
- Comments (single-line and multi-line)

## Features
- Recognizes keywords, identifiers, and operators.
- Distinguishes between single-line and multi-line comments.
- Parses numeric, character, and string constants.

## How to Use
- Clone the repository.
- Run the program.
- Enter C-style code for lexical analysis.
- Type each line and press Enter.
- Type scan on a new line to finish input and begin analysis, exit to end program.
- The program outputs a list of tokens with their types.

# Recursive Descent Parser
## Features

## Grammar Input:
- Accepts user-defined rules for non-terminals S and B.
- Stores rules in reversed order for parsing.

## Grammar Validation:
- Ensures the grammar is simple:
- Exactly 2 rules for each non-terminal.
- Distinct first characters for the rules.
- Rules do not begin with non-terminals (S or B).

## String Parsing:
- Accepts an input string to check against the defined grammar.
- Uses a stack-based approach to simulate the parsing process.

## User Interaction:
- Options to input a new grammar, input a new string, or exit the program.

## How It Works

1. Input Grammar
- User inputs rules for S and B.
- Rules are stored in reversed form for efficient parsing.
- First characters of each rule are tracked for validation.

2. Grammar Validation
- The grammar is considered simple if:
- There are exactly 2 rules for both S and B.
- The first characters of the rules for each non-terminal are distinct.
- No rule begins with a non-terminal (S or B).

3. String Parsing
- The stack is initialized with the start symbol S and end marker #.
- The program processes the stack and the input string step-by-step:
- If the top of the stack matches a character from the string, the stack pops.
- If the top of the stack is a non-terminal, it applies the appropriate rule.

4. Output
- If the input string can be derived from the grammar, it outputs "Accepted".
- Otherwise, it outputs "Rejected".


## Implemented By
- Ahmed Ali Hassan Ahmed
- Ramadan Osman Dawood Mohamed
- Karim Mohamed Mohamed Salama
- Abdelrahman Eid Masoud
- Fayez Abdelmaqsoud Elsayed
