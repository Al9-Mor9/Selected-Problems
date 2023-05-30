#include <string>
#include <vector>
#include <map>

using namespace std;

int RT = 0, CF = 1, JM = 2, AN = 3;
int score[4][2];
map<char, pair<int, int>> m;

string solution(vector<string> survey, vector<int> choices) {
	int len = survey.size();
	m.emplace('R', make_pair(0, 0));
	m.emplace('T', make_pair(0, 1));
	m.emplace('C', make_pair(1, 0));
	m.emplace('F', make_pair(1, 1));
	m.emplace('J', make_pair(2, 0));
	m.emplace('M', make_pair(2, 1));
	m.emplace('A', make_pair(3, 0));
	m.emplace('N', make_pair(3, 1));

	for (int i = 0; i < len; i++){
		int choice = 4 - choices[i];
		pair<int, int> target = m[survey[i][choice > 0 ? 0 : 1]];	

		score[target.first][target.second] += abs(choice);
	}

	string answer = "";
	answer += (score[0][0] >= score[0][1] ? 'R' : 'T'); 
	answer += (score[1][0] >= score[1][1] ? 'C' : 'F'); 
	answer += (score[2][0] >= score[2][1] ? 'J' : 'M'); 
	answer += (score[3][0] >= score[3][1] ? 'A' : 'N'); 
  
  return answer;
}
