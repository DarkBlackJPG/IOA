int random_int(int a, int b){
	int res;
	res = a + rand() % (b + 1 - a);
	return res;
}
