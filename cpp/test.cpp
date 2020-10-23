#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> basket;
    for(int t=0;t<moves.size();t++){
        int col = moves[t]-1;
        for(int i=0;i<board.size();i++){
            if (board[i][col] != 0){
                basket.push_back(board[i][col]);
                board[i][col] = 0;
                break;
            }
        }
        if(basket.size() > 1 && basket[basket.size()-1] == basket[basket.size()-2]){
            answer+= 2;
            basket.pop_back();
            basket.pop_back();
        }
    }
    return answer;
}