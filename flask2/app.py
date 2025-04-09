from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
# Секретный ключ нужен для работы сессий
app.secret_key = 'your_secret_key_here'


@app.route('/', methods=['GET', 'POST'])
def index():
    # Если в сессии нет числа, загадываем его
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 10)

    feedback = None

    if request.method == 'POST':
        guess_str = request.form.get('guess')
        if guess_str:
            try:
                guess = int(guess_str)
                secret_number = session['secret_number']

                if guess < secret_number:
                    feedback = "Загаданное число больше!"
                elif guess > secret_number:
                    feedback = "Загаданное число меньше!"
                else:
                    feedback = f"Поздравляю! Вы угадали число {secret_number}."
                    # Сразу загадываем новое число, чтобы можно было играть дальше
                    session['secret_number'] = random.randint(1, 10)
            except ValueError:
                feedback = "Пожалуйста, введите целое число."

    return render_template('index.html', feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)