double random_float(double a, double b){
	double res;
	res = a + (double)rand() / (double)(RAND_MAX / (b - a));
	return res;
}
