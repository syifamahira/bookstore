link deploy app : https://syifa-bookstore.adaptable.app
syifa bookstore menyediakan katalog berisi buku-buku yang dapat dibeli di syifa bookstore.

1. Saya mengerjakan checklist tugas 2 melalui tahapan berikut:
- Pertama saya membuat repo baru di github berjudul bookstore, lalu saya juga membuat direktori baru di laptop saya dan menginisiasi git agar terhubung dengan repo github
- Saya membuat virtual environment di direktori bookstore dan mengaktifkan env
- Saya meng-install django dan modul lain dengan menambahkan berkas requreiments.txt di direktori
-  membuat proyek django dengan nama sama seperti direktori saya yaitu bookstore
-  Saya menambahkan berkas .gitignore di direktori bookstore
-  Saya membuat aplikasi baru bernama main didalam proyek bookstore di direktori bookstore, setelah itu saya mendaftarkan aplikasi main di berkas settings.py dengan menambahkan 'main' ke variabel INSTALLED_APPS
-  Saya membuat class Book di berkas models.py yang terdiri dari title(name) (CharField), author(CharField), genre(CharField), price(IntegerField), amount(IntegerField), dan synopsis(TextField)
-  Saya melakuan migrasi model untuk mengubah struktur basis data sesuai model yang saya buat
-  Saya membuat templates yang berisi main.html sebagai design tampilan website yang ingin saya buat
-  Saya membuat fungsi show_main di berkas views.py untuk memasukkan value sesuai model Book yang sudah dibuat tadi, dan memakai fungsi render juga untuk me-render tampilan HTML
-  Saya meng-config routing url aplikasi main di berkas urls.py pada direktori proyek bookstore 

2. ![baganpbp](https://github.com/syifamahira/bookstore/assets/80321089/1a52cf45-900b-44f0-b12b-646e8c5019d1)
     Alurnya pertama request oleh user akan diproses melalui urls yang akan memilih view yang telah didefisinikan oleh developer di views.py. views akan memamnggil query ke models jika membutuhkan keterlibatan database dan query nya akan dikembalikan lagi hasilnya ke views. Kemudian setelah request selesai diproses, hasil prosesnya akan dipetakan ke berkas html yang sesuai di dalam template, dan terakhir request akan ditampilkan dalam bentuk halaman web ke user.

3. Dengan menggunakan Virtual Environment, kita memastikan bahwa setiap proyek terisolasi dari satu sama lain sehingga memungkinkan kita untuk bekerja di berbagai proyek tanpa menganggu yang lainnya. Selain itu, pemeliharaan proyek dapat menjadi lebih mudah dan lebih aman.
Bisa saja kita membuat aplikasi Django tanpa Virtual Environment, namun hal tersebut dapat menimbulkan risiko yang tidak diinginkan. Tanpa Virtual Environment, proyek-proyek berbagi ketergantungan yang sama, sehingga dapat menyebabkan konflik yang kemudian akan membuat rentan dan kacau proyek.

4.
- MVC memisahkan aplikasi menjadi tiga komponen utama: Model (data dan logika), View (tampilan), dan Controller (pengendali). Model mengelola data, View mengatur tampilan, dan Controller mengatur interaksi pengguna.
- MVT adalah varian dari MVC yang digunakan dalam kerangka kerja Django. MVT memiliki Model (data), View (tampilan), dan Template (pola tampilan). Model mengelola data, View mengontrol logika tampilan, dan Template mengatur tampilan HTML.
- MVVM adalah pola desain yang digunakan terutama dalam pengembangan aplikasi berbasis antarmuka pengguna (UI). Ini memisahkan aplikasi menjadi Model (data), View (tampilan), dan View Model (penghubung antara Model dan View). View Model memungkinkan binding dua arah antara Model dan View.

Perbedaannya terletak pada detail implementasi dan fokus penggunaan masing-masing pola, namun ketiganya bertujuan untuk memisahkan logika bisnis dari tampilan dalam pengembangan aplikasi.
