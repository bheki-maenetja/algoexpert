#include <vector>
using namespace std;
vector<int> sortVector(vector<int>);

vector<int> findThreeLargestNumbers(vector<int> array) {
  // Write your code here.
	vector<int> return_vector = sortVector({array[0], array[1], array[2]});
	if (array.size() == 3) {
		return return_vector;
	}
	for (int i = 3; i < array.size(); i++) {
		if (array[i] > return_vector[2]) {
			int temp1, temp2;
			temp1 = return_vector[2];
			temp2 = return_vector[1];
			return_vector[2] = array[i];
			return_vector[1] = temp1;
			return_vector[0] = temp2;
		} else if (array[i] > return_vector[1]) {
			int temp = return_vector[1];
			return_vector[1] = array[i];
			return_vector[0] = temp;
		} else if (array[i] > return_vector[0]) {
			return_vector[0] = array[i];
		}
	}
  return return_vector;
}

vector<int> sortVector(vector<int> input) {
	bool isSorted = false;
	while (!isSorted) {
		isSorted = true;
		for (int i = 0; i < input.size() - 1; i++) {
			if (input[i] > input[i+1]) {
				int temp = input[i+1];
				input[i+1] = input[i];
				input[i] = temp;
				isSorted = false;
			} 
		}
	}
	return input;
}