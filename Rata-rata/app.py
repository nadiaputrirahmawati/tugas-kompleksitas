from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    show_result = True
    # Ambil data dari form
    n = int(request.form['n'])
    data = request.form['data']
    
    # Ubah data string menjadi list angka
    data_list = [float(x) for x in data.split(',')]
    
    if len(data_list) != n:
        return render_template('index.html', error="Jumlah data tidak sesuai dengan nilai n yang dimasukkan.")
    
    # Hitung rata-rata
    jumlah = sum(data_list)
    rerata = jumlah / n
    
    return render_template('index.html', rerata=rerata, show_result=show_result, data = data, n=n)

if __name__ == '__main__':
    app.run(debug=True)
