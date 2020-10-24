#include <iostream>
#include <sstream>
#include <string>

using namespace std;


string subcalc(string parent){
	string answer = "";
	string tmp = "";
	int num = 0;
	int mode = 0;
	char alpha = 'R';
	for(int i=0;i<parent.size();i++){
		if(parent[i]-48 >=0 && parent[i]-48 <10){
			mode = 1;
			if(num ==0){
				num = parent[i]-48;
			}
			else{
				num = num*10 + parent[i]-48;
			}
		}
		else if(parent[i] == '('){
			i++;
			while(1){
				if(parent[i] == ')'){
					i++;
					break;
				}
				tmp += parent[i];
				i++;
			}
			tmp = subcalc(tmp);
			if(mode ==1){
				for(int j=0;j<num;j++){
					answer += tmp;
				}
			}
			else if(mode ==2){
				
			}
		}
		else if(parent[i] == ')'){
			return answer;
		}
		else{
			mode =2;
			alpha = parent[i];
		}
	}
	return answer;
}

void solution(int numOfOrder, string *orderArr) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	
	for(int t=0;t<numOfOrder;t++){
		string answer = subcalc(orderArr[t]);
		cout << answer << endl;
	}

}

struct input_data {
  int numOfOrder;
  string *orderArr;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.numOfOrder;

  inputData.orderArr = new string[inputData.numOfOrder];
  for (int i = 0; i < inputData.numOfOrder; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    iss >> inputData.orderArr[i];
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.numOfOrder, inputData.orderArr);
  return 0;
}