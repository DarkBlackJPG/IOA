void random_combination (int n, int k, int* P){
	if(k > n)
		return;
	
	int i, j, r, c;
	int* Q = new int[n];
	
	for(i = 0; i < n; i++)
		Q[i] = 0;
	
	for(i = 0; i < k; i++){
		r = random_int(0, n - 1 - i);
		c = 0;
		for (j = 0; j < n; j++){
			if(Q[j] == 0){
				if (r == c){
					Q[j]++;
					break;
				}
				c++;
			}
		}
	}
	
	c = 0;
	for(i = 0; i < n; i++){
		if(Q[i] == 1){
			P[c] = i + 1;
			c++;
		}
	}
	
	delete [] Q;
}

void driver_random_combination(void){
	int n = 5;
	int k = 3;
	
	int* P = new int [k];
	
	for(int i = 0; i < 100; i++){
		random_combination(n, k, P);
		for(int i = 0; i < k; i++){
			printf("2%d ", P[i]);
		}
		printf("\n");
	}
	
	delete [] P;
}