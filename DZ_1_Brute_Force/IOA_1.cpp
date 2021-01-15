#include <iostream>
#include <math.h>
#include <time.h>
/**
* Posto se zelimo da zaokruzimo sve na cele brojeve, potrebno je pomnoziti svaki mnozilac sa 100.
* Inicijalno:   a * b * c * d = 7.11
* Trenutno: (100 * a) * (100 * b) * (100 * c) * (100 * d) = 7.11 * 100^4
* 
* Logaritmujemo jer kasnije koristimo logaritme za racunanje proizvoda
* 
**/
const double log_max = log(711000000);
const int max = 711;
const int step = 1;

bool f(int a, int b, int c, int d) {

    /**
    * Logaritmujemo mnozenje jer mnozenjem celih brojeva mozemo, u ovom slucaju, da predjemo MAX_INT. Logaritmovanjem smanjujemo tu mogucnost.
    * Podeljeno je na log(a * b) + log(c * d) jer da smo sve stavili pod isti log, i dalje moze da dodje do overflow-a
    */
    if (a + b + c + d == max && log(a * b) + log(c * d) == log_max) {
        return true;
    }
    return false;
}

int main() {
    /*
    *   Ideja resenja je:
    *   Ako imamo a + b + c + d = 711, zelimo da izbegnemo 4x for petlji u rasponu od 1 do 711, kompleksnost je onda 711^4.
    *   
    *   Zeleo sam da svakom pojedinacnom clanu dodelim odredjeni opseg za koji je zaduzen. To sam uradio tako sto 711 podelim sa 4
    *   i dobije se 177.75, zaokruzivanjem na 178 sam uzeo da oduzimam od 711 do 177. Tako garantujemo da ce uvek postojati bar jedna
    *   suma koja dovodi do 711. --- Makar meni ovo ima smisla... ---
    * 
    * 
    *   Step break je flag koji nam "hard break"-uje ove tri unutrasnje petlje. Zelimo da nadjemo jedinstvene kombinacije brojeva.
    * 
    *   Npr:
    *   
    *   1, 3, 4, 5 je za nas isto sto i ->
    *   1, 4, 3, 5 isto sto i ->
    *   1, 5, 3, 4 itd...
    * 
    *   Jos jedna optimizacija bi se dodala tako sto se stavi provera za "i" petlju da li trenutna vrednost i postoji u skupu odradjenih brojeva.
    *   Ako postoji, onda je najverovatnije obradjen taj slucaj. U opstem slucaju ovo ne bi radilo, potrebno je modifikovati dodavanje u skup.
    *   Receno je da se ocekuje jedinstveno resenje.
    * 
    *   Ovo moze da radi samo u slucaju da je spoljasnja petlja 177, a najunutrasnjija 711.
    * 
    */
    bool step_break = false;
    bool firstResult = false;
    time_t beginTime, endTime, firstResultTime;
    std::cout << "Begin execution..." << std::endl;
    unsigned long counter = 0;
    time(&beginTime);
    for (int i = 1; i < 177; i++)
    {

        for (int j = 1; j < 355 && step_break == false; j++)
        {
            for (int z = 1; z < 533 && step_break == false; z++)
            {
                for (int t = 1; t < 708 && step_break == false; t++)
                {
                    counter++;
                    if ( f(i, j, z, t) ) {
                        if (firstResult == false)
                        {
                            firstResult = true;
                            time(&firstResultTime);
                        }
                        std::cout << "Working combination: \t" << ((float)i)/100 << "," << ((float)j) / 100 << "," << ((float)z) / 100 << "," << ((float)t) / 100 << std::endl << "Each permutation of the given result is acceptable." << std::endl;
                        step_break = true;
                    }
                }
              
            }
           
        }
        step_break = false;
    }
    time(&endTime);

    std::cout << std::endl << "===========================\n" << "Execution time: \t" << difftime(endTime, beginTime) << " seconds" << std::endl << "First result time: \t" << difftime(firstResultTime, beginTime) << " seconds" << "\n===========================" << std::endl;
    std::cout << std::endl << "This project's maximum number of calls for optimization function is:"
        << std::endl << counter << std::endl
        << "Theorethical maximum (without any optimization is 711 ^ 4)" << std::endl;
    std::cout << std::endl << "END" << std::endl;
}
