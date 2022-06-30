delimitadores =()

trans_funcId = {'identifier': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('Null', 0)},
               'letras': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)},
               'digit': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)},
               'this_': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)}}
start_stateId = 'identifier'
final_statesId = set(['letras','digit', 'this_'])
delimitadoresId = ('\n', " ", "'", '+', '-', '$', '.')
automIdentifier = (trans_funcId, start_stateId, final_statesId, delimitadoresId, 0)


trans_funcF = {'Function': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)}}
start_stateF = 'Function'
final_statesF = set(['letras','digit'])
delimitadoresF = ('\n', " ", "'", '+', '-', '$', '.')
automFunction = (trans_funcF, start_stateF, final_statesF, delimitadoresF, 1)


trans_funcD = {'Decimal': {'isDigit': ('digit', 2)},
                'digit': {'isDigit': ('digit', 2)}}
start_stateD = 'Decimal'
final_statesD = set(['digit'])
delimitadoresD = ('+', '-', 'e', '.', " ", "'", '$')
automDecimal = (trans_funcD, start_stateD, final_statesD, delimitadoresD, 2)


trans_funcE = {'Exponent': {'e': ('e', 3), 'isDigit': ('Null', 3), '+':('Null', 3), '-': ('Null', 3)},
                'e': {'e': ('Null', 3), 'isDigit': ('digit', 2), '+':('is+', 3), '-': ('is-', 3)},
                'is+':{'e': ('Null', 3), 'isDigit': ('digit', 2), '+':('Null', 3), '-': ('Null', 3)},
                'is-':{'e': ('Null', 3), 'isDigit': ('digit', 2), '+':('Null', 3), '-': ('Null', 3)}}
start_stateE = 'Exponent'
final_statesE = set(['digit'])
delimitadoresE = ('\n', " ", "'", '$', '.')
automExponent = (trans_funcE, start_stateE, final_statesE, delimitadoresE, 3)


trans_funcFl = {'Float': {'isDigit': ('digit', 2), '.':('Null', 4), 'e': ('Null', 4)},
                '.': {'isDigit': ('digit', 2), '.':('Null', 4), 'e': ('Null', 4)},
                'e':{'isDigit': ('Null', 4), '.':('Null', 4), 'e': ('e', 3)}}
start_stateFl = 'Float'
final_statesFl = set(['digit'])
delimitadorFl = ('\n', " ", "'", '+', '-', '$')
automFloat = (trans_funcFl, start_stateFl, final_statesFl, delimitadorFl, 4)


trans_funcM = {'Middle': {'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'letras': {'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'isEmp': {'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'digit':{'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'is$':{'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'this_':{'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'is.':{'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)}}
start_stateM = 'Middle'
final_statesM = set(['letras','digit', 'isEmp', 'is$', 'this_', 'is.'])
delimitadoresM = ('"', "'", '+', '-', '.')
automMiddleStr = (trans_funcM, start_stateM, final_statesM, delimitadoresM, 5)


trans_funcC = {'Constant': {'is"': ('initAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('Null', 6), 'Emp': ('Null', 6), 'isDigit': ('Null', 6), '$': ('Null', 6), '_': ('Null', 6), '.': ('Null', 6)},
                'initAsp':{'is"': ('Null', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'letras': {'is"': ('finalAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'isEmp':{'is"': ('finalAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'digit':{'is"': ('finalAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'is$':{'is"': ('finalAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'this_':{'is"': ('finalAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)},
                'is.':{'is"': ('finalAsp', 6), 'initAsp':('Null', 6), 'finalAsp': ('Null', 6), 'isLetra': ('letras', 5), 'Emp': ('isEmp', 5), 'isDigit': ('digit', 5), '$': ('is$', 5), '_': ('this_', 5), '.': ('is.', 5)}}
start_stateC = 'Constant'
final_statesC = set(['finalAsp'])
delimitadoresC = ('\n', "'", '+', '-', '.')
automConstant = (trans_funcC, start_stateC, final_statesC, delimitadoresC, 6)


trans_funcCh = {'Charact': {'isAspS': ('initAspS', 7), 'initAspS':('Null', 7), 'finalAspS': ('Null', 7), 'isLetra': ('Null', 7)},
                'initAspS': {'isAspS': ('Null', 7), 'initAspS':('Null', 7), 'finalAspS': ('Null', 7), 'isLetra': ('letras', 7)},
                'letras':{'isAspS': ('finalAspS', 7), 'initAspS':('Null', 7), 'finalAspS': ('Null', 7), 'isLetra': ('Null', 7)}}
start_stateCh = 'Charact'
final_statesCh = set(['finalAspS'])
delimitadoresCh = ('\n', " ", '+', '-', '$', '.')
automChar = (trans_funcCh, start_stateCh, final_statesCh, delimitadoresCh, 7)

autmoList = (automIdentifier, automFunction, automDecimal, automExponent, automFloat, automConstant, automChar)