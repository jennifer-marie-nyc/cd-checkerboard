from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board_8_by_8():
    return render_template('index.html', width=8, height=8, color1="black", color2="red")

@app.route('/4')
def board_8_by_4():
    return render_template('index.html', width=8, height=4, color1="black", color2="red")

@app.route('/<int:x>/<int:y>')
def board_size(x, y):
    return render_template('index.html', width=x, height=y, color1="black", color2="red")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def board_size_colors(x, y, color1, color2):
    return render_template('index.html', width=x, height=y, color1=color1, color2=color2)

if __name__=='__main__':
    app.run(debug=True, host='localhost', port='5150')