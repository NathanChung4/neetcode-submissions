class MedianFinder {
private:
    priority_queue<int, vector<int>> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        // organization
        maxHeap.push(num);
        if (!(minHeap.empty()) && (maxHeap.top() > minHeap.top())) {
            int move = maxHeap.top();
            maxHeap.pop();
            minHeap.push(move);
        }


        // balancing check
        if ((int)maxHeap.size() - (int)minHeap.size() > 1) {
            int move = maxHeap.top();
            maxHeap.pop();
            minHeap.push(move);
        }
        else if ((int)minHeap.size() - (int)maxHeap.size() > 1) {
            int move = minHeap.top();
            minHeap.pop();
            maxHeap.push(move);
        }
    }
    
    double findMedian() {
        // 3 cases
        if (minHeap.size() == maxHeap.size()) {
            return ((double)minHeap.top() + maxHeap.top()) / 2;
        }
        else if (minHeap.size() > maxHeap.size()) {
            return minHeap.top();
        }
        else {
            return maxHeap.top();
        }
        
    }
};
