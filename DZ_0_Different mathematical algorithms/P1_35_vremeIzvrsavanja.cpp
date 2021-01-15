#include <stdio.h>
#include <time.h>

double F(double a, double b){
	return a + b;
}

int main(void){
	double x, eval;
	double max = 7e9;
	
	time_t t1, t2;
	time(&t1);
	
	for(x = 0; x < max; x = x + 1.0)
		eval = F(x, x);
	
	time(&t2);
	
	printf("%5.5e\n", (t2 - t1)/max);
	
	return 0;
}