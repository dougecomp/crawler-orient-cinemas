# README #

Este projeto tem o intuito de aprender a utilizar o Git e também a utilizar um framework Python próprio para crawler chamado Scrapy.

### How do I get set up? ###

* Para rodar o crawler deve-se instalar primeiro o [Scrapy](http://www.scrapy.org)
* Depois basta configurar o e-mail e senha no arquivo CinemaSpider.py e executar scrapy runspider CinemaSpider.py. O crawler irá varrer a página do cinema e me enviar um email com os filmes (sinopses,posters,etc...)
* Recentemente o gmail apresentou uma nível maior de segurança que não permite que softwares menos confiáveis enviem e-mail. É necessário desativar esse recurso quando precisar usar o crawler e seu e-mail for gmail.