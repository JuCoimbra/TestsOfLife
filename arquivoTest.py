import pandas as pd
import automatos as atm
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

def whatIs(caracter, autom):
     print(any(map(str.isalpha, caracter)))
     if any(map(str.isdigit, caracter)):
          return 'isDigit'
     elif any(map(str.isalpha, caracter)) and autom != 2 and autom != 3:
          return 'isLetra'
     elif any(map(str.isalpha, caracter)) and caracter == 'e' and autom == 2 and autom == 3:
          return 'e'
     elif caracter == '_' or '+' or '-' or '.' or '$':
          return caracter
     elif caracter == " ":
          return 'Emp'
     elif caracter == '"':
          return 'is"'
     elif caracter == "'":
          return 'isAspS'
     else:
          return 'NULL'

demilitadores = set(['(', ')', ',', ':', ';', '{', '}', '[', ']', '=', '/','\n'])

def atomoPorAtomo(line, posicao, lenLine):
     posicaoIni = posicao

     for autom in atm.autmoList:
          state[0] = autom[1]
          state[1] = autom[4]
          atomo = ''
          posicao = posicaoIni
          while line[posicao] not in demilitadores and (posicao - posicaoIni <= 35):
               caracter = line[posicao]

               if whatIs(caracter) != 'NULL' and state != 'NULL' and state[1] == autom[4]:
                    state = autom[0][state[0]][whatIs(caracter)]
                    if state[0] != 'NULL':
                         atomo = atomo + str(caracter).upper()

               elif whatIs(caracter) != 'NULL' and state != 'NULL' and state[1] != autom[4]:
                    state = atm.autmoList[state[1]][0][state[1]][whatIs(caracter)]


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
               for autom in atm.autmoList:
                    atomoTupla = atomoPorAtomo(line, posicao, len(line)-1)
               #
               #if atomoTupla[0] != (-1):
               #     d.append([atomoTupla[0], 'Código do lexeme', atomoTupla[2]])
               #posicao = atomoTupla[1] + 1
     
     relatLex(d, nomeArquivo)
     f.close()

     

#myAUT()