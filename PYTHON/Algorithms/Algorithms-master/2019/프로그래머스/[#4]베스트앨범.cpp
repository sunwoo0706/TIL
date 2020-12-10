#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    unordered_map<string, int> m;
    for(int i = 0; i < genres.size();i ++) {
        m[genres[i]] += plays[i];
    }

    vector<pair<int, string>> v;
    for(auto em : m) {
        v.push_back(pair<int, string>(em.second, em.first));
    }
    sort(v.begin(), v.end());

    for(auto it = v.begin(); it != v.end(); it++) {
        cout << it->second;
    }

    
    return answer;
}

int main() {
    vector<string> genres = {"classic", "pop", "classic", "classic", "pop"};
    vector<int> plays = {500, 600, 150, 800, 2500};
    solution(genres, plays);
    return 0;
}