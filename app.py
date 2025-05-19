import json
from flask import Flask, render_template, request

app = Flask(__name__)

def load_content(lang):
    try:
        with open(f'static/content/content_{lang}.json', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        with open('static/content/content_de.json', encoding='utf-8') as f:
            return json.load(f)

@app.route('/')
def index():
    lang = request.args.get('lang', 'de')
    content = load_content(lang)
    return render_template('index.html', content=content, lang=lang)

if __name__ == '__main__':
    app.run(debug=True, port=3000)