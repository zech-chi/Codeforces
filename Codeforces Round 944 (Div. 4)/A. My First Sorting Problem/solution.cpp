#include <iostream>
using namespace std;

int main()
{
	int t, a, b;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> a >> b;
		cout << min(a, b) << " " << max(a, b) << endl;
	}
}