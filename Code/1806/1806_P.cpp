#include <iostream>
using namespace std;


int main() {
	int N, S, nums[100000], start, end, ans, sum, a, b;
	scanf("%d%d", &N, &S);
	for (int i = 0; i < N; i++) scanf("%d", &nums[i]);
	
	start = end = 0, ans = N+1, sum = nums[0];

	while (start <= end && end < N) {
		if (sum < S) {
			sum += nums[++end];
		}
		else if (sum >= S) {
			if (end - start + 1 < ans) {
				ans = end - start + 1;
				a = start;
				b = end;
			}
			sum -= nums[start];
			start++;
		}
	}

	if (ans > N) printf("0");
	else printf("%d", ans);


}
