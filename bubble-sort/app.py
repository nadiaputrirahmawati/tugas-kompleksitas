from flask import Flask, request, render_template

app = Flask(__name__)

# Fungsi untuk mengurutkan data menggunakan algoritma pengurutan sederhana
def simple_sort(data):
    n = len(data)
    for i in range(1, n):
        for j in range(i, n):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jumlah', methods=['POST'])
def jumlah():
    jumlah = request.form['jumlah']
    return render_template('index.html', jumlah=jumlah)

@app.route('/sort', methods=['POST'])
def sort():
    jumlah = int(request.form['jumlah'])
    data = request.form['data']
    data_list = list(map(int, data.split(',')))
    if len(data_list) != jumlah:
        return render_template('index.html', error="Jumlah angka yang di masukan tidak sesuai, dengan jumlah data.", jumlah=jumlah)
    sorted_data = simple_sort(data_list)
    return render_template('index.html', sorted_data=sorted_data, data=data)

if __name__ == '__main__':
    app.run(debug=True)
