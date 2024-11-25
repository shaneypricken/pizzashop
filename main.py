//SHane Pricken
//Pizza shop lab
// 11/25
// extra: medium pizza, extra option, and sales tax

#include <iostream>
using namespace std;

void prices();
void welcome();

int main()
{
    int order, top;
    double total;
    welcome();
    prices();
    
    cout << "Which piuzz would you like to buzz? " << endl;
    cin >> order;
    switch (order){
        case 1: cout << "Large piuzz selected" << endl; total += 72.36; break;
        case 2: cout << "Medium piuzz selected" << endl; total += 56.19; break;
        case 3: cout << "Small piuzz selected" << endl; total += 41.64; break;
        case 4: cout << "Why did you select this if its coming soon dummy, +$100" << endl; total += 100; break;
        default: cout << "Not an option, +$100" << endl; total += 100; break;
    }
    
    cout << "How many toppings do you want ($172 each)" << endl;
    cin >> top;
    
    total += (top * 172);
    

    
    cout << "And heres the bill" << endl;
    cout << "Sub Total: $" << total << endl;
    cout << "Tax: 6.625%" << endl;
    cout << "Total: $" << (total * 1.06625) << endl;
    
}

void prices() {
    cout << "1. Large Piuzz: $72.36" << endl;
    cout << "2. Medium Piuzz: $56.19" << endl;
    cout << "3. Small Piuzz: $41.64" << endl;
    cout << "4. *coming soon*" << endl;
}

void welcome() {
    cout << "Welcuzz touzz chruzz's piuzz parluzz" << endl;
}
