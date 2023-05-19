/* test_c.c */
double somma(int M, int N, double a[M][N], double b[M][N]) {

    int i, j;
    double s = 0.;
	
    for (i=0; i<M; i++){
        for (j=0;j<N;j++){
            s = s + a[i][j] * b[i][j];
        }
    }
    return s;
}
