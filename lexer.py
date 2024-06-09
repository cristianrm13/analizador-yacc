import ply.lex as lex

tokens = (
    'VOID', 'SETUP', 'LOOP', 'SERIAL', 'BEGIN', 'PRINT',
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMICOLON',
    'NUMBER', 'STRING', 'DOT'
)

t_VOID = r'Void'
t_SETUP = r'setup'
t_LOOP = r'loop'
t_SERIAL = r'Serial'
t_BEGIN = r'begin'
t_PRINT = r'print'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_NUMBER = r'\d+'
t_STRING = r'\".*?\"'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
