#include <string>
#include <vector>
#include <algorithm>
#include <typeinfo> 
#include <functional>  
#include <unordered_map>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    
    unordered_map<string, int> m;
    for (auto elem : phone_book) { 
        m.insert(pair<string, int>(elem, elem.size()));
    }
    
     unordered_map<string, int>::iterator it;
     unordered_map<string, int>::iterator it2;
    for(it = m.begin(); it != m.end(); it++) {
        
        for(it2 = m.begin(); it2 != m.end(); it2++) {
            if(it->second > it2->second) {
                if((it->first).find(it2->first) == 0) {
                    return false;
                }
            }
            
        }
    }

    return answer;
}

int main() {
    vector<string> phone_book = {"119", "97674223", "1195524421"};
    
    cout << solution(phone_book) << endl;
    return 0;
}