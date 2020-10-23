#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for(int i=0;i<numbers.size();i++){
        for(int j=i+1;j<numbers.size();j++){
            int tmp = numbers[i] + numbers[j];
            int flag = 1;
            for(int k=0;k<answer.size();k++){
                if (answer[k] == tmp){
                    flag = 0;
                    break;
                }
            }
            if(flag == 0){
                continue;
            }
            answer.push_back(numbers[i]+numbers[j]);
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}