#!/usr/bin/env python
# -*- coding: utf-8 -*-

class No:
    def __init__(self, chave, val, esquerda = None, direita = None, pai = None):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.pai = pai
        self.carga = val

    def temFilhoEsquerda(self):
        return self.esquerda

    def temFilhoDireita(self):
        return self.direita

    def ehFolha(self):
        return not (self.esquerda or self.direita)

    def ehFilhoEsquerda(self):
        return self.pai and self.pai.esquerda == self

    def ehFilhoDireita(self):
        return self.pai and self.pai.direita == self

    def temTodosFilhos(self):
        return self.direita and self.esquerda

    def temAlgumFilho(self):
        return self.direita or self.esquerda

    def alterarDadosNo(self, chave, valor, esquerda, direita):
        self.chave = chave
        self.carga = valor
        self.esquerda = esquerda
        self.direita = direita
        
        if self.temFilhoEsquerda():
            self.esquerda.pai = self
        
        if self.temFilhoDireita():
            self.direita.pai = self
