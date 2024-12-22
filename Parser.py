def input_grammar():
    """
    Prompts the user to input grammar rules for non-terminals 'S' and 'B'.
    Stores the reversed rules and their first characters for further processing.
    """
    global s_rules, b_rules, s_first_chars, b_first_chars

    # Initialize grammar rule lists and selection sets
    s_rules, b_rules = [], []
    s_first_chars, b_first_chars = [], []

    print("\nEnter grammar rules:")

    # Input rules for 'S'
    for i in range(2):
        rule = input(f"Enter rule {i + 1} for non-terminal 'S': ").strip()
        if rule:
            s_rules.append(rule[::-1])  # Store reversed rule
            s_first_chars.append(rule[0])  # Store first character of rule

    # Input rules for 'B'
    for i in range(2):
        rule = input(f"Enter rule {i + 1} for non-terminal 'B': ").strip()
        if rule:
            b_rules.append(rule[::-1])  # Store reversed rule
            b_first_chars.append(rule[0])  # Store first character of rule

    print("\nGrammar rules:")
    print("S rules:", s_rules)
    print("B rules:", b_rules)
    print("First characters of S rules:", s_first_chars)
    print("First characters of B rules:", b_first_chars)

def input_string():
    """
    Prompts the user to input the string to be checked.
    """
    global input_str
    input_str = list(input("\nEnter the string to be checked: ").strip())
    print("The input string:", input_str)

def is_simple_grammar():
    """
    Checks if the grammar rules are simple.

    A simple grammar satisfies:
    - Exactly 2 rules for each non-terminal.
    - The first characters of the rules for a non-terminal are distinct.
    - No rules start with non-terminals ('S' or 'B').
    """
    if len(s_rules) == 2 and len(b_rules) == 2:
        if s_first_chars[0] != s_first_chars[1] and b_first_chars[0] != b_first_chars[1]:
            if 'S' not in s_first_chars and 'B' not in b_first_chars:
                return True
    return False

def initialize_stack():
    """
    Initializes the parsing stack with the start symbol 'S'.
    """
    global stack
    stack = ['#', 'S']
    print("\nInitial parsing stack:", stack)

def parse_string():
    """
    Parses the input string using the grammar rules.
    Accepts or rejects the string based on the rules.
    """
    global stack, input_str

    while stack:
        top = stack.pop()
        print(f"\nCurrent stack: {stack}")
        if top == '#':
            print("\nParsing complete.")
            if not input_str:
                print("Result: ACCEPTED")
            else:
                print("Result: REJECTED")
            return

        if not input_str:
            print("Result: REJECTED (Input string exhausted before parsing complete)")
            return

        current_char = input_str.pop(0)

        if top in ['a', 'b']:  # Terminal symbols
            if top == current_char:
                print(f"Matched terminal: {current_char}")
            else:
                print(f"Error: Expected {top}, found {current_char}")
                print("Result: REJECTED")
                return
        elif top == 'S':  # Non-terminal S
            rule_applied = False
            for rule in s_rules:
                if rule[-1] == current_char:
                    stack.extend(rule[:-1][::-1])  # Push rule to stack (except last char)
                    rule_applied = True
                    print(f"Applied rule for S: {rule[::-1]}")
                    break
            if not rule_applied:
                print(f"Error: No matching rule for S with {current_char}")
                print("Result: REJECTED")
                return
        elif top == 'B':  # Non-terminal B
            rule_applied = False
            for rule in b_rules:
                if rule[-1] == current_char:
                    stack.extend(rule[:-1][::-1])  # Push rule to stack (except last char)
                    rule_applied = True
                    print(f"Applied rule for B: {rule[::-1]}")
                    break
            if not rule_applied:
                print(f"Error: No matching rule for B with {current_char}")
                print("Result: REJECTED")
                return

def start_parsing():
    """
    Main function to manage the parsing process.
    """
    print("\nStarting Recursive Descent Parsing")

    input_grammar()

    if is_simple_grammar():
        print("\nThe grammar is simple.")
        input_string()
        initialize_stack()
        parse_string()
    else:
        print("\nThe grammar is not simple. Please try again.")
        start_parsing()

# Main script
if __name__ == "__main__":
    print("Recursive Descent Parsing for the Given Grammar")

    # Initialize global variables
    s_rules, b_rules = [], []
    s_first_chars, b_first_chars = [], []
    input_str, stack = '', []

    # Start the parsing process
    start_parsing()

    while True:
        print("\n============================================")
        choice = input("1 - Input Another Grammar\n2 - Input Another String\n3 - Exit\nEnter your choice: ").strip()

        if choice == '1':
            start_parsing()
        elif choice == '2':
            input_string()
            initialize_stack()
            parse_string()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")