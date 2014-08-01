# -*- coding: utf-8 -*-
import scrapy

from scrapy.items import ScrapyDeudoresItem as Item

locale.setlocale(locale.LC_ALL, "en_US.UTF8")

class DeudorSpider(scrapy.Spider):
    name = "deudor"
    allowed_domains = ["pisaq.minjus.gob.pe"]
    max_id = 1000

    start_urls = (
            'http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=',
    )

    def start_requests(self):
        for i in range(self.max_id):
            yield
            Request('http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=' + str(i),
                    callback=self.parse)

    def parse(self, response):
        item = Item()

        sel = response.xpath

        sele = sel("//td[@class='formularioColumna']/text()").extract()
        item['nombres'] = sele[2].strip()
        item['apellidos'] = sele[5].strip()
        item['dni'] = sele[8].strip()
        item['domicilio'] = sele[11].strip()
        item['delito'] = sele[14].strip()

        # check!
        item['entidad_agraviada'] = sele[17].strip()

        item['fecha_sentencia'] = sele[20].strip()
        item['fecha_ejecutoria'] = sele[23].strip()
        item['juzgado'] = sele[26].strip()
        item['expediente'] = sele[29].strip()
        item['solidaria'] = sele[32].strip()

        sele = sel("//td[@class='formularioColumna']/div[@align='center']/text()").extract()
        item['reparacion_civil'] = locale.atoif(sele[0])
        item['intereses'] = locale.atoif(sele[1])
        item['monto_total'] = locale.atoif(sele[2])
        item['pagos_realizados'] = locale.atoif(sele[3])
        item['pagos_pendientes'] = locale.atoif(sele[4])
        item['url'] = response.url

        yield item
