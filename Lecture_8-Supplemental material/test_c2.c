/* test_c2.c */
void somma(int M, int N, double a[M][N], double b[M][N], double c[M][N]) {

    int i, j;
    

    for (i=0; i<M; i++){
        for (j=0;j<N;j++){
            c[i][j] = a[i][j] + b[i][j];
        }
    }

}

/* gcc  -shared -o test_c2.so test_c2.c */




