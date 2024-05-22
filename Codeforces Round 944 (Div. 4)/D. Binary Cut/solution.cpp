#include <iostream>
#include <algorithm>
using namespace std;

int	get(string s)
{
	int	count;
	bool	got_it;

	if (s.empty())
		return (0);
	count = 1;
	got_it = false;
	for (int i = 1; i < s.length(); i++) {
		if (s[i] != s[i - 1]) {
			if (s[i] == '0') {
				count++;
			} else {
				if (got_it)
					count++;
				else
					got_it = !got_it;
			}
		}
	}
	return (count);
}

int	main()
{
	int	t;
	string	s;

	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> s;
		cout << get(s) << endl;
	}
}
