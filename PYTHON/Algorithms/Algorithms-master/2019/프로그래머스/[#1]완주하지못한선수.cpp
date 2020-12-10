#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string findNonCompletion(vector<string> completion, unordered_multimap<string, int> m ) {
    string answer = "";
    
    for(int i = 0; i < completion.size(); i++) {
        auto it = m.find(completion[i]);
        m.erase(it);
    }

    return m.begin()->first;
}

void chkValues(vector<string> participant, vector<string> completion) {
    if(participant.size() < 1 || participant.size() > 100000) {
        throw -1;
    } else if (participant.size() != completion.size() + 1){
        throw -2;
    } else {
        for(int i = 0; i < participant.size(); i++) {
            if(participant[i].size() < 1 || participant[i].size() > 20) {
                throw -3;
            }
        }
    }
}


string solution(vector<string> participant, vector<string> completion) {

   
    string answer = "";
    unordered_multimap<string, int> m;

    try {
        chkValues(participant, completion);

        vector<pair<string, int>> temp;
        for(int i = 0; i < participant.size(); i++) {
            temp.push_back(pair<string,int>(participant[i], i+1));
        }

    
        for(int i = 0; i < temp.size(); i++) {
            m.insert(temp[i]);
        }


        answer = findNonCompletion(completion, m);
    } catch(int e) {

        return "error : " + to_string(e);
    }
    return answer;
}


int main() {
    vector<string> participant = {"a", "b", "b"};
    vector<string> completion = {"a", "b"};

    cout << solution(participant, completion) << endl;
    
    return 0;
}