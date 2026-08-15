class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maximumArea = 0;

        int l = 0;
        int r = heights.size()-1;

        while (l < r) {
            int area = min(heights[l], heights[r]) * (r-l);

            maximumArea = max(maximumArea, area);

            if (heights[l] < heights[r]) {
                l += 1;
            }
            else {
                r -= 1;
            }
        }
        return maximumArea;

    }
};
