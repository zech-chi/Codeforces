#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int get_diff(string s)
{
	if (s.empty()) {
		return (-1);
	}
	for (int i = 1; i < s.length(); i++) {
		if (s[i] != s[0]) {
			return (i);
		}
	}
	return (-1);
}

int	main()
{
	int	t;
	string s;
	int	d;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s;
		d = get_diff(s);
		if (d == -1) {
			cout << "NO" << endl;
		} else {
			cout << "YES" << endl;
			swap(s[0], s[d]);
			cout << s << endl;
		}
	}
}