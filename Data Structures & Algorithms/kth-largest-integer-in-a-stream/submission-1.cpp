class KthLargest {
private:
    int K;
    priority_queue<int, vector<int>, greater<int>> heap;
public:
    KthLargest(int k, vector<int>& nums) {
        K = k;
        for (int i = 0; i < nums.size(); i++) {
            int kth = add(nums[i]);
        }
        
    }
    
    int add(int val) {
        if (int(heap.size()) < K) {
            heap.push(val);
        }
        else if (heap.top() < val) {
            heap.pop();
            heap.push(val);
        }

        return heap.top();
    }
};
