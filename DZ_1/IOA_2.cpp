#include <iostream>
#include <math.h>
#include <time.h>
const unsigned long long max = 711;
const unsigned long long step = 1;

int f(int b, int c, int d) {
	int a = 711 - b - c - d;
	if (log(a * b) + log(c * d) == log(711000000))
	{
		return a;
	}
	else return -1;
}

/*
* Ideja za ovaj zadatak je slicna, ako ne i ista ideji za resavanje prethodnog zadatka.
*/
int main_() {
	bool step_break = false;
	bool firstResult = false;
	time_t beginTime, endTime, firstResultTime;
	std::cout << "Begin execution..." << std::endl;
	unsigned long counter = 0;
	time(&beginTime);
	for (int i = 1; i < 237; i++)
	{
		for (int j = 1; j < 474 && step_break == false; j++)
		{
			for (int z = 1; z < 708 && step_break == false; z++)
			{
				int a;
				counter++;
				if ( (a = f(i, j, z)) != -1) {
					if (firstResult == false)
					{
						firstResult = true;
						time(&firstResultTime);
					}
					std::cout << "Working combination: \t" << (float)a/100 << "," << (float)i/100 << "," << (float)j/100 << "," << (float)z/100 << std::endl << std::endl;
					step_break = true;
				}
			}
		}
		step_break = false;
	}
	time(&endTime);
	std::cout << std::endl << "===========================\n" << "Execution time: \t" << difftime(endTime, beginTime) << " seconds" << std::endl << "First result time: \t" << difftime(firstResultTime, beginTime) << " seconds" << "\n===========================" << std::endl;
	std::cout << std::endl << "This project's maximum number of calls for optimization function is:"
		<< std::endl << counter << std::endl
		<< "Theorethical maximum (without any optimization is 711 ^ 3)" << std::endl;
	std::cout << "END";
}