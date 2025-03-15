# Constants

DIGITS = '0123456789'

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'


# Token class

class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    
    def __repr__(self):
        if self.value:
            return f'{self.type_}:{self.value}'
        return f'{self.type_}'
    
# Lexer class

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, '+'))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, '-'))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, '*'))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, '/'))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, '('))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, ')'))
                self.advance()
            else:
                print(f"Illegal character '{self.current_char}'")
                return []
        return tokens