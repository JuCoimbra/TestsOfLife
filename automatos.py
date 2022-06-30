delimitadores =()

trans_funcId = {'identifier': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('Null', 0)},
               'letras': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)},
               'digit': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)},
               'this_': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)}}
start_stateId = 'identifier'
final_statesId = set(['letras','digit', 'this_'])
delimitadoresId = set(['\n', " ", "'", '+', '-', '$', '.'])
automIdentifier = (trans_funcId, start_stateId, final_statesId, delimitadoresId, 0)


trans_funcF = {'Function': {'isLetra': ('letras', 0), '_': ('this_', 0), 'isDigit': ('digit', 0)}}
start_stateF = 'Function'
final_statesF = set(['letras','digit'])
delimitadoresF = set(['\n', " ", "'", '+', '-', '$', '.'])
automFunction = (trans_funcF, start_stateF, final_statesF, delimitadoresF, 1)


trans_funcD = {'Decimal': {'isDigit': ('digit', 2)},
                'digit': {'isDigit': ('digit', 2)}}
start_stateD = 'Decimal'
final_statesD = set(['digit'])
delimitadoresD = set(['+', '-', 'e', '.', " ", "'", '$'])
automDecimal = (trans_funcD, start_stateD, final_statesD, delimitadoresD, 2)


trans_funcE = {'Exponent': {'e': ('e', 3), 'isDigit': ('Null', 3), '+':('Null', 3), '-': ('Null', 3)},
                'e': {'e': ('Null', 3), 'isDigit': ('digit', 2), '+':('is+', 3), '-': ('is-', 3)},
                'is+':{'e': ('Null', 3), 'isDigit': ('digit', 2), '+':('Null', 3), '-': ('Null', 3)},
                'is-':{'e': ('Null', 3), 'isDigit': ('digit', 2), '+':('Null', 3), '-': ('Null', 3)}}
start_stateE = 'Exponent'
final_statesE = set(['digit'])
delimitadoresE = set(['\n', " ", "'", '$', '.'])
automExponent = (trans_funcE, start_stateE, final_statesE, delimitadoresE, 3)


trans_funcFl = {'Float': {'isDigit': ('digit', 2), '.':('Null', 4), 'e': ('Null', 4)},
                '.': {'isDigit': ('digit', 2), '.':('Null', 4), 'e': ('Null', 4)},
                'e':{'isDigit': ('Null', 4), '.':('Null', 4), 'e': ('e', 3)}}
start_stateFl = 'Float'
final_statesFl = set(['digit'])
delimitadorFl = set(['\n', " ", "'", '+', '-', '$'])
automFloat = (trans_funcFl, start_stateFl, final_statesFl, delimitadorFl, 4)


trans_funcC = {'Constant': {'is"': ('initAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('Null', 5), 'Emp': ('Null', 5), 'isDigit': ('Null', 5), '$': ('Null', 5), '_': ('Null', 5), '.': ('Null', 5)},
                'initAsp':{'is"': ('Null', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'letras': {'is"': ('finalAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'isEmp':{'is"': ('finalAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'digit':{'is"': ('finalAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'is$':{'is"': ('finalAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'this_':{'is"': ('finalAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'is.':{'is"': ('finalAsp', 5), 'initAsp':('Null', 5), 'finalAsp': ('Null', 5), 'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)}}
start_stateC = 'Constant'
final_statesC = set(['finalAsp'])
delimitadoresC = set(['\n', "'", '+', '-', '.'])
automConstant = (trans_funcC, start_stateC, final_statesC, delimitadoresC, 5)


trans_funcCh = {'Charact': {'isAspS': ('initAspS', 6), 'initAspS':('Null', 6), 'finalAspS': ('Null', 6), 'isLetra': ('Null', 6)},
                'initAspS': {'isAspS': ('Null', 6), 'initAspS':('Null', 6), 'finalAspS': ('Null', 6), 'isLetra': ('letras', 6)},
                'letras':{'isAspS': ('finalAspS', 6), 'initAspS':('Null', 6), 'finalAspS': ('Null', 6), 'isLetra': ('Null', 6)}}
start_stateCh = 'Charact'
final_statesCh = set(['finalAspS'])
delimitadoresCh = set(['\n', " ", '+', '-', '$', '.'])
automChar = (trans_funcCh, start_stateCh, final_statesCh, delimitadoresCh, 6)


trans_funcM = {'Middle': {'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'letras': {'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'isEmp': {'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'digit':{'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'is$':{'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'this_':{'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)},
                'is.':{'isLetra': ('letras', 7), 'Emp': ('isEmp', 7), 'isDigit': ('digit', 7), '$': ('is$', 7), '_': ('this_', 7), '.': ('is.', 7)}}
start_stateM = 'Middle'
final_statesM = set(['letras','digit', 'isEmp', 'is$', 'this_', 'is.'])
delimitadoresM = set(['"', "'", '+', '-', '.'])
automMiddleStr = (trans_funcM, start_stateM, final_statesM, delimitadoresM, 7)


autmoList = (automIdentifier, automFunction, automDecimal, automExponent, automFloat,automConstant, automChar, automMiddleStr)