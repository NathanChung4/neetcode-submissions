class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // no need for negation
        priority_queue<int> heap;

        // add to heap
        for (int i = 0; i < stones.size(); i++) {
            heap.push(stones[i]);
        }

        while (heap.size() > 1) {
            int first = heap.top();
            heap.pop();
            int second = heap.top();
            heap.pop();

            if (first > second) {
                first -= second;
                heap.push(first);
            }
        }

        if (heap.empty()) {
            return 0;
        }
        else {
            return heap.top();
        }
    }
};
