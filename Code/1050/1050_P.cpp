#include <iostream>
#include <string.h>
#include <vector>
#include <map>

#define INF 1000000001LL
using namespace std;

int N, M;
long long price;
string ingred, expr;
map<string,long long> cost;
map<string, vector<map<string, int>>> recipes;

void parse(string expr){
    string numStr, S, Sk;
    int idx1, idx2;
	long long num;
    map<string, int> detail;
    for (int i = 0; i <= expr.length(); i++){
        if (expr[i] == '='){
            S = expr.substr(0, i);
            idx1 = i;
        }
        else if (isdigit(expr[i])){
            idx2 = i;
        }
        else if (expr[i] == '+' || expr[i] == '\0'){
            numStr = expr.substr(idx1 + 1, idx2 - idx1);
            Sk = expr.substr(idx2 + 1, i - idx2 - 1);
            if (numStr.length() < 10) num = stoll(numStr);
            else if (numStr.length() == 10 && numStr[0] == '1' && stoll(numStr) == INF-1) num = INF -1;
            else num = INF;
            detail[Sk] += num;
            if (detail[Sk] >= INF) detail[Sk] = INF;
            idx1 = i;
        } 
    }
    recipes[S].push_back(detail);
}

int main(){
	ios::sync_with_stdio(false);
    cin >> N >> M;
    for (int i = 0; i < N; i++){
        cin >> ingred >> price;
		long long p = INF; 
		if (cost.find(ingred) != cost.end()) p = cost[ingred]; 
        cost.insert({ingred, min(p, price)});
    }
    for (int i = 0; i < M; i++){
        cin >> expr;
        parse(expr);
    }


	bool flag = true;
	while (flag) {
		flag = false;
		for (auto recipe : recipes){
			string target = recipe.first;
			for (auto ingredMap: recipe.second){
				long long sum = 0;
				for (auto detail : ingredMap){
					string name = detail.first;
					int count = detail.second;	
					if (cost.find(name) != cost.end()) {
						sum += cost[name] * count;	
						if (sum >= INF) sum = INF;
					}
					else {
						sum = 0;	
						break;
					}
				}
				if (sum && (cost.find(target) == cost.end() || cost[target] > sum)) {
					cost[target] = sum;
					flag = true;
				}
			}	
		}
	}

	if (cost.find("LOVE") == cost.end()) cout << -1 << endl;
	else cout << (cost["LOVE"] >= INF ? INF : cost["LOVE"]) << endl;
}
