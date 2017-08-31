#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from arvore import Arvore

#limpar a tela
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimirArvore():
    pass

def menu():
    print("Menu de utilizacao")
    print("1 - Arvore vazia.")
    print("2 - Incluir um no.")
    print("3 - Excluir um no.")
    print("4 - Retornar tamanho da arvore.")
    print("5 - Integrantes.")
    print("6 - Sair.")
    print("\n")

def integrantes():
    print("\n")
    print("** Disciplina de estrutura de dados **")
    print("Integrantes da implementacao de arvore binaria:")
    print("Alessandro Rocha")
    print("Bruno Wantil")
    print("Igor Elias")
    print("Lucas da Conceicao")
    print("Romantiezer Beloni")
    print("\n")

if __name__ == "__main__":
    menu()

    arvore = Arvore()

    continuar = True
    while continuar:
        op = int(raw_input("Entre com uma opcao valida: "))

        if op == 1:
            arvore.esvaziar(arvore)

        elif op == 2:
            posicao = int(raw_input("Entre com uma chave pare o nó:  "))
            item = int(raw_input("Entre com o no desejado: "))
            arvore[posicao] = item

        elif op == 3:
            item = int(raw_input("Digita a chave do no que deseja remover: "))
            arvore.deletar(item)

        elif op == 4:
            print("Tamanho da arvore: ")
            print(arvore.quantidade())
            
        elif op == 5:
            integrantes()

        elif op == 6:
            continuar = False
            limparTela()
            integrantes()
            exit()

        desejaContinuar = str(raw_input("Deseja continuar no sistema? [S/N]: "))
        if (desejaContinuar != 'S' and desejaContinuar != 's'):
            continuar = False
            limparTela()
        else:
            limparTela()
            menu()