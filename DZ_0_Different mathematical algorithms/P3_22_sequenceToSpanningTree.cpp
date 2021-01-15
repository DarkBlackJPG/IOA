void SequenceToSpanningTree(int* P, int len, int* T) {
	int i, j, q = 0; 
	int n = len + 2; 
	int* V = new int[n];

	for (i = 0; i < n; i++) {
		V[i] = 0;
	}

	for (i = 0; i < len; i++) {
		V[P[i] - 1] += 1; 
	}

	for (i = 0; i < len; i++) {
		for (j = 0; j < n; j++) {
			if (V[j] == 0) {
				V[j] = -1; 
				T[q++] = j + 1;
				T[q++] = P[i];
				V[P[i] - 1]--;
				break;
			}
		}
	}

	j = 0;
	for (i = 0; i < n; i++) {
		if (V[i] == 0 && j == 0) {
			T[q++] = i + 1;
			j++;
		}
		else if(V[i]==0 && j==1) {
			T[q++] = i + 1;
			break;
		}
	}

	delete[] V;
}