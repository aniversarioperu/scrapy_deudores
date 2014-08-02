# Descarga la lista de deudores al Estado peruano

El buscador de deudores al Estado peruano no es muy amigable:
<http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verWeb>

Con este software te puedes bajar toda la información de todos los deudores.
El minjus tiene organizada la info por registros. Cada registro tiene un número
``id`` numérico que se incrementa a partir del ``1``.

Si hay un deudor con varias deudas entonces tendrá varios números ``id``. Con
el número ``id`` se puede acceder a la cartilla del deudor. Ejemplo para el
"doc" Vladimiro Montesinos:
<http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=317>

## Requisitos
* git
* Python2.7

## Procedimiento

* Descarga el software: ``git clone https://github.com/aniversarioperu/scrapy_deudores.git``
* Es necesario ingresar el rango de ``ids`` a descargar. Para descargar los 
registros del 1 al 100 hacer lo siguiente:  
    ``scrapy crawl deudor -a start_id=1 -a end_id=100 -o deudores.json``
