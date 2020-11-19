#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Spider para busca do menor preço do Moto G 2ª geração.
No momento ele consegue buscar o valor e o nome da loja que está oferecendo o preço no buscape

@author: douglas
"""
from scrapy import Spider
import smtplib

class SimpleSpider(Spider):
	name = 'simpleSpider'
	start_urls = ['http://www.buscape.com.br/prod_unico?idu=600602&ordem=prec#precos'] # Lista com os preços já ordenados por preço de forma ascendente

	def parse(self, response):

		lojas = response.xpath('//div[contains(@class, "details")]/a/img/@alt').extract(); # extrai o valor do atributo alt com o nome da loja
		loja = lojas[0].encode('utf8');

		dados = response.selector.xpath('//span[contains(@class, "integer")]/text()').extract(); # extrai o valor sem o centavos
		menorValor = dados[0]

		msg = 'O valor mais baixo do Moto G de segunda Geração está no valor de R$ ' + str(menorValor) + ' na loja ' + str(loja)

		server = 'smtp.gmail.com'
		port = 587

		sender = 'seu@email.com'
		password = 'senhaseuemail'
		recipient = 'seu@email.com'
		subject = 'Menor preço do moto g 2ª geração'
		body = msg

		"Sends an e-mail to the specified recipient."

		body = "" + body + ""

		headers = ["From: " + sender,
		           "Subject: " + subject,
		           "To: " + recipient,
		           "MIME-Version: 1.0",
		           "Content-Type: text/html"]
		headers = "\r\n".join(headers)

		session = smtplib.SMTP(server, port)

		session.ehlo()
		session.starttls()
		session.ehlo
		session.login(sender, password)

		session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
		session.quit()


		#print msg
