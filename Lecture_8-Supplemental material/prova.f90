Program prova
Implicit none
integer(kind=4) :: n, i, j
real(kind=8) :: s
print*,"immetti n"
read (*,*) n
s = 0.
do i=0,n-1
do j=0,n-1
s = s + sin(dble(i)*dble(j))
end do
enddo
write(*,"('s = ',f20.3)") s
end program prova
