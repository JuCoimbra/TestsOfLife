#TODO:
#   funcao proximo_simbolo() -> retornar proximo simbolo do texto fonte com base em magia negra
#       cada chamada dessa funcao pede 
#           1) posicao corrente do codigo fonte
#           2) codigo do atomo formado ( parametro de retorno )
#           3) indice da tabela de simbolos onde o atomo foi gravado 
#   implementar o limite de 35 caracteres para cada atomo
#   implementar a filtragem de comentarios (tem que ser na analise lexica, para persistir o numero correto de linhas )
#   Tabela de simbolos
#        - acertar o tipo do simbolo
#        - so armazenar 35 primeiros carecteres validos
#   Tabela_Simbolos.gerar_tabela() -> arquivo .TAB
#   Analise_Lexica.gerar_analise() -> arquivo .LEX


import atomos
import os
import sys
import lexLib as lex

# Declaracao de estrutura de um Identifier contem
# id
# lexeme
# codigo 
# qnt. antes do truncamento
# qnt. depois do truncamento
# tipo
# numero da linha que foi encontrado pelas primeiras cinco vezes

class Identifier: 
    def __init__(self, _id, _lexeme, _codigo, _qtat, _qtdt, _tipo, _linha):
        self.id = _id
        self.lexeme = _lexeme
        self.codigo = _codigo
        self.qtat = _qtat
        self.qtdt = _qtdt
        self.tipo = _tipo
        self.linha = _linha

# Declaracao de estrutura de um Atomo contem
# lexeme
# codigo 
# indice na tabela de simbolos

class Atomo:
    def __init__(self, _lexeme, _codigo, _idx_tabela_simbolos):
        self.lexeme = _lexeme
        self.codigo = _codigo
        self.idx_tabela_simbolos = _idx_tabela_simbolos
          

tabela_simbolos = []
listaDeAtomos = []
atomos = atomos.atomos


def main():

    path = input('Insira o nome do arquivo, sem extensão. Caso o arquivo esteja em outra pasta, especifique o diretorio:')
    
    with open(path+'.dks', 'r') as f:
     textofonte = f.readlines()
     for line in textofonte:

          isComent = lex.filtrar(line, textofonte)
          posicao = isComent[1]
          line = isComent[0]

          while posicao != len(line) and line != '\n':
               atomoTupla = lex.atomoPorAtomo(line, posicao, len(line)-1)
               if atomoTupla[0] != (-1):
                    if atomoTupla[3] == 'identifier':
                        tabela_simbolos.append(len(tabela_simbolos), atomos[atomoTupla[4]], atomoTupla[0])
                    listaDeAtomos.append([atomoTupla[0], atomos[atomoTupla[4]], lex.procurar_simbolo_na_tabela(atomoTupla[0], tabela_simbolos)])
               posicao = atomoTupla[1] + 1
     
     


    # Gera arquivo .TAB
    lex.gerar_tabela_simbolos(tabela_simbolos)
    # Gera arquivo .LEX
    lex.relatLex(listaDeAtomos, path)

    f.close()



if __name__ == "__main__":
    main()
