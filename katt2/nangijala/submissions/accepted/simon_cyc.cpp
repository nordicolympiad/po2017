#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int solvecyc(vector<vi>& ed) {
	int N = sz(ed);
	vi seen(N);
	int res = 0;
	rep(i,0,N) if (!seen[i]) {
		vi stack = {i};
		int vcount = 0, ecount = 0;
		while (!stack.empty()) {
			int x = stack.back();
			stack.pop_back();
			if (seen[x]++) continue;
			vcount++;
			trav(e, ed[x]) {
				ecount++;
				stack.push_back(e);
			}
		}
		assert(ecount % 2 == 0);
		ecount /= 2;

		if (ecount == vcount) {
			assert(vcount > 1);
			res += vcount / 2 + (vcount % 2 == 0 ? 0 : 2);
		}
		else {
			assert(vcount == ecount + 1);
			res += vcount / 2;
		}
	}
	return res;
}

int main() {
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int N, M;
	cin >> N >> M;
	vector<vi> ed(N);
	rep(i,0,M) {
		int a, b;
		cin >> a >> b;
		ed[a].push_back(b);
		ed[b].push_back(a);
	}

	cout << solvecyc(ed) << endl;

	exit(0);
}
