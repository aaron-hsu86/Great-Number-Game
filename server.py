from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret_number'

@app.route('/')
def welcome():
    # session.clear()
    if 'answer' not in session:
        session['answer'] = int(random.randint(1, 100))
        session['guess_count'] = 5
        session['guess_check'] = 'none'

    return render_template('index.html')


@app.route('/guess', methods=['post'])
def make_a_guess():
    guess = int(request.form['num_guess'])
    answer = session['answer']
    session['num_guess'] = int(request.form['num_guess'])
    # print(answer)

    if guess == answer:
        session['guess_check'] = 'correct'
    elif guess < answer:
        session['guess_check'] = 'lower'
    elif guess > answer:
        session['guess_check'] = 'higher'

    if session['guess_count'] > 0:
        session['guess_count'] -= 1

    return redirect('/')


@app.route('/game_over')
def game_over():
    session['answer'] = int(random.randint(1, 100))
    session['guess_count'] = 5
    session['guess_check'] = 'none'
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

