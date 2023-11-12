from mpi4py import MPI
import time

start = time.time()

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Ambil input dari pengguna
        input_str = input("Masukkan data, dipisahkan dengan spasi: ")
        data = list(map(int, input_str.split()))
    else:
        data = None

    # Broadcast data dari proses 0 ke semua proses
    data = comm.bcast(data, root=0)

    chunk_size = len(data) // size
    start = rank * chunk_size
    end = (rank + 1) * chunk_size

    if rank == size - 1:
        end = len(data)

    local_sum = sum(data[start:end])

    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        print("Total hasil perhitungan:", total_sum)

if _name_ == '_main_':
    main()
end = time.time()
print("waktu dikerjakan", end - start)
