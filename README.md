# Servicio de Impresión con Flask

Este proyecto es un servicio de impresión simple construido con Flask. Permite imprimir texto e imágenes en una impresora local.

## Dependencias

El proyecto depende de las siguientes bibliotecas:

- Flask
- flask_cors
- escpos.printer
- PIL
- requests

## Instalación

Para instalar las dependencias, puedes usar pip:

```bash
pip install flask flask_cors python-escpos pillow requests
```

## Configuración

Para poner en marcha el servidor localmente es muy necesario ejecutar en un CMD en Windows el siguiente comando:

```bash
net use lpt1: "\\computername\sharedprinter" /persistent:yes
```

## Uso

El servicio expone una ruta /imprimir que acepta solicitudes POST con un cuerpo JSON. Los campos del JSON son:

logo: URL de la imagen del logo para imprimir en el recibo.
titulo: Texto del título para imprimir en el recibo.
cuerpo: Texto del cuerpo para imprimir en el recibo.
Ejemplo de uso con una petición POST usando JavaScript:

```bash
var xhr = new XMLHttpRequest();
var url = "http://localhost:5000/imprimir";

xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");

var data = JSON.stringify({
    "logo": "http://example.com/logo.png",
    "titulo": "Mi Tienda",
    "cuerpo": "Gracias por su compra"
});

xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        console.log(json.mensaje); // Imprime "Impresión exitosa"
    }
};

xhr.send(data);
```

