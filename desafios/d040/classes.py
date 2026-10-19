class Usuario:
  def __init__(self, nome:str, email:str):
    self.nome = nome
    self.email = email

class Aluno:
  def __init__(self, nome:str, curso:str, periodo:str):
    self.nome = nome
    self.curso = curso
    self.periodo = periodo

class JSON:
  def exportar(self, dados):
    from json import dumps
    lista = []
    for item in dados:
      lista.append(item.__dict__)
    return dumps(lista, ensure_ascii=False, indent=4)


class XML:
  def exportar(self, dados):
    import xml.etree.ElementTree as ET
    nome = dados[0].__class__.__name__.lower()
    pai = ET.Element("dados")
    for item in dados:
      filho = ET.SubElement(pai, nome)
      for chave, valor in item.__dict__.items():
        subfilho = ET.SubElement(filho, chave)
        subfilho.text = str(valor)
    ET.indent(pai, space="\t",)
    return ET.tostring(pai, encoding="unicode", xml_declaration=True)

def exportar_dados(exportador, dados):
  print(exportador.exportar(dados))