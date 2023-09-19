# Syifa Bookstore
> Syifa Bookstore adalah website yang berisi katalog buku tersedia. Terdapat informasi terkait buku seperti judul, penulis, genre, harga dan lain-lain.

### Perbedaan POST dan GET
Form **POST** digunakan untuk mengirim data ke server dengan cara yang tidak terlihat oleh pengguna. Data ini umumnya digunakan untuk mengirim data sensitif seperti kata sandi dan tidak muncul di URL. Form POST digunakan dalam tindakan yang mengubah data di server, seperti membuat, memperbarui, atau menghapus data.

Form **GET** mengirim data ke server sebagai bagian dari URL. Data yang dikirim melalui form GET akan terlihat di URL, sehingga dapat dibaca oleh siapa saja yang melihatnya. Form GET digunakan untuk mengambil data dari server tanpa mengubahnya, seperti saat melakukan pencarian atau filtrasi data.

### Perbedaan XML, JSON, HTML 
1. XML :
- Digunakan untuk menggambarkan dan menyimpan data dalam bentuk hierarki.
- Tidak memiliki struktur tetap dan dapat disesuaikan dengan kebutuhan.
- Cocok untuk pertukaran data antara aplikasi yang berbeda dan memiliki dukungan yang baik untuk metadata.
- Lebih berat dalam hal ukuran file dan kompleksitas dibandingkan dengan JSON dan HTML.

2. JSON :
- Digunakan untuk menyimpan dan mengirim data dalam format ringkas dan mudah dibaca oleh manusia.
- Terutama digunakan dalam pengembangan aplikasi web dan RESTful APIs.
- Lebih ringan dibandingkan dengan XML dan lebih mudah diproses oleh JavaScript.
- Terbatas dalam dukungan terhadap metadata dibandingkan dengan XML.

3. HTML:
- Digunakan untuk membuat struktur dan konten halaman web.
- Tidak dirancang untuk pertukaran data atau representasi data yang kaya, tetapi lebih untuk menampilkan informasi dalam bentuk halaman web yang dapat diakses oleh pengguna.
- Menggunakan markup untuk menampilkan konten, seperti teks, gambar, tautan, dan elemen-elemen lainnya.
- Terutama digunakan untuk tujuan presentasi dan interaksi pengguna dengan aplikasi web.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena format yang ringkas, mudah dipahami oleh manusia, dan kompatibel dengan banyak bahasa pemrograman serta platform.

### _Step-by-step_ pengerjaan
1. Pertama saya membuat berkas base.html sebagai template untuk tampilan html lain di proyek saya
2. Saya mendaftarkan template di settings.py milik bookstore di proyek bookstore saya
3. Saya memodifikasi berkas main.html agar sesuai dengan skeleton base.html
4. Saya membuat form baru untuk menerima data produk baru dengan nama forms.py
5. Saya membuat fungsi create_product di views.py pada main untuk menambahkan data produk setelah di submit, setelah itu saya meng-import fungsi dan menambahkan path url nya
6. Saya membuat berkas create_product.html untuk mendapatkan produk
7. Saya memodifikasi kode di main.html agar data produk yang diterima ditampilkan dalam bentuk table, dan menambahkan tombol add product yang terhubung ke form
8. Saya membuat fungsi show_xml, show_json, show_xml_by_id dan show_json_by_id. Hasilnya berisi parameter data hasil query
9. Saya meng=import fungsi yang sudah dibuat tadi dan menambahkan path url nya
10. Selesai, run servernya di main,json,xml,json_by_id atau xml_by_id

### Postman
