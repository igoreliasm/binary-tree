#!/usr/bin/env python
# -*- coding: utf-8 -*-
from no import No

class Arvore:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def __setitem__(self, chave, valor):
        self.inserir(chave, valor)

    def __delitem__(self, chave):
        self.deletar(chave)

    def __len__(self):
        return self.tamanho

    def __getitem__(self, chave):
        return self.get(chave)

    def __contains__(self, chave):
        if self._get(chave, self.raiz):
            return True
        else:
            return False
    
    def quantidade(self):
        return self.tamanho

    def inserir(self, chave, val):
        if self.raiz:
            self._inserir(chave, val, self.raiz)

        else:
            # arvore iniciada
            self.raiz = No(chave, val)
        self.tamanho = self.tamanho + 1

    def _inserir(self, chave, val, noCorrente):
        # valor chave do nó é menor doque o atual nó
        if chave < noCorrente.chave:
            if noCorrente.temFilhoEsquerda():
                self._inserir(chave, val, noCorrente.esquerda)
            else:
                noCorrente.esquerda = No(chave, val, pai = noCorrente)
        else:
            if noCorrente.temFilhoDireita():
                self._inserir(chave, val, noCorrente.direita)
            else:
                noCorrente.direita = No(chave, val, pai = noCorrente)

    def get(self, chave):
        if self.raiz:
            res = self._get(chave, self.raiz)
            if res:
                return res.carga
            else:
               return None
        else:
            return None

    # função auxiliar
    # recebendo um nó e sua chave correta conseguimos retornar corretamente 
    # o nó de acordo com sua chave correta
    def _get(self, chave, noCorrente):
        if not noCorrente:
            return None
        elif noCorrente.chave == chave:
           return noCorrente
        elif chave < noCorrente.chave:
            return self._get(chave, noCorrente.temFilhoEsquerda)
        else:
            return self._get(chave, noCorrente.temFilhoDireita)

    def deletar(self, chave):
        if self.tamanho > 1:
            # adquirindo o nó corretamente de acordo com sua chave
            # atualmente só temos a chave
            noParaDeletar = self._get(chave, self.raiz)
            if noParaDeletar:
                self.remover(noParaDeletar)
                # decrementando o tamanho da arvore
                self.tamanho = self.tamanho - 1
            else:
                raise KeyError('Chave nao encontrada na arvore atual')
        # esfaziamos a lista caso possuir apenas 1 elemento
        elif self.tamanho == 1 and self.raiz.chave == chave:
            self.raiz = None
            self.tamanho = self.tamanho - 1
        else:
            raise KeyError('Chave nao encontrada na arvore atual')

    #esvaziar toda a arvore
    def esvaziar(self,arvore):
        if arvore!=None:
            arvore = None
            self.tamanho = 0
            print("Sua Arvore esta vazia!")
        else:
            print("Sua Arvore esta vazia!")

    # buscar sucessor
    def buscarSucessor(self):
        sucessor = None
        if self.temFilhoDireita():
            sucessor = self.direita.chaveMinima()
        else:
            if self.pai:
                if self.ehFilhoEsquerda():
                    sucessor = self.pai
                else:
                    self.pai.direita = None
                    # retursiva
                    sucessor = self.pai.buscarSucessor()
                    self.pai.direita = self
        return sucessor

    # chave minima em uma sub arvore
    def chaveMinima(self):
        corrente = self
        while corrente.temFilhoEsquerda():
            corrente = corrente.esquerda
        return current

    def removerSucessor(self):
        if self.ehFolha():
            if self.ehFilhoEsquerda():
                self.pai.esquerda = None
            else:
                self.pai.direita = None

        elif self.temAlgumFilho():
            if self.temFilhoEsquerda():
                if self.ehFilhoEsquerda():
                    self.pai.esquerda = self.esquerda
                else:
                    self.pai.direita = self.esquerda
                    self.esquerda.pai = self.pai
        else:
            if self.ehFilhoEsquerda():
                self.pai.esquerda = self.direita
            else:
                self.pai.direita = self.direita
                self.direita.pai = self.pai


    def remover(self, noCorrente):
        # verificando se o no atual é folha
        if noCorrente.ehFolha():
            if noCorrente == noCorrente.pai.esquerda:
                noCorrente.pai.esquerda = None
            else:
                noCorrente.pai.direita = None

        elif noCorrente.temTodosFilhos():
            sucessor = noCorrente.sucessor()
            sucessor.removerSucessor()
            noCorrente.chave = sucessor.chave
            noCorrente.carga = sucessor.carga

        # tem apenas um filho
        else:
            if noCorrente.temFilhoEsquerda():
                if noCorrente.ehFilhoEsquerda():
                    noCorrente.esquerda.pai = noCorrente.pai
                    noCorrente.pai.esquerda = noCorrente.esquerda
            
                elif noCorrente.ehFilhoEsquerda():
                    noCorrente.esquerda.pai = noCorrente.pai
                    noCorrente.pai.direita = noCorrente.esquerda
            
                else:
                    noCorrente.alterarDadosNo(
                        noCorrente.esquerda.chave, 
                        noCorrente.esquerda.carga, 
                        noCorrente.esquerda.esquerda,
                        noCorrente.esquerda.direita
                )
            else:
                if noCorrente.ehFilhoEsquerda():
                    noCorrente.direita.pai = noCorrente.pai
                    noCorrente.pai.esquerda = noCorrente.direita
                
                elif noCorrente.ehFilhoDireita():
                    noCorrente.direita.pai = noCorrente.pai
                    noCorrente.pai.direita = noCorrente.direita
                else:
                    noCorrente.alterarDadosNo(
                        noCorrente.direita.chave,
                        noCorrente.direita.carga,
                        noCorrente.direita.esquerda,
                        noCorrente.direita.direita
                    )