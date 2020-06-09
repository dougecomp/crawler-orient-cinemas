#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 17/11/2014

@author: douglas
'''
from scrapy.spider import Spider
from mailer import Mail

class CinemaSpider(Spider):
    '''
    classdocs
    '''
    
    name = 'cinema'
    start_urls = ['http://boulevardfeira.com.br/cinema/']

    def parse(self, response):

        mensagem = ""
        
        # capturando o filme de destaque
        destaque = response.selector.xpath('//div[contains(@class, "destaque")]/div[contains(@class, "baseline")]')[0]

        # Retirando o // do início o xpath a busca se torna relativa
        # Retorna um vetor mas como sempre vai ser de uma posição só, então basta acessasr a primeira e única posição
        fotoDestaque = destaque.xpath('div[contains(@class, "thumb_destaque")]/div[contains(@class, "imagem")]/a/img/@src').extract()[0]

        # Captura a segunda ocorrencia do <p> e extrai a sinopse do filme em destaque
        sinopseDestaque = destaque.xpath('div[contains(@class, "sinopse")]/p').extract()[1]

        # Captura o html dentro da <ul> contendo as <li>s com os horários
        horariosDestaque = destaque.xpath('div[contains(@class, "thumb_destaque")]/div[contains(@class, "informacoes")]/div/ul').extract()[0]

        mensagem = mensagem + "<img src=\"" + fotoDestaque.encode('utf-8') + "\" alt=\"\"> <br> Sinopse: " + sinopseDestaque.encode('utf-8') + " <br> Horários: " + horariosDestaque.encode('utf-8') + "<br>"

        # capturando as divs com as informações dos demais filmes
        filmes = response.selector.xpath('//div[contains(@class, "mais_filmes")]/div[contains(@class, "filme")]')

        for filme in filmes:

            # capturando o link da foto do filme
            poster = filme.xpath('div[contains(@class, "thumb")]/a/img/@src').extract()[0]

            # capturando as sinopses dos filmes
            sinopse = filme.xpath('div[contains(@class, "cont_filme")]/div[contains(@class, "sinopse")]/p').extract()[1]

            # capturando os horários dos filmes
            horarios = filme.xpath('div[contains(@class, "informacoes")]/div/ul').extract()[0]

            mensagem = mensagem + "<img src=\"" + poster.encode('utf-8') + "\" alt=\"\"> <br> Sinopse: " + sinopse.encode('utf-8') + "<br> horários: " + horarios.encode('utf-8') + "<br>"

        #server = 'smtp.gmail.com'
        #port = 587

        sender = 'seu@email.com'
        password = 'senhaseuemail'
        subject = 'Horários do Cinema do Boulevard Shopping'
        body = mensagem
        
        mail = Mail()
        mail.send(sender, password, subject, body)