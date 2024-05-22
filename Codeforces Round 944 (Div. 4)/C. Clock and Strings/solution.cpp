#include <iostream>
#include <algorithm>
using namespace std;

bool	is_up(int a, int b, int x)
{
	int	mx;
	int	mn;

	mx = max(a, b);
	mn = min(a, b);

	if ((1 <= x && x <= mn) || (mx <= x && x <= 12)) {
		return (true);
	}
	return (false);
}

int	main()
{
	int		t, a, b, c, d;
	bool	c_is_up;
	bool 	d_is_up;

	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> a >> b >> c >> d;
		c_is_up = is_up(a, b, c);
		d_is_up = is_up(a, b, d);
		if (c_is_up == d_is_up) {
			cout << "NO" << endl;
		} else {
			cout << "YES" << endl;
		}
	}
}
