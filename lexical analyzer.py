import re

# Define the regex patterns for each token type
KEYWORDS = {
    'int', 'float', 'return', 'if', 'else', 'while', 'for', 'void', 
    'char', 'long', 'double', 'short', 'continue', 'break', 'switch', 'case'
}
BUILT_IN_FUNCTIONS = {'printf', 'scanf', 'sprintf', 'fscanf'} 

# Define patterns for tokens
keyword_pattern = r'\b(?:' + '|'.join(KEYWORDS) + r')\b'
identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*' 
integer_pattern = r'\d+'
float_pattern = r'\d+\.\d+([eE][+-]?\d+)?'
operator_pattern = r'[+\-*/%=&|<>!]+'  
punctuation_pattern = r'[;{},()\[\]]'
string_literal_pattern = r'"([^"\\]*(\\.[^"\\]*)*)"'
single_line_comment_pattern = r'//.*'
multi_line_comment_pattern = r'/\*.*?\*/'
whitespace_pattern = r'\s+'

# Master regex combining all token patterns
master_regex = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in {
    'single_line_comment': single_line_comment_pattern,
    'multi_line_comment': multi_line_comment_pattern,
    'keyword': keyword_pattern,
    'identifier': identifier_pattern,
    'integer_number': integer_pattern,
    'float_number': float_pattern,
    'operator': operator_pattern,
    'punctuation': punctuation_pattern,
    'string_literal': string_literal_pattern,
    'whitespace': whitespace_pattern,
}.items())

def tokenize(code):
    tokens = []
    declared_identifiers = set()  
    position = 0
    errors = []
    expect_identifier_after_keyword = False  
    expect_semicolon_after_statement = False  
    parentheses_stack = []  
    current_function = None

    # Process the code with regex matching
    while position < len(code):
        match = re.match(master_regex, code[position:])
        if match:
            for group_name, group_value in match.groupdict().items():
                if group_value:
                    if group_name == 'whitespace':
                        continue  
                    if group_name in ['single_line_comment', 'multi_line_comment']:
                        tokens.append(('comment', group_value.strip()))  
                    elif group_name == 'string_literal':
                        tokens.append(('string', group_value))  
                    elif group_name == 'identifier':
                        # Check if identifier is a keyword or built-in function
                        if group_value in KEYWORDS:
                            errors.append(f"Syntax Error: '{group_value}' cannot be used as an identifier.")
                            tokens.append(('error', f"'{group_value}' is a keyword"))
                        elif group_value in BUILT_IN_FUNCTIONS:
                            tokens.append(('function', group_value))  
                        elif group_value not in declared_identifiers and not expect_identifier_after_keyword:
                            errors.append(f"Syntax Error: Undeclared identifier: {group_value}")
                        else:
                            tokens.append(('identifier', group_value))  
                            declared_identifiers.add(group_value)  
                        expect_identifier_after_keyword = False 
                    elif group_name == 'keyword':
                        # Handle keywords like int, float, etc., for variable declarations
                        if group_value in {'int', 'float', 'char', 'long', 'double', 'short'}:
                            # Look ahead to check if there is an identifier after the keyword
                            next_token = code[position + match.end():].strip()
                            if next_token and re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', next_token.split()[0]):
                                identifier_match = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*', next_token)
                                if identifier_match:
                                    declared_identifiers.add(identifier_match.group(0))
                                    tokens.append(('keyword', group_value))
                                    expect_identifier_after_keyword = False
                                    expect_semicolon_after_statement = True 
                            else:
                                errors.append(f"Syntax Error: Expected identifier after '{group_value}'")
                                tokens.append(('error', f"Expected identifier after '{group_value}'"))
                        else:
                            tokens.append(('keyword', group_value))
                    elif group_name == 'operator':
                        # Handle assignment operator and expect semicolon after it
                        if group_value == '=':
                            expect_semicolon_after_statement = True  
                        tokens.append(('operator', group_value))
                    elif group_name == 'punctuation':
                        if group_value == ';':
                            expect_semicolon_after_statement = False 
                        elif group_value in '([{':
                            parentheses_stack.append(group_value)  
                        elif group_value in ')]}':
                            if parentheses_stack:
                                top = parentheses_stack.pop()
                                if (group_value == ')' and top != '(') or \
                                   (group_value == ']' and top != '[') or \
                                   (group_value == '}' and top != '{'):
                                    errors.append(f"Syntax Error: Unmatched parentheses, brackets, or braces.")
                            else:
                                errors.append(f"Syntax Error: Unmatched {group_value}.")
                        tokens.append(('punctuation', group_value))  
                    else:
                        tokens.append((group_name, group_value))  
            position += match.end()
        else:
            # Handle unexpected characters
            raise ValueError(f"Unexpected character at position {position}: {code[position:]}")
    
    # Check for missing semicolons after statements that require them
    if expect_semicolon_after_statement:
        errors.append("Syntax Error: Missing semicolon at the end of the statement.")
    
    # Check for unbalanced parentheses/braces/brackets
    if parentheses_stack:
        errors.append(f"Syntax Error: Unmatched opening parentheses/braces/brackets: {parentheses_stack}")

    return tokens, errors

def main():
    print("Enter C code (type 'scan' to analyze the code, 'exit' to quit):")
    while True:
        code = ""
        while True:
            line = input()
            if line.lower() == "scan":
                break
            elif line.lower() == "exit":
                print("Exiting...")
                return
            code += line + "\n"
        
        print("\nTokens found:")
        try:
            tokens, errors = tokenize(code)
            for token in tokens:
                print(token)
            
            if errors:
                print("\nErrors detected:")
                for error in errors:
                    print(error)
            else:
                print("\nNo syntax errors detected.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()