from flask import Flask, render_template, request
from lexer import lexer
from myparser import parser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        try:
            lexical_analysis = parse_lexical_analysis(code)
            syntactic_analysis = parse_syntactic_analysis(code)
            
            token_data, classified_tokens = classify_tokens(lexical_analysis)
            
            lexical_present = lexical_analysis is not None
            syntactic_present = syntactic_analysis is not None
            
            return render_template('index.html', 
                                   code=code, 
                                   lexical_analysis=lexical_analysis, 
                                   syntactic_analysis=syntactic_analysis, 
                                   lexical_present=lexical_present, 
                                   syntactic_present=syntactic_present, 
                                   error_message=None,
                                   token_data=token_data,
                                   classified_tokens=classified_tokens)
        except SyntaxError as e:
            error_message = "Error sintáctico: " + str(e)
            return render_template('index.html', 
                                   code=code, 
                                   lexical_analysis=None, 
                                   syntactic_analysis=None, 
                                   lexical_present=False, 
                                   syntactic_present=False, 
                                   error_message=error_message,
                                   token_data=None,
                                   classified_tokens=None)
    else:
        return render_template('index.html', 
                               code=None, 
                               lexical_analysis=None, 
                               syntactic_analysis=None, 
                               lexical_present=False, 
                               syntactic_present=False, 
                               error_message=None,
                               token_data=None,
                               classified_tokens=None)

def parse_lexical_analysis(code):
    lexer.input(code)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append({'line': tok.lineno, 'token': tok.value, 'type': tok.type})
    return tokens

def parse_syntactic_analysis(code):
    result = parser.parse(code)
    return result

def classify_tokens(lexical_analysis):
    token_classes = {
        'Reservada': ['VOID', 'SETUP', 'LOOP', 'SERIAL', 'BEGIN', 'PRINT'],
        'Identificador': ['STRING'],
        'Numero': ['NUMBER'],
        'Simbolo': ['DOT'],
        'Parentesis_Izquierdo': ['LPAREN'],
        'Parentesis_Derecho': ['RPAREN'],
        'Llave_Izquierda': ['LBRACE'],
        'Llave_Derecha': ['RBRACE'],
      # 'Cadena': ['STRING']
    }
    
    classified_tokens = {
        'Reservada': 0,
        'Identificador': 0,
        'Numero': 0,
        'Simbolo': 0,
        'Parentesis_Izquierdo': 0,
        'Parentesis_Derecho': 0,
        'Llave_Izquierda': 0,
        'Llave_Derecha': 0,
      # 'Cadena': 0
    }
    
    token_data = []
    
    for token in lexical_analysis:
        token_class = None
        for key, values in token_classes.items():
            if token['type'] in values:
                token_class = key
                classified_tokens[key] += 1
                break
        token_data.append({
            'token': token['token'],
            'class': token_class
        })
    
    return token_data, classified_tokens

if __name__ == '__main__':
    app.run(debug=True)
