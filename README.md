# Cara Install MPI pada Ubuntu Server dengan Python
Repositori ini akan membahas cara menginstal MPI dan menjalankan program Python numerik menggunakan Ubuntu Server 22.04 sebagai sistem operasi yang digunakan.

# Instalasi MPI di Ubuntu Server
## Topologi
![Gambar](https://github.com/feliana444/Eksekusi-Program-Buble-Sort-Python-Menggunakan-MPI/assets/145323449/f8d0a758-04d8-4092-b9a8-b7510e6e417a)

## 1. Langkah Pertama
1. Siapkan beberapa komputer dan tentukan satu komputer sebagai master dan beberapa komputer sebagai slave.
2. Pastikan semua komputer terhubung ke satu jaringan.
3. Perbarui dan Tingkatkan paket **sudo apt update && sudo apt upgrade**

## 2. Buat Pengguna Baru
Lakukan pada Master dan Slave
1. Buat Pengguna <br> **sudo adduser <nama user>**
2. Berikan Akses Root <br> **sudo usermod -aG mpiuser**
3. Masuk ke Pengguna Baru <br> **su - mpiuser**

## 3. Instalasi MPICH
Lakukan pada Master dan Slave
1. Instal MPICH Dan Semua Dokumentasi MPI <br> **sudo apt-get install -y mpich-doc mpich**
2. Periksa Versi MPI <br> **mpirun --version**
3. Uji Instalasi <br> **mpiexec -n <jumlah core> pyhton3 -m mpi4py.bench helloworld**
4. Instal paket python mpi4py dengan pip untuk menjalankan python pada MPI <br> **pip install mpi4py -U**

## 4. Konfigurasi Berkas /etc/hosts
**sudo nano /etc/hosts**
1. Master <br>
   ![Gambar1](https://github.com/feliana444/Eksekusi-Program-Buble-Sort-Python-Menggunakan-MPI/assets/145323449/4eebb045-9e2d-4c10-abc1-8cf37bb57704)
2. Slave <br>
   ![Gambar2](https://github.com/feliana444/Eksekusi-Program-Buble-Sort-Python-Menggunakan-MPI/assets/145323449/1b49e18a-57ec-4284-8dac-daf4ef5a97d6)

## 5. Instalasi SSH
Lakukan pada Master dan Slave <br>
**sudo apt install openssh-server**
1. Buat Kunci <br> Pada Master **ssh-keygen -t rsa**
2. Salin kunci publik ke klien <br> **ssh-copy-id <user>@<host>** <br>
   Ganti <user> dengan pengguna yang dibuat dan <host> dengan slave, lakukan pada semua slave.

## 6. Jalankan MPI
Lakukan pada master <br> **mpiexec -n <Jumlah Core> python -m mpi4py.bench helloworld**<br>
<img width="404" alt="percobaan" src="https://github.com/feliana444/Eksekusi-Program-Buble-Sort-Python-Menggunakan-MPI/assets/145323449/8e1d12c1-2d12-4016-afd9-341b1eea56e7">

# Cara Menjalankan Numeric MPI dengan MultiNode
## 1. Salin ID Master ke Semua Slave 
**ssh-copy-id user@hostname_or_ip**

## 2. Membuat Program Numeric Python 
Kode Numeric <br>
![Numeric](https://github.com/Alzidan21/MPI-Numeric/assets/105232288/8f2c0725-1389-4647-845c-f1440c16fbc8)

## 3. Salin Berkas Python ke Semua Slave
**~path$ scp /path/to/locate/bin * user@hostname_or_ip:path/to** <br>

## 4. Output
**Dengan Perintah**: **mpirun -n 4 -host danserver,slave,slave2,slave3 python3 numerik.py**
![Multi](https://github.com/Alzidan21/MPI-Numeric/assets/105232288/1cd294c7-0159-4d75-85d5-30f5ecff1500)
