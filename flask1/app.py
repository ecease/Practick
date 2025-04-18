from flask import Flask, render_template

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):

    return render_template('404.html'), 404

@app.route('/404')
def index():
    return "Главная страница приложения"

if __name__ == '__main__':
    app.run(debug=True)