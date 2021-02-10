from boggle import Boggle
from flask import Flask,request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY']='zoro'
debug = DebugToolbarExtension(app)

boggle_game = Boggle()
score = 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/board', methods=["POST"])
def board_created():
    session['user'] = request.form['user']
    session['board'] = boggle_game.make_board()
    return render_template('board.html', score = score)

@app.route('/checkWord')
def checkWord():
    words = boggle_game.words
    word = request.args['str']
    board = session['board']
    # print(board)
    # print(f'VAlue of word = {word}')
    # if word in words:
    #     result = boggle_game.check_valid_word(board,word)
    #     return jsonify({'result':result})
    #     # print('after check valid')
    # else:
    #     print('not in list')
    result = boggle_game.check_valid_word(board,word)
    print(f'value of result in route {result}')
    if result == 'ok':
        flash('Word found it', 'success')
    if result == 'not-on-board':
        flash('Sorry that word is not on the board ', 'error')
    if result == 'not-word':
        flash('Sorry that is not a word ', 'error')
    return jsonify({'result':result})


#  delete the print from app and boogle function then jsonify the value of result and create flash msgs 
# add the score by 1 when the result is OK 