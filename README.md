# Syifa Bookstore
> Syifa Bookstore adalah website yang berisi katalog buku tersedia. Terdapat informasi terkait buku seperti judul, penulis, genre, harga dan lain-lain.

### Apa itu UserCreationForm
Django UserCreationForm adalah salah satu formulir bawaan yang disediakan oleh Django untuk mempermudah proses pembuatan akun pengguna dalam aplikasi web. Form ini memungkinkan pengguna untuk mendaftar dengan menyediakan informasi seperti nama pengguna (username) dan kata sandi (password). 

Kelebihan:
- Mudah Digunakan: UserCreationForm menyediakan formulir siap pakai yang dapat dengan mudah diintegrasikan ke dalam aplikasi Django tanpa perlu menulis kode form kustom dari awal.
- Validasi Bawaan: Form ini dilengkapi dengan validasi bawaan, seperti pengecekan kesamaan kata sandi dan persyaratan panjang kata sandi, sehingga membantu mengurangi kesalahan saat pendaftaran.
- Integrasi dengan Django Authentication: Setelah pengguna terdaftar, Django Authentication sistem dapat digunakan dengan mudah untuk mengelola otentikasi dan otorisasi pengguna.
  
Kekurangan:
- Kustomisasi Terbatas: UserCreationForm memiliki tampilan dan validasi bawaan yang mungkin perlu disesuaikan sesuai dengan kebutuhan desain dan persyaratan aplikasi tertentu.
- Tidak Mengatasi Data Pengguna Tambahan: Form ini hanya mencakup informasi dasar seperti username dan password. Jika kita perlu mengumpulkan data tambahan dari pengguna saat pendaftaran, maka kita perlu menambahkan form tambahan atau mengkustomisasi form tersebut.

### Apa Perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi (Authentication): Autentikasi adalah proses memverifikasi identitas pengguna untuk memastikan bahwa mereka adalah mereka yang mengklaim diri mereka. Dalam konteks Django, autentikasi berkaitan dengan pengenalan pengguna berdasarkan informasi seperti username dan password. Django memiliki sistem autentikasi yang kuat yang memungkinkan pengguna untuk login dan mengidentifikasi diri mereka.

Otorisasi (Authorization): Otorisasi adalah proses mengendalikan akses pengguna yang telah diotentikasi ke sumber daya atau tindakan tertentu dalam aplikasi. Ini menentukan apa yang diizinkan atau tidak diizinkan pengguna lakukan setelah mereka login. Dalam konteks Django, otorisasi sering kali melibatkan pengaturan izin (permissions) yang mengontrol akses pengguna ke tampilan (views), model (database), atau bagian lain dari aplikasi.

Keduanya penting karena:
Autentikasi memastikan bahwa hanya pengguna yang sah yang memiliki akses ke aplikasi, sehingga melindungi data dan fungsi dari pengguna yang tidak sah.
Otorisasi memungkinkan pengelolaan tingkat akses pengguna, sehingga Anda dapat mengontrol siapa yang dapat melakukan tindakan tertentu dalam aplikasi Anda, mencegah penyalahgunaan dan memastikan bahwa pengguna hanya dapat melihat atau mengubah data yang sesuai dengan izin mereka.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah data kecil yang disimpan di perangkat pengguna oleh server web dan digunakan untuk melacak informasi terkait sesi dan preferensi pengguna. Dalam konteks aplikasi web, cookies sering digunakan untuk:

- Manajemen Sesi Pengguna: Cookies dapat digunakan untuk mengidentifikasi pengguna yang telah login dan mempertahankan sesi login mereka, sehingga pengguna tidak perlu login ulang setiap kali mengakses halaman baru.
  
Django menggunakan cookies untuk mengelola data sesi pengguna dengan cara sebagai berikut:

- Ketika pengguna pertama kali login, Django menyimpan informasi sesi pengguna, seperti ID sesi, di cookie di perangkat pengguna.
- Setiap kali pengguna mengirim permintaan ke server, cookie ini disertakan dalam permintaan HTTP, memungkinkan Django untuk mengidentifikasi sesi pengguna yang sesuai.
Django dapat menggunakan informasi sesi ini untuk menjaga status login pengguna, menyimpan preferensi, dan melacak data sesi lainnya.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web memiliki beberapa risiko potensial yang harus diwaspadai:
- Keamanan Data: Cookies biasanya disimpan di perangkat pengguna dalam bentuk teks yang dapat dibaca. Ini berarti jika informasi rahasia atau sensitif (seperti token otentikasi) disimpan dalam cookies tanpa enkripsi atau tindakan keamanan lainnya, informasi tersebut dapat rentan terhadap pencurian.
- Cross-Site Scripting (XSS): Serangan XSS dapat memanipulasi atau mencuri cookies pengguna jika tidak dilindungi dengan baik. Oleh karena itu, perlindungan terhadap XSS sangat penting.
- Cross-Site Request Forgery (CSRF): Cookies juga dapat digunakan oleh penyerang untuk melakukan serangan CSRF jika tidak ada tindakan pengamanan, seperti penggunaan token CSRF.

Dalam pengembangan web, penggunaan cookies harus dilakukan dengan hati-hati dan memperhatikan tindakan keamanan seperti enkripsi (HTTPS), pengaturan HttpOnly untuk cookies sensitif, dan perlindungan terhadap serangan XSS dan CSRF. Secara default, cookies tidak aman, tetapi dengan praktik keamanan yang tepat, mereka dapat digunakan secara aman dalam aplikasi web.

### _Step-by-step_ Pengerjaan
- Pertama saya meng-import redirect dan messages pada views.py
- Saya juga meng-import UserCreationForm untuk form otomatis dari Django
- Saya membuat fungsi di views.py yaitu fungsi register, login, logout, addproduct, decrementproduct, dan deleteproduct
- saya membuat berkas HTML baru yaitu login.html sebagai tampilan pertama saat load localhost karena loginpage dan berkas register.html dimana user akan di redirect untuk membuat akun
- saya meng-import fungsi yang sudah dibuat di urls.py dan menambahkan path url masing-masing di urlpatterns
- Kemudian saya merestriksi akses main agar hanya bisa diakses setelah user login dengan meng-import login-required di views.py
- Kemudian untuk penggunaan data cookies saya menambahkan cookie last_login di fungsi login dan memodifikasi fungsi show_main. Saya juga mengubah fungsi logout agar menghapus cookie saat user logout
- Saya menghubungkan setiap user dengan product yang berbeda tergantung user dengan memodifikasi model product dan mengimplementasikan perubahannya dengan migrations
- Saya mengubah fungsi create_product agar Django tidak langsung menyimpan objek langsung ke database. Saya juga mengubah nama di show_main sesuai dengan name user.
  





   



   
