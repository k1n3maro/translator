"""
Web Translator Lab
"""

from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    r = translator.english_to_french(textToTranslate)
    return r

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    r = translator.french_to_english(textToTranslate)
    return r

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()