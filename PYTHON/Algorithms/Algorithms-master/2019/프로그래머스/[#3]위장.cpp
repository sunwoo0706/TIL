#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> m;
    for (auto em : clothes) {
        m[em[1]]++;
    }
    for(auto it = m.begin(); it != m.end(); it++) {
        answer *= (it->second+1);
    }
    answer --;
    return answer;
}

int main() {
    vector<vector<string>> clothes;
    clothes = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
    // clothes = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};
    cout << solution(clothes);
    return 0;
}