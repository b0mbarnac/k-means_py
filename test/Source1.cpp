#include <iostream>

using namespace std;

int main()
{
   // setlocale(LC_ALL, "Russian");

    int m, d;
    cout << "Íîìåð ìåñÿöà: "; cin >> m;
    cout << "×èñëî: ";        cin >> d;


    // ïðîâåðêè ìåñÿöà, ÷èñëà, êîë-âà äíåé â ìåñÿöå
    if (m > 12 || m < 0)
    {
        cout << "Íåïðàâèëüíûé íîìåð ìåñÿöà!" << endl; return -2;
    }

    if (d > 31 || d < 0)
    {
        cout << "Íåâåðíîå ÷èñëî!" << endl; return -1;
    }

    if (d > 30 && (m == 4 || m == 6 || m == 9 || m == 11))
    {
        cout << "Â ýòîì ìåñÿöå 30 äíåé!" << endl; return -1;
    }
    else if (m == 2 && d > 28)
    {
        cout << "Â ýòîì ìåñÿöå 28 äíåé!" << endl; return -1;
    }


    // âû÷èñëåíèå
    // ïðèáàâëÿåì ñóììó âñåõ äíåé ïðåäûäóùèõ ìåñÿöåâ è â êîíöå ñóììó äíåé äàííîãî ìåñÿöà
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

    cout << endl << "Äî ÍÃ îñòàëîñü: " << 365 - D << endl;
    cout << "Ëèáî: " << 366 - D << " (åñëè ñ÷èòàòü ñêîëüêî îñòàëîñü äî 1 ÿíâ)" << endl << endl;

    return 0;
}
