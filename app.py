# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:18:55 2023

@author: barbora.filova
"""

from flask import Flask, render_template, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
   return render_template('index.html')

# Unicode symbols for the chess pieces

WHITE_PIECES = {
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
}

BLACK_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
}

# Initial chessboard setup (empty chessboard)
chessboard = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

# Function to convert chessboard state to Unicode symbols
def convert_to_unicode(chessboard_state):
    # Rotate the chessboard state 180 degrees
    rotated_chessboard_state = [row[::-1] for row in chessboard_state[::-1]]

    unicode_chessboard = []
    for row in rotated_chessboard_state:
        unicode_row = [WHITE_PIECES.get(piece, BLACK_PIECES.get(piece, piece)) for piece in row]
        unicode_chessboard.append(unicode_row)
    return unicode_chessboard

# Function to get the chessboard state
@app.route('/get_chessboard', methods=['GET'])
def get_chessboard():
    unicode_chessboard = convert_to_unicode(chessboard)
    return jsonify(unicode_chessboard)

if __name__ == '__main__':
    app.run(debug=True)
