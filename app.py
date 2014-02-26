from flask import Flask
from flask import request
from flask import Markup
from flask import render_template as st
from mikoto.libs.text import render
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		md_content = request.form['md_content']
		html = Markup(render(md_content))
	return st('index.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)