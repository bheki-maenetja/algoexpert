using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
// Write your code here.
    int seq_index = 0;
    for (int i = 0; i < array.size(); i++) {
        if (array[i] == sequence[seq_index]) {
            seq_index += 1;
        }
        if (seq_index == sequence.size()) {
            return true;
        }
    }
return false;
}