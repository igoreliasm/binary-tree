#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from arvore import Arvore

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def esvaziar():
    print("Sua árvore está vazia!")
    exit()

def imprimirArvore():
    pass

def menu():
    print("Menu de utilização")
    print("1 - Árvore vazia.")
    print("2 - Incluir um nó.")
    print("3 - Excluir um nó.")
    print("4 - Retornar tamanho da árvore.")
    print("5 - Sair.")
    print("\n")

def integrantes():
    print("\n")
    print("** Disciplina de estrutura de dados **")
    print("Integrantes da implementação de árvore binária:")
    print("Alessandro Rocha")
    print("Bruno Wantil")
    print("Igor Elias")
    print("Lucas Bucker")
    print("Romantiezer Beloni")
    print("\n")

if __name__ == "__main__":
    integrantes()
    menu()

    arvore = Arvore()

    continuar = True
    while continuar:
        op = int(raw_input("Entre com uma opção válida: "))

        if op == 1:
            esvaziar()

        elif op == 2:
            print("Onde deseja inserir o nó? ")
            posicao = int(raw_input("Ex.: 5: "))
            item = int(raw_input("Entre com o nó desejado: "))
            arvore[posicao] = item

        elif op == 3:
            item = int(raw_input("Digita a chave do nó que deseja remover: "))
            arvore.deletar(item)

        elif op == 4:
            print("Tamanho da árvore: ")
            print(arvore.quantidade())
            
        elif op == 5:
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
            integrantes()
            menu()