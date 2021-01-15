void driver_random_variation(void){
	srand((unsigned int)time(NULL));
	
	int n = 10;
	int k = 4;
	int s = 15;
	
	int* r = new int [k];
	
	for(int i = 0; i < s; i++){
		for(int j = 0; j < k; j++){
			r[j] = random_int(0, n - 1);
			printf("%2d ", r[j]);
		}
		printf("\n");
	}
	
	delete [] r;
}

void driver_random_vector(void){
	srand((unsigned int)time(NULL));
	
	double xmin = -1.0;
	double xmax = +1.0;
	int k = 4;
	int s = 15;
	
	double* r = new double [k];
	
	for(int i = 0; i < s; i++){
		for(int j = 0; j < k; j++){
			r[j] = random_float(xmin, xmax);
			printf("%2.3f ", r[j]);
		}
		printf("\n");
	}
	
	delete [] r;
	
}