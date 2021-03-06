int next_permutation(const int N, int *P) {
	int s;
	int *first = &P[0];
	int *last = &P[N - 1];
	int *k = last - 1;
	int *l = last;
	//find larges k so that P[k]<P[k+1]
	while (k > first) {
		if (*k < *(k + 1)) {
			break;
		}
		k--;
	}
	//if no P[k]<P[k+1], P is the last permutation in lexicographic order
	if (*k > *(k + 1)) {
		return 0;
	}
	//find largest l so that P[k]<P[l]
	while (l > k) {
		if (*l > *k) {
			break;
		}
		l--;
	}
	//swap P[l] and P[k]
	s = *k;
	*k = *l;
	*l = s;
	//reverse the remaining P[k+1]...P[N-1]
	first = k + 1;
	while (first < last) {
		s = *first;
		*first = *last;
		*last = s;

		first++;
		last--;
	}

	return 1;
}


void main(void){
	int N = 5;
	int *P = new int [N];
	
	//intitialize the first permutation
	for(int i = 0; i < N; i++)
		P[i] = i + 1;
	
	do{
		for(int i = 0; i < N; i++)
			printf("%2d ", P[i]);
		printf("\n");
	}while(next_permutation(N, P));
	
	delete [] P;
}