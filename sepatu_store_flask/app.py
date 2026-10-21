import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi folder upload foto dari laptop/komputer
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Membuat folder uploads secara otomatis jika belum ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Data sepatu awal
data_sepatu = [
    {"id": 1, "nama": "Nike Air Force 1 '07", "kategori": "Lifestyle", "harga": "1.549.000", "stok": 12, "gambar": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=500"},
    {"id": 2, "nama": "Adidas Ultraboost Light", "kategori": "Running", "harga": "2.800.000", "stok": 8, "gambar": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=500"},
    {"id": 3, "nama": "Puma Suede Classic", "kategori": "Casual", "harga": "1.099.000", "stok": 15, "gambar": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=500"},
    {"id": 4, "nama": "New Balance 550", "kategori": "Retro", "harga": "1.999.000", "stok": 5, "gambar": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=500"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produk')
def produk():
    return render_template('produk.html', sepatu_list=data_sepatu)

@app.route('/tambah-produk', methods=['GET', 'POST'])
def tambah_produk():
    if request.method == 'POST':
        nama = request.form.get('nama')
        kategori = request.form.get('kategori')
        harga = request.form.get('harga')
        stok = request.form.get('stok')
        
        # Ambil file foto dari komputer
        file = request.files.get('gambar')
        gambar_path = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500" # Gambar default jika tidak ada file
        
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            gambar_path = url_for('static', filename=f'uploads/{filename}')

        new_id = len(data_sepatu) + 1
        data_sepatu.append({
            "id": new_id,
            "nama": nama,
            "kategori": kategori,
            "harga": harga,
            "stok": int(stok) if stok else 0,
            "gambar": gambar_path
        })
        
        return redirect(url_for('produk'))
        
    return render_template('tambah_produk.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

if __name__ == '__main__':
    app.run(debug=True)
