# Constants

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