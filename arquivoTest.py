import pandas as pd
import os


def relatLex(d, nomeArq):
     inic = '''"Relatório da Análise Léxica"\n
Domingos - 
Juliane Amaral Reis Coimbra - juliane.coimbra@aln.senaicimatec.edu.br - (71) 99681-9629
Luiz - 
Matheus Carvalho Nascimento de Souza - matheus@aln.senaicimatec.edu.br - (71) 91979719\n\n'''

     df = pd.DataFrame(d, columns = ['Lexeme','Código','Posi. Tabela de SImbolos'])
     relatNome ='RelatórioLexico'+nomeArq
     with open(relatNome+'.LEX', 'w') as f:
          f.write(inic)
          dfAsString = df.to_string(header=True, index=True)
          f.write(dfAsString)

def whatIs(caracter):
     print(any(map(str.isalpha, caracter)))
     if any(map(str.isdigit, caracter)):
          return 'isDigit'
     elif any(map(str.isalpha, caracter)):
          return 'isLetra'
     elif caracter == '_':
          return caracter
     else:
          return 'NULL'

demilitadores = set([" ", '(', ')', ',', ':', ';', "'", '{', '}', '"', '[', ']', '=', '/','\n'])

def atomoPorAtomo(line, posicao, lenLine):
     state = automIdentifier[1]
     posicaoIni = posicao
     atomo = ''

     while line[posicao] not in demilitadores and (posicao - posicaoIni <= 35):
          caracter = line[posicao]
          if whatIs(caracter) != 'NULL' and state != 'NULL':
               state = trans_func.get(state, 'NULL').get(caracter, 'NULL')
               if state != 'NULL':
                    atomo = atomo + caracter
          
          if int(posicao) == int(lenLine): 
               break
          else:
               posicao += 1

     if state in final_states:
          resultado = [atomo, posicao, 1]
          return resultado
     else: 
          resultado = [-1, posicao, 1]
          return resultado
     

      
trans_func = {'identifier': {'isLetra': 'letras', '_': 'this_', 'isDigit': 'NULL'},
               'letras': {'isLetra': 'letras', '_': 'this_', 'isDigit': 'digit'},
               'digit': {'isLetra': 'letras', '_': 'this_', 'isDigit': 'digit'},
               'this_': {'isLetra': 'letras', '_': 'this_', 'isDigit': 'digit'}}
start_state = 'identifier'
final_states = set(['letras','digit', 'this_'])
automIdentifier = (trans_func, start_state, final_states)

d = []
nomeArquivo = 'mecompile'
with open(nomeArquivo+'.dks', 'r') as f:
     textofonte = f.readlines()

     for line in textofonte:
          posicao = 0
          while posicao != len(line):
               atomoTupla = atomoPorAtomo(line, posicao, len(line)-1)
               if atomoTupla[0] != (-1):
                    d.append([atomoTupla[0], 'Código do lexeme', atomoTupla[2]])
               posicao = atomoTupla[1] + 1
     
     relatLex(d, nomeArquivo)
     f.close()

     

#myAUT()