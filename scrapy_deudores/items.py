# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDeudoresItem(scrapy.Item):
    # define the fields for your item here like:
    nombres = scrapy.Field()
    apellidos = scrapy.Field()
    dni = scrapy.Field()
    domicilio = scrapy.Field()
    delito = scrapy.Field()
    entidad_agraviada = scrapy.Field()
    fecha_sentencia = scrapy.Field()
    fecha_ejecutoria = scrapy.Field()
    juzgado = scrapy.Field()
    expediente = scrapy.Field()
    solidaria = scrapy.Field()
    reparacion_civil = scrapy.Field()
    intereses = scrapy.Field()
    monto_total = scrapy.Field()
    pagos_realizados = scrapy.Field()
    pagos_pendientes = scrapy.Field()
    url = scrapy.Field()
