import pandas as pd
import automatos as atm
import os

def gerar_tabela_simbolos(dados):
     count = 0
     simbolos = []

     cabecalho = '''\n
Domingos Ferreira Viana Neto - \n
Juliane Amaral Reis Coimbra - juliane.coimbra@aln.senaicimatec.edu.br - (71) 99681-9629\n
Luiz Henrique Correa da Costa - luiz.costa@aln.senaicimatec.edu.br - (71) 99999-4882\n 
Matheus Carvalho Nascimento de Souza - matheus@aln.senaicimatec.edu.br - (71) 99308-1377\n\n'''

     for idx in range(len(dados)):
          if dados[idx][2][0:1] == "ID":
               tat = len(dados[idx][1])
               tdt = tat if tat < 35 else 35
               simbolos.append([count, dados[idx][2], dados[idx][1], tat, tdt, dados[idx][2], '-'])
               count = count + 1
     
     df = pd.DataFrame(dados, columns=['id', 'codigo', 'lexeme', 'tam_antes_trunc', 'tam_depois_trunc', 'tipo', 'linha'])

     with open('tabela_de_simbolos.TAB', 'w') as file:
               file.write(cabecalho)
               df_to_string = df.to_string(header=True, index=False)
               file.write(df_to_string)
            
def procurar_simbolo_na_tabela(lexeme, tabela):
  for simbolo in tabela:
    if lexeme == simbolo[2]:
      return simbolo[1]
  return '-'

def relatLex(d, nomeArq):
     inic = '''"Relatório da Análise Léxica"\n
Domingos Ferreira Viana Neto - 
Juliane Amaral Reis Coimbra - juliane.coimbra@aln.senaicimatec.edu.br - (71) 99681-9629
Luiz Henrique Correa da Costa - luiz.costa@aln.senaicimatec.edu.br - (71) 99999-4882
Matheus Carvalho Nascimento de Souza - matheus@aln.senaicimatec.edu.br - (71) 99308-1377\n\n'''

     df = pd.DataFrame(d, columns = ['Lexeme','Código','Posi. Tabela de Simbolos'])
     relatNome ='RelatórioLexico-'+nomeArq
     with open(relatNome+'.LEX', 'w') as f:
          f.write(inic)
          dfAsString = df.to_string(header=True, index=True)
          f.write(dfAsString)

def buscaLinha(trecho, f):
     for line in range(len(f)): 
          if f[line] == trecho:
               return f[line+1]

#funcao filtrar
#se lermos um '/' entramos nessa funcao
def filtrar(trecho, f):
     posiBarra = trecho.find('/')
     posicao = posiBarra+1

     if posiBarra >= 0 and trecho[posiBarra+1] == '/':
          novaPosi = (buscaLinha(trecho, f), 0)
          return novaPosi
          
     elif posiBarra >= 0 and trecho[posiBarra+1] == '*':
          while trecho.find('*/') < 0:
               if trecho[posicao] == '\n':
                    trecho = buscaLinha(trecho, f)
               posicao += 1
          novaPosi = (trecho, (trecho.find('*/'))+1)
          return novaPosi

     else:
          novaPosi = (trecho, 0)
          return novaPosi


def whatIs(caracter, autom):
     if any(map(str.isdigit, str(caracter).upper())):
          return 'isDigit'
     elif any(map(str.isalpha, str(caracter).upper())) and autom != 2 and autom != 3:
          return 'isLetra'
     elif any(map(str.isalpha, str(caracter).upper())) and caracter == 'E' and autom == 2 and autom == 3:
          return 'E'
     elif caracter == "_" or caracter == "+" or caracter == "-" or caracter == "." or caracter == "$":
          return caracter
     elif caracter == " " or caracter == ' ':
          return 'Emp'
     elif caracter == '"':
          return 'is"'
     elif caracter == "'":
          return 'isAspS'
     else:
          return 'Null'

delimitadores = set(['(', ')', ',', ':', ';', '{', '}', '[', ']', '=', '\n', '%', '<', '>', '#', '&', '*', '!'])

def atomoPorAtomo(line, posicao, lenLine):
     posicaoIni = posicao
     state = ("")

     for autom in atm.autmoList:
          state = (autom[1], autom[4])
          atomo = ''
          caracter = ''
          posicao = posicaoIni
          delim = delimitadores.union(autom[3])
          abreAsp = False

          while line[posicao] not in delim and (posicao - posicaoIni <= 35):
               caracter = line[posicao]

               if caracter == '"' and abreAsp == False:
                    abreAsp = True
               elif caracter == '"' and abreAsp == True:
                    abreAsp = False

               if abreAsp == False and caracter == ' ':
                    return [-1, posicao, 1, state[0]]

               if whatIs(caracter, autom) != 'Null'and state[0] != 'Null' and state[1] == autom[4]:
                    state = autom[0][state[0]][whatIs(caracter, autom)]
                    if state[0] != 'Null':
                         atomo = atomo + str(caracter).upper()
                         if int(posicao) == int(lenLine): 
                              break
                         else:
                              posicao += 1

               elif whatIs(caracter, autom) != 'Null' and state[0] != 'Null' and state[1] != autom[4]:
                    state = atm.autmoList[state[1]][0][state[0]][whatIs(caracter, autom)]

                    if state[0] != 'Null' and caracter not in atm.autmoList[state[1]][3]:
                         atomo = atomo + str(caracter).upper()

                         if int(posicao) == int(lenLine): 
                              break
                         else:
                              posicao += 1
                    elif state[0] != 'Null' and caracter in atm.autmoList[state[1]][3]: 
                         state[1] = autom[4]
                         continue

          if abreAsp == False and caracter == ' ':
                    return [-1, posicao, 1, state[0]]

          if (posicao - posicaoIni >= 35):
               resultado = [atomo, (line.find(' ', posicao)), 1, state[0]]
               return resultado     

          if state[0] in autom[2]:
               resultado = [atomo, posicao, 1, state[0]]
               return resultado

          elif atomo == '\n':
               resultado = [-1, posicao, 1, state[0]]
               return resultado
          else:
               posicao += 1
               continue
     
d = []