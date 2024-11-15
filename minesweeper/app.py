from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

def generate_board(num_mines):
    board = [[0 for _ in range(5)] for _ in range(5)]
    for _ in range(num_mines):
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if board[row][col] == 0:
                board[row][col] = 1
                break
    return board

def check_mines(board, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < 5 and 0 <= j < 5 and board[i][j] == 1:
                count += 1
    return count

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    num_mines = data.get('num_mines', 10)
    board = generate_board(num_mines)
    return jsonify({'board': board})

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    board = data['board']
    row = data['row']
    col = data['col']
    if board[row][col] == 1:
        return jsonify({'status': 'game over'})
    else:
        count = check_mines(board, row, col)
        return jsonify({'status': 'safe', 'count': count})

if __name__ == '__main__':
    app.run(debug=True)
