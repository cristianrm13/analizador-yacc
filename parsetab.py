
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN DOT LBRACE LOOP LPAREN NUMBER PRINT RBRACE RPAREN SEMICOLON SERIAL SETUP STRING VOIDprogram : void_setup void_loopvoid_setup : VOID SETUP LPAREN RPAREN LBRACE serial_begin serial_print RBRACEserial_begin : SERIAL DOT BEGIN LPAREN NUMBER RPAREN SEMICOLONserial_print : SERIAL DOT PRINT LPAREN STRING RPAREN SEMICOLONvoid_loop : VOID LOOP LPAREN RPAREN LBRACE RBRACE'
    
_lr_action_items = {'VOID':([0,2,20,],[3,5,-2,]),'$end':([1,4,16,],[0,-1,-5,]),'SETUP':([3,],[6,]),'LOOP':([5,],[7,]),'LPAREN':([6,7,22,23,],[8,9,24,25,]),'RPAREN':([8,9,26,27,],[10,11,28,29,]),'LBRACE':([10,11,],[12,13,]),'SERIAL':([12,14,30,],[15,18,-3,]),'RBRACE':([13,17,31,],[16,20,-4,]),'DOT':([15,18,],[19,21,]),'BEGIN':([19,],[22,]),'PRINT':([21,],[23,]),'NUMBER':([24,],[26,]),'STRING':([25,],[27,]),'SEMICOLON':([28,29,],[30,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'void_setup':([0,],[2,]),'void_loop':([2,],[4,]),'serial_begin':([12,],[14,]),'serial_print':([14,],[17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> void_setup void_loop','program',2,'p_program','myparser.py',5),
  ('void_setup -> VOID SETUP LPAREN RPAREN LBRACE serial_begin serial_print RBRACE','void_setup',8,'p_void_setup','myparser.py',9),
  ('serial_begin -> SERIAL DOT BEGIN LPAREN NUMBER RPAREN SEMICOLON','serial_begin',7,'p_serial_begin','myparser.py',13),
  ('serial_print -> SERIAL DOT PRINT LPAREN STRING RPAREN SEMICOLON','serial_print',7,'p_serial_print','myparser.py',17),
  ('void_loop -> VOID LOOP LPAREN RPAREN LBRACE RBRACE','void_loop',6,'p_void_loop','myparser.py',21),
]
