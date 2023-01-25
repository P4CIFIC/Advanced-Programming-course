#include <stdio.h>
#include <map.h>
#include <iostream.h>

using namespace std;
map<string, int> R2N;
map<int, string> N2R;
string NtoR(int num) {
    const string ch[] = {"M", "CM", "D", "CD", "C", "XC", "L",
                "XL", "X", "IX", "V", "IV", "I"};
    const int val[] = {1000, 900, 500, 400, 100, 90, 50,
                40, 10, 9, 5, 4, 1};
    string ans = "";
    for(int i = 0; i < 13; i++) {
        while(num >= val[i]) {
            num -= val[i];
            ans += ch[i];
        }
    }
    return ans;
}
int main() {
    int i;
    string tmp;
    for(i = 1; i <= 100; i++) {
        tmp = NtoR(i);
        N2R[i] = tmp;
        R2N[tmp] = i;
    }
    while(cin >> tmp) {
        if(tmp == "#")  break;
        int pos1 = tmp.find('+'), pos2 = tmp.find('=');
        string a = tmp.substr(0, pos1);
        string b = tmp.substr(pos1+1, pos2-pos1-1);
        string c = tmp.substr(pos2+1);
        if(N2R[R2N[a]+R2N[b]] == c)
            cout << "Correct ambiguous" << endl;
        cout << a <<" "<< b <<" "<< c << endl;
    }
    return 0;
}

#include <iostream>
#include <map>
using namespace std;

map<char, int> values = { {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000} };

int getValue(string s) {
    int res = 0;
    for (int i = 0; i < s.size(); i++) {
        int val = values[s[i]];
        if (i + 1 < s.size() && values[s[i + 1]] > val) {
            res += values[s[i + 1]] - val;
            i++;
        }
        else {
            res += val;
        }
    }
    return res;
}

bool checkValid(string s) {
    int cnt = 1;
    char prev = s[0];
    for (int i = 1; i < s.size(); i++) {
        if (s[i] == prev) {
            cnt++;
            if (cnt > 3) return false;
        }
        else {
            cnt = 1;
            prev = s[i];
        }
    }
    return true;
}

int main() {
    string s;
    while (cin >> s) {
        if (s == "#") break;
        int pos1 = s.find('+'), pos2 = s.find('=');
        string a = s.substr(0, pos1);
        string b = s.substr(pos1 + 1, pos2 - pos1 - 1);
        string c = s.substr(pos2 + 1);

        if (!checkValid(a) || !checkValid(b) || !checkValid(c)) {
            cout << "Incorrect impossible" << endl;
            continue;
        }

        int num1 = getValue(a);
        int num2 = getValue(b);
        int sum = num1 + num2;
        if (getValue(c) == sum) {
           
