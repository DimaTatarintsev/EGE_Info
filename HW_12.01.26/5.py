for N in range(10000,100000):
    A=list(map(int, str(N)))
    S=sum(A)
    M=max(A)+min(A)
    L=A[0]
    R=A[-1]
    P1=S-L
    P2=M-R
    Z=int(str(P1)+str(P2))
    if Z==222:
        print(N)
