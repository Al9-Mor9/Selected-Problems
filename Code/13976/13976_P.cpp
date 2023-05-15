#include <iostream>
using namespace std;
#define ll long long
#define pll pair<ll, ll>
const long long MOD = 1000000007;

pair<pll, pll> precomputed[64]; 
pair<pll, pll> unit = {{4, -1}, {1, 0}};

pair<pll, pll> mat_prod(pair<pll, pll> mat1, pair<pll, pll> mat2){
	pair<pll, pll> ret;
	ret.first.first = ((mat1.first.first * mat2.first.first) % MOD + (mat1.first.second * mat2.second.first) % MOD + MOD) % MOD;
	ret.first.second= ((mat1.first.first * mat2.first.second) % MOD + (mat1.first.second * mat2.second.second) % MOD + MOD) % MOD;
	ret.second.first = ((mat1.second.first * mat2.first.first) % MOD + (mat1.second.second * mat2.second.first) % MOD + MOD) % MOD;
	ret.second.second= ((mat1.second.first * mat2.first.second) % MOD + (mat1.second.second * mat2.second.second) % MOD + MOD) % MOD;
	return ret;
}

pair<pll, pll> mat_pow(ll n){
	pair<pll, pll> ret = {{1, 0}, {0, 1}}; 
	for (int i = 0; i < 64; i++) {
		if ((1LL << i) & n) {
			ret = mat_prod(ret, precomputed[i]);
			//printf("(%lld %lld / %lld %lld)\n", ret.first.first, ret.first.second, ret.second.first, ret.second.second);
		}
	}
	return ret;
}

void precompute(){
	precomputed[0] = {{4, -1}, {1, 0}};
	for (int i = 1; i < 64; i++) {
		precomputed[i] = mat_prod(precomputed[i-1], precomputed[i-1]);
		//printf("%d : (%lld %lld / %lld %lld)\n", i, precomputed[i].first.first, precomputed[i].first.second, precomputed[i].second.first, precomputed[i].second.second);
	}
}

ll solve(ll N){
	if (N % 2) return 0;
	N = (N - 2) / 2;
	pair<pll, pll> tmp = mat_pow(N);

	return ((3 * tmp.first.first) % MOD + (tmp.first.second % MOD) + MOD) % MOD; 
}

int main(){
	long long N;
	scanf("%lld", &N);
	precompute();
	printf("%lld", solve(N));
}
