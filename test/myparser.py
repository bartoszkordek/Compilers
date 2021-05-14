import ply.yacc as yacc

# Get the token map from the lexer.
from mylexer import tokens

# grammar rules


def p_statement_preamble(p):
    'statement : DOCUMENTCLASS header body'
    p[0] = '<!DOCTYPE html>'+'\n<html lang="en">' + p[2]+ p[3]+'\n</html>'


def p_header(p):
    '''header : USE_PACKAGE USE_PACKAGE 
              | USE_PACKAGE'''
    p[0] = '\n<header>' + '\n</header>'


def p_body(p):
    'body : BEGIN_DOCUMENT expression END_DOCUMENT'
    p[0] = '\n<body>' + p[2] + '\n</body>'


def p_expression_text(p):
    'expression : TEXT'
    p[0] = p[1]


def p_expression_bold(p):
    '''expression : BOLD LBRACE expression RBRACE expression
                  | BOLD LBRACE expression RBRACE'''
    if len(p) == 6:
         p[0] = '<b>' + p[3] + '</b>'+ p[5]
    else:
        p[0] = '<b>' + p[3] + '</b>'
   

def p_expression_italic(p):
    '''expression : ITALIC LBRACE expression RBRACE expression
                  | ITALIC LBRACE expression RBRACE'''
    if len(p) == 6:
        p[0] = '<i>' + p[3] + '</i>' + p[5]
    else:
        p[0] = '<i>' + p[3] + '</i>'


def p_title(p):
    'expression : TITLE LBRACE TEXT RBRACE'
    p[0] = '<i>' + p[3] + '</i>'

def p_expression_unordered_list(p):
    'expression : BEGIN_ULIST expression END_ULIST'
    p[0] = '\n<ul>' + p[2] + '\n</ul>'


def p_expression_ordered_list(p):
    'expression : BEGIN_OLIST expression END_OLIST'
    p[0] = '\n<ol>' + p[2] + '\n</ol>'


def p_expression_listitem(p):
    '''expression : ITEM expression expression 
                  | ITEM expression '''
    if len(p) == 4:
        p[0] = '\n<li>' + p[2] + '</li>' + p[3]
    else:
        p[0] = '\n<li>' + p[2] + '</li>'


# Error rule for syntax errors

def p_error(p):
    print(p)
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
