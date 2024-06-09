import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : void_setup void_loop'''
    p[0] = "La estructura del código es válida."

def p_void_setup(p):
    '''void_setup : VOID SETUP LPAREN RPAREN LBRACE serial_begin serial_print RBRACE'''
    pass

def p_serial_begin(p):
    '''serial_begin : SERIAL DOT BEGIN LPAREN NUMBER RPAREN SEMICOLON'''
    pass

def p_serial_print(p):
    '''serial_print : SERIAL DOT PRINT LPAREN STRING RPAREN SEMICOLON'''
    pass

def p_void_loop(p):
    '''void_loop : VOID LOOP LPAREN RPAREN LBRACE RBRACE'''
    pass

def p_error(p):
    raise SyntaxError(f"Syntax error at '{p.value}'")

parser = yacc.yacc()
