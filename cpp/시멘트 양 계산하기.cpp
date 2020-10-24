#include <iostream>
#include <sstream>

using namespace std;

void solution(int day, int width, int **blocks) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	int sement = 0;
	int height[width] = {0,};
	
	for(int t=0;t<day;t++){
		for(int w=0;w<width;w++){
			height[w] += blocks[t][w];
		}
		for(int now=1;now<width-1;now++){
			for(int h=height[now]+1;h<10001;h++){
				int flag = 0;
				for(int check=now-1;check>-1;check--){
					if(height[check] >= h){
						flag++;
						break;
					}
				}
				for(int check=now+1;check<width;check++){
					if(height[check] >= h){
						flag++;
						break;
					}
				}
				if(flag ==2){
					sement++;
					height[now]++;
				}
				else{
					break;
				}
			}
		}
	}
	
	printf("%d\n", sement);

}

struct input_data {
  int day;
  int width;
  int **blocks;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.day;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.width;

  inputData.blocks = new int*[inputData.day];
  for (int i = 0; i < inputData.day; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    inputData.blocks[i] = new int[inputData.width];
    for (int j = 0; j < inputData.width; j++) {
      iss >> inputData.blocks[i][j];
    }
  }
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.day, inputData.width, inputData.blocks);
	return 0;
}