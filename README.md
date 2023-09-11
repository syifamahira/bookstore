1. Saya mengerjakan checklist tugas 2 melalui tahapan berikut:
- Pertama saya membuat repo baru di github berjudul bookstore, lalu saya juga membuat direktori baru di laptop saya dan menginisiasi git agar terhubung dengan repo github
-Saya membuat virtual environment di direktori bookstore dan mengaktifkan env 
-Saya meng-install django dan modul lain dengan menambahkan berkas requreiments.txt di direktori
-Saya membuat proyek django dengan nama sama seperti direktori saya yaitu bookstore
-Saya menambahkan berkas .gitignore di direktori bookstore
-Saya membuat aplikasi baru bernama main didalam proyek bookstore di direktori bookstore, setelah itu saya mendaftarkan aplikasi main di berkas settings.py dengan menambahkan 'main' ke variabel INSTALLED_APPS
-Saya membuat class Book di berkas models.py yang terdiri dari title(name) (CharField), author(CharField), genre(CharField), price(IntegerField), amount(IntegerField), dan synopsis(TextField)
-Saya melakuan migrasi model untuk mengubah struktur basis data sesuai model yang saya buat
-Saya membuat templates yang berisi main.html sebagai design tampilan website yang ingin saya buat
-Saya membuat fungsi show_main di berkas views.py untuk memasukkan value sesuai model Book yang sudah dibuat tadi, dan memakai fungsi render juga untuk me-render tampilan HTML
-Saya meng-config routing url aplikasi main di berkas urls.py pada direktori proyek bookstore 

2. 