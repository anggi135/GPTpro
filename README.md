# GPTpro
Pro GPT chat for user
File py

Kode yang diberikan adalah sebuah program Python yang memanfaatkan beberapa API untuk mengambil informasi dari sebuah RSS feed dan kemudian memposting artikel ke sebuah blog di Blogspot.

Program ini diawali dengan mengimpor tiga modul Python yaitu feedparser, openai, dan os. Modul feedparser digunakan untuk mengambil informasi dari sebuah RSS feed, openai digunakan untuk membangkitkan teks secara otomatis, dan os digunakan untuk mengatur kunci API OpenAI.

Setelah itu, program menentukan URL RSS feed yang akan diambil datanya dengan menetapkan nilai pada variabel rss_url. Kemudian, program mengambil data RSS dengan menggunakan modul feedparser.

Program selanjutnya akan melakukan ekstraksi informasi dari setiap posting pada RSS feed menggunakan perulangan for. Informasi yang diekstraksi antara lain judul, link, deskripsi, URL gambar, dan kategori dari setiap posting.

Setelah itu, program mengatur kunci API OpenAI dengan menetapkan nilai pada variabel openai.api_key menggunakan nilai yang tersimpan pada environment variable OPENAI_API_KEY.

Program kemudian mendefinisikan sebuah fungsi generate_text(prompt) yang digunakan untuk membangkitkan teks secara otomatis dengan menggunakan API OpenAI. Fungsi ini akan menghasilkan teks dengan menggunakan mesin pembelajaran mesin yang disebut davinci dengan jumlah token maksimum 1024, jumlah hasil yang dihasilkan 1, stop words tidak diberikan, dan temperatur 0.5.

Selanjutnya, program menentukan path ke file credential untuk akun Google dengan menetapkan nilai pada variabel SERVICE_ACCOUNT_FILE dan menginisialisasi credential untuk mengakses Google API dengan menggunakan modul service_account.

Setelah itu, program menginisialisasi API Blogspot menggunakan credential yang telah disiapkan dengan memanggil fungsi build() dari modul googleapiclient.discovery. Program kemudian mendefinisikan sebuah fungsi create_post(blog_id, title, content) yang digunakan untuk memposting artikel ke Blogspot. Fungsi ini akan membuat sebuah request untuk mengambil informasi blog, mengambil URL dari blog tersebut, mengubah HTML ke teks biasa, dan membuat post request untuk memposting artikel ke Blogspot.

Program terakhir memanggil fungsi create_post dengan parameter yang sesuai yaitu ID blogspot, judul artikel, dan konten artikel.

Dengan menggunakan program ini, pengguna dapat dengan mudah mengambil informasi dari sebuah RSS feed dan memposting artikel ke Blogspot secara otomatis dengan memanfaatkan API OpenAI dan Google.


#auto with cronjob

Untuk menjalankan kode tersebut secara otomatis menggunakan Cron Job, berikut adalah langkah-langkahnya:

1. Buka terminal pada sistem operasi Anda.
2. Jalankan perintah `crontab -e` untuk membuka file konfigurasi Cron Job.
3. Tambahkan baris berikut pada akhir file konfigurasi tersebut:

   ```
   * * * * * python /auto.py
   ```

   Keterangan:
   
   - Tanda `*` pada setiap kolom menunjukkan bahwa perintah akan dijalankan setiap menit, setiap jam, setiap hari, setiap bulan, dan setiap hari dalam seminggu.
   - Ganti `/auto.py` dengan path ke file script Anda yang akan dijalankan. Pastikan path-nya benar dan script tersebut dapat dijalankan menggunakan Python.
   
4. Simpan file konfigurasi Cron Job dengan menekan tombol `Ctrl + X`, lalu tekan tombol `Y` untuk menyimpan perubahan, dan tekan `Enter`.
5. Cron Job sekarang akan dijalankan setiap menit untuk menjalankan script tersebut secara otomatis.

Pastikan bahwa sistem operasi Anda sudah diatur dengan benar untuk menjalankan Cron Job. Jika Anda tidak yakin, Anda dapat menghubungi administrator sistem Anda untuk mendapatkan bantuan. Selain itu, pastikan juga bahwa lingkungan yang dibutuhkan oleh script telah diatur dengan benar pada saat menjalankan Cron Job.

### jangn lupa mengubah gen.py

Untuk menjalankan kode tersebut, Anda harus memastikan bahwa Python sudah terinstal pada komputer Anda, dan modul json sudah terpasang.

Anda juga perlu mengisi nilai variabel di dalam dictionary credentials dengan nilai yang sesuai. Terdapat beberapa nilai yang harus diisi yaitu:

- client_id: ID klien dari proyek Anda di Console Cloud Google.
- client_secret: Kunci rahasia dari proyek Anda di Console Cloud Google.
- refresh_token: Token akses segar yang diperoleh dari permintaan pertama yang diotorisasi oleh pengguna.
- user_agent: Nama aplikasi atau nama agen pengguna yang diinginkan.
- scopes: Daftar izin yang diminta oleh aplikasi.

Setelah Anda mengisi nilai variabel tersebut, Anda dapat menjalankan kode tersebut untuk membuat file JSON bernama "credential.json" dengan isi dictionary credentials. File JSON ini dapat digunakan untuk mengakses API Google, khususnya API Blogger.
