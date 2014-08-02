import json

f = "deudor.json"

objs = []
for i in open(f, "r").readlines():
    i = i.strip()
    i = json.loads(i)
    i['dni'] = str(i['dni'])
    objs.append(i)

f = open("deudor2.json", "w")
f.write(json.dumps(objs))
f.close()
