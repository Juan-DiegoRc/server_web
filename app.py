from flask import Flask, request, redirect, send_from_directory, render_template
import os

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

UPLOAD_FOLDER = 'uploads'  # Carpeta donde se guardarán los archivos subidos
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Si la carpeta 'uploads' no existe, la crea
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Página principal - muestra el formulario de subida y los archivos disponibles
@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)  # Lista los archivos en la carpeta de subidas
    return render_template('index.html', files=files)

# Ruta para subir archivos (se activa al enviar el formulario por POST)
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:  # Si no se envió ningún archivo
        return 'No file part'
    file = request.files['file']
    if file.filename == '':  # Si el nombre del archivo está vacío
        return 'No selected file'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))  # Guarda el archivo
    return redirect('/')  # Redirige al inicio

# Ruta para descargar archivos
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# Inicia la aplicación en el puerto 8080, visible desde cualquier IP
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)