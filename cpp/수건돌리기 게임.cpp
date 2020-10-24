#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

void solution(int numOfAllPlayers, int numOfQuickPlayers, char *namesOfQuickPlayers, int numOfGames, int *numOfMovesPerGame) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
	int human[numOfAllPlayers];
	int count[numOfAllPlayers] = {0,};
	int target = 'A';
	int where = 0;
	
	count[0] = 1;
	for(int i=0;i<numOfAllPlayers;i++){
		human[i] = i+66;
	}
	
	for(int t=0;t<numOfGames;t++){
		where += numOfMovesPerGame[t] + numOfAllPlayers-1;
		where = where % (numOfAllPlayers-1);
		//printf("%d\n", where);
		int flag = 1;
		for(int k=0;k<numOfQuickPlayers;k++){
			if(namesOfQuickPlayers[k] == human[where]){
				flag = 0;
				break;
			}
		}
		if(flag ==1){
			char tmp = target;
			target = human[where];
			human[where] = tmp;
		}
		count[target-65]++;
		
	}
	
	for(int t=0;t<numOfAllPlayers-1;t++){
		printf("%c %d\n", human[t], count[human[t]-65]);
	}
	printf("%c %d\n", target, count[target-65]);
}

struct input_data {
  int numOfAllPlayers;
  int numOfQuickPlayers;
  char *namesOfQuickPlayers;
  int numOfGames;
  int *numOfMovesPerGame;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.numOfAllPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfQuickPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
  for (int i = 0; i < inputData.numOfQuickPlayers; i++) {
    iss >> inputData.namesOfQuickPlayers[i];
  }

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfGames;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.numOfMovesPerGame = new int[inputData.numOfGames];
  for (int i = 0; i < inputData.numOfGames; i++) {
    iss >> inputData.numOfMovesPerGame[i];
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  return 0;
}