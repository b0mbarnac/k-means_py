#include <iostream>

using namespace std;

int main()
{
   // setlocale(LC_ALL, "Russian");

    int m, d;
    cout << "Номер месяца: "; cin >> m;
    cout << "Число: ";        cin >> d;


    // проверки месяца, числа, кол-ва дней в месяце
    if (m > 12 || m < 0)
    {
        cout << "Неправильный номер месяца!" << endl; return -2;
    }

    if (d > 31 || d < 0)
    {
        cout << "Неверное число!" << endl; return -1;
    }

    if (d > 30 && (m == 4 || m == 6 || m == 9 || m == 11))
    {
        cout << "В этом месяце 30 дней!" << endl; return -1;
    }
    else if (m == 2 && d > 28)
    {
        cout << "В этом месяце 28 дней!" << endl; return -1;
    }


    // вычисление
    // прибавляем сумму всех дней предыдущих месяцев и в конце сумму дней данного месяца
    int D = 0;

    switch (m - 1)
    {
    case 11: D += 30;
    case 10: D += 31;
    case 9: D += 30;
    case 8: D += 31;
    case 7: D += 31;
    case 6: D += 30;
    case 5: D += 31;
    case 4: D += 30;
    case 3: D += 31;
    case 2: D += 28;
    case 1: D += 31;
    case 0: D += d; break;
    }

    cout << endl << "До НГ осталось: " << 365 - D << endl;
    cout << "Либо: " << 366 - D << " (если считать сколько осталось до 1 янв)" << endl << endl;

    return 0;
}