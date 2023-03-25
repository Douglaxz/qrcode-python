from flask import Flask, render_template, request, redirect, url_for
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

#rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #pegar os campos da pagina html
        name = request.form.get('name')
        linkedin = request.form.get('linkedin')
        github = request.form.get('github')
        #mensagem
        message = f"Oi, meu nome é {name}, meu link para o LinkedIn é {linkedin} e o meu link para o GitHub é {github}"
        #gerar qrcode
        img = qrcode.make(message)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        nameuser = name
        #redirecionar para a pagina qr com a imagem
        return render_template('qr.html', img_str=img_str,nameuser=nameuser)
    return render_template('index.html')

@app.route('/generate')
def generate():
    #recebe os dados para geração
    name = request.args.get('name')
    linkedin = request.args.get('linkedin')
    github = request.args.get('github')
    message = f"Oi, meu nome é {name}, meu link para o LinkedIn é {linkedin} e o meu link para o GitHub é {github}"
    img = qrcode.make(message)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    nameuser = name
    return render_template('qr.html', img_str=img_str, nameuser=nameuser)

if __name__ == '__main__':
    app.run(debug=True)
