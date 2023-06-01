#include <iostream>
using namespace std;

int N, solution[100000];

int abs(int a){
    if (a >= 0) return a;
    else return -a;

}

int main () {
    scanf("%d", &N);
    int lend = 0, rend = N - 1, min = 2000000000, sum, ansL = 0, ansR = N - 1;

    for (int i = 0; i < N; i++) {
        scanf("%d", &solution[i]);
    }

    while (lend < rend && lend != rend){
        sum = solution[lend] + solution[rend];
        if (sum < 0) {
            if (abs(sum) < min) {
                min = abs(sum);
                ansL = lend;
                ansR = rend;
            }
            lend++;
        }
        else {
            if (abs(sum) < min){
                min = abs(sum);
                ansL = lend;
                ansR = rend;
            }
            rend--;
        }
    }
    printf("%d %d", solution[ansL], solution[ansR]);

}
