# -*- coding: utf-8 -*-
import locale

import scrapy
from scrapy_deudores.items import ScrapyDeudoresItem as Item
from scrapy.http import Request

locale.setlocale(locale.LC_ALL, "en_US.UTF8")


class DeudorSpider(scrapy.Spider):
    name = "deudor"
    allowed_domains = ["pisaq.minjus.gob.pe"]

    def __init__(self, start_id='', end_id=''):
        self.start_id = int(start_id)
        self.end_id = int(end_id)

    def start_requests(self):
        for i in range(self.start_id, self.end_id + 1):
            url = 'http://pisaq.minjus.gob.pe:8080/sisca_web/'
            url += 'DeudoresWebAction_verDeudorWeb.action?deudor.id=' + str(i)
            yield Request(url, callback=self.parse)

    def parse(self, response):
        item = Item()

        sel = response.xpath

        sele = sel("//td[@class='formularioColumna']/text()").extract()
        item['nombres'] = sele[2].strip().replace("\n", " -")
        item['apellidos'] = sele[5].strip().replace("\n", " -")
        item['dni'] = sele[8].strip().replace("\n", " -")
        item['domicilio'] = sele[11].strip().replace("\n", " -")
        item['delito'] = sele[14].strip().replace("\n", " -")

        # check!
        item['entidad_agraviada'] = sele[17].strip().replace("\n", " -")

        item['fecha_sentencia'] = sele[20].strip().replace("\n", " -")
        item['fecha_ejecutoria'] = sele[23].strip().replace("\n", " -")
        item['juzgado'] = sele[26].strip().replace("\n", " -")
        item['expediente'] = sele[29].strip().replace("\n", " -")
        item['solidaria'] = sele[32].strip().replace("\n", " -")

        sele = sel("//td[@class='formularioColumna']/div[@align='center']/text()").extract()
        item['reparacion_civil'] = locale.atof(sele[0])
        item['intereses'] = locale.atof(sele[1])
        item['monto_total'] = locale.atof(sele[2])
        item['pagos_realizados'] = locale.atof(sele[3])
        item['pagos_pendientes'] = locale.atof(sele[4])
        item['url'] = response.url.replace("\n", " -")

        yield item
