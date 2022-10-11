#include <iostream>
#include <ostream>
using namespace std;
int main(){
    string a = "Hello World";
    string* ab = &a;
    string &c = a;
    cout << a << endl;
    cout << ab<< endl;
    cout << c;
    cout << "\n";
    return 0;
}