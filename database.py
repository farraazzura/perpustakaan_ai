import sqlite3

def saveSurvey(no_buku, nama_buku, tanggal_terima, genre, role, image):
    conn = sqlite3.connect('survey.sqlite3')
    conn.execute('''
CREATE TABLE buku (
    no_buku INT AUTO_INCREMENT PRIMARY KEY,
    nama_buku VARCHAR(255) NOT NULL,
    tanggal_terima DATE NOT NULL,
    genre VARCHAR(255) NOT NULL,
    role VARCHAR(100),
    image VARCHAR(255) NOT NULL
);
    ''')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (no_buku, nama_buku, tanggal_terima, genre, role, image)
        VALUES (?, ?, ?, ?, ?)
    ''', (no_buku, nama_buku, tanggal_terima, genre, role, image))
    conn.commit()
    conn.close()
