#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

void solution(int sizeOfMatrix, int **matrix) {
  // TODO: 이곳에 코드를 작성하세요.
	vector<int> count;
	count.push_back(0);
	
	for(int i =0;i<sizeOfMatrix;i++){
		for(int j=0;j<sizeOfMatrix;j++){
			if(matrix[i][j]==1 && (i==0 || matrix[i-1][j]==0) && (j==0 || matrix[i][j-1]==0)){
				int bid = count.size();
				matrix[i][j] = bid;
				count.push_back(1);
			}
			else if(matrix[i][j]==1 && i!=0 && matrix[i-1][j] != 0){
				int bid = matrix[i-1][j];
				matrix[i][j] = bid;
				count[bid]++;
			}
			else if(matrix[i][j]==1 && j!=0 && matrix[i][j-1] !=0){
				int bid = matrix[i][j-1];
				matrix[i][j] = bid;
				count[bid]++;
			}
		}
	}
	printf("%d\n", count.size()-1);
	sort(count.begin(),count.end());
	if (count.size()>1){
		for(int i=1;i<count.size();i++){
			printf("%d", count[i]);
			if (i<count.size()){
				printf(" ");
			}
		}
		printf("\n");
	}

}

struct input_data {
  int sizeOfMatrix;
  int **matrix;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.sizeOfMatrix;

  inputData.matrix = new int*[inputData.sizeOfMatrix];
  for (int i = 0; i < inputData.sizeOfMatrix; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    inputData.matrix[i] = new int[inputData.sizeOfMatrix];
    for (int j = 0; j < inputData.sizeOfMatrix; j++) {
      iss >> inputData.matrix[i][j];
    }
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.sizeOfMatrix, inputData.matrix);
  return 0;
}