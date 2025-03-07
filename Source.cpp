#include <iostream>
#include <cmath>  // pentru pow()
using namespace std;

// Clasa Calculator
class Calculator {
public:
    // Metode pentru operații
    double adunare(double a, double b) { return a + b; }
    double scadere(double a, double b) { return a - b; }
    double inmultire(double a, double b) { return a * b; }
    double impartire(double a, double b) {
        if (b != 0) return a / b;
        cout << "Eroare: Impartire la zero!\n";
        return 0;
    }
    double putere(double a, double b) { return pow(a, b); }
};

int main() {
    Calculator calc;
    int optiune;
    double x, y;

    do {
        // Meniu
        cout << "\n=== Calculator Simplu ===\n";
        cout << "1. Adunare\n2. Scadere\n3. Inmultire\n4. Impartire\n5. Putere\n6. Iesire\n";
        cout << "Alege o optiune: ";
        cin >> optiune;

        if (optiune >= 1 && optiune <= 5) {
            cout << "Introdu primul numar: ";
            cin >> x;
            cout << "Introdu al doilea numar: ";
            cin >> y;
        }

        switch (optiune) {
        case 1: cout << "Rezultat: " << calc.adunare(x, y) << "\n"; break;
        case 2: cout << "Rezultat: " << calc.scadere(x, y) << "\n"; break;
        case 3: cout << "Rezultat: " << calc.inmultire(x, y) << "\n"; break;
        case 4: cout << "Rezultat: " << calc.impartire(x, y) << "\n"; break;
        case 5: cout << "Rezultat: " << calc.putere(x, y) << "\n"; break;
        case 6: cout << "Iesire...\n"; break;
        default: cout << "Optiune invalida!\n";
        }
    } while (optiune != 6);

    return 0;
}
