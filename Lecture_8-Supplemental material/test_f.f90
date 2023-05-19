! test_f.f90
subroutine moltiplica( a, b, c, m, n )
  
  integer(kind=4)   :: m, n
  real(kind=8)  :: a(m,n), b(m,n)
  real(kind=8)  :: c(m, n)

!f2py intent(in) a
!f2py intent(in) b
!f2py intent(out) c

  integer(kind=4) :: i,j

  do j=1,n
    do i=1,m
      c(i,j) = a(i,j) * b(i,j)
    end do
  end do

end subroutine
