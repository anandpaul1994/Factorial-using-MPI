from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = 15
if rank != 0 and rank != size-1:
        fact=1
        for i in range((rank*a)/size,((rank+1)*a)/size):
                fact=fact*i
        comm.send(fact, dest=0, tag=11)
elif rank == size-1:
        fact=1
        for i in range(a*rank/size,a+1):
                fact=fact*i
        comm.send(fact,dest=0,tag=11)

elif rank == 0:
        fact=1
        for i in range(1,(a/size)):
                fact=fact*i
        for i in range(1,size):
                data = comm.recv(source=i,tag=11)
                fact=fact*data
        print fact



