from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        return redirect(url_for('result', text=text))
    return render_template('index.html')

@app.route('/result')
def result():
    text = request.args.get('text', '')
    return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)