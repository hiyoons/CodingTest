#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    string str;
    int B;
    int result = 0;
    int a = 0;
    cin >> str >> B;

    for (int i = 0; i < str.length(); i++)
    {
        char in = str[str.length() - 1 - i];
        if ('0' <= in && in <= '9')
        {
            result += (in - '0') * pow(B, i);
        }
        else
        {
            result += (in - 'A' + 10) * pow(B, i);
        }
    }

    cout << result;
    return 0;
}