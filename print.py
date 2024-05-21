from flask import Flask, request
from flask_cors import CORS
from escpos.printer import File
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# CODIGO NECESARIO PARA CORRER EN CMD: net use lpt1: "\\computername\sharedprinter" /persistent:yes


class MiImpresora:
    def __init__(self):
        self.printer = File("LPT1")

    def descargar_imagen(self, url):
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            return img
        except Exception as e:
            print("Error al desargar la imagen de %s %s" % (url, e))
            return None

    def imprimir_y_cortar(self, logo=None, titulo=None, cuerpo=None):
        if logo:
            img_logo = self.descargar_imagen(logo)
            if img_logo is not None:
                self.printer.image(img_logo)
        if titulo:
            self.printer.set(font='b', normal_textsize=True,
                             double_height=True, double_width=True)
            self.printer.text('n' + titulo)
        if cuerpo:
            self.printer.set(align='left', font='a', normal_textsize=True,
                             double_height=False, double_width=False)
            self.printer.text(cuerpo)
        self.printer.cut()
        self.printer.close()


@app.route('/imprimir', methods=['POST'])
def imprimir():
    try:
        data = request.json
        logo = data.get('logo', '')
        titulo = data.get('titulo', '')
        cuerpo = data.get('cuerpo', '')
        impresora = MiImpresora()
        impresora.imprimir_y_cortar(logo, titulo, cuerpo)
        return {"mensaje": "Impresión exitosa"}
    except Exception as e:
        print("Error al imprimir: " + str(e))


if __name__ == '__main__':
    app.run(port=5000)