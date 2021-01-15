// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cmath>
#include <iomanip>
#include <thread>
long double J1_1, J1_2, J2_1, J2_2;

void calc(int n, int z, long double a_coo, long double b_coo) {
	long double current;
	long double prev_iter = -100;
	long double a = std::sph_bessel(n, a_coo);
	long double b = std::sph_bessel(n, b_coo);

	long double temp = (a_coo + b_coo) / 2;
	current = std::sph_bessel(n, temp);
	while (std::abs(current - prev_iter) * 10e13 >= 1) {
		if (a * current < 0) {
			b_coo = temp;
			b = std::sph_bessel(n, b_coo);
			prev_iter = current;
			temp = (a_coo + b_coo) / 2;
			current = std::sph_bessel(n, temp);
		}
		else if (b * current < 0) {
			a_coo = temp;
			a = std::sph_bessel(n, a_coo);
			prev_iter = current;
			temp = (a_coo + b_coo) / 2;
			current = std::sph_bessel(n, temp);
		}
	}
	switch (n) {
	case 1:
		switch (z) {
		case 1:
			J1_1 = temp;
			break;
		case 2:
			J1_2 = temp;
			break;
		}
		break;
	case 2:
		switch (z) {
		case 1:
			J2_1 = temp;
			break;
		case 2:
			J2_2 = temp;
			break;
		}
		break;
	}
	
}
int main()
{
	long double J1_1_a = 4;
	long double J1_1_b = 5;

	long double J1_2_a = 7.5;
	long double J1_2_b = 8;

	long double J2_1_a = 5.5;
	long double J2_1_b = 6;

	long double J2_2_a = 9;
	long double J2_2_b = 9.5;

	calc(1, 1, J1_1_a, J1_1_b);
	calc(1, 2, J1_2_a, J1_2_b);
	calc(2, 1, J2_1_a, J2_1_b);
	calc(2, 2, J2_2_a, J2_2_b);
	
	

	std::cout << "================================================================" << std::endl;
	std::cout << "Bessel order 1 zeros at:\n\t1st position:" << std::setprecision(13) << J1_1 << std::endl;
	std::cout << "\t2nd position:" << std::setprecision(13) << J1_2 << std::endl;
	std::cout << "----------------------------------------------------------------" << std::endl;
	std::cout << "Bessel order 2 zeros at:\n\t1st position:"<< std::setprecision(13) << J2_1 << std::endl;
	std::cout << "\t2nd position:" << std::setprecision(13) << J2_2 << std::endl;
	std::cout << "================================================================" << std::endl;
	
}