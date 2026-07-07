/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // if empty return nullptr
        if (lists.empty()) {
            return nullptr;
        }

        // merge the lists
        while (lists.size() > 1) {
            vector<ListNode*> merged;
            for (int i = 0; i < lists.size(); i += 2) {
                if (i+1 > lists.size() - 1) {
                    merged.push_back(lists[i]);
                }
                else {
                    merged.push_back(merge2Lists(lists[i],lists[i+1]));
                }           
            }
            lists = merged;
        }
        return lists[0];

    }

ListNode* merge2Lists(ListNode* l1, ListNode* l2) {
    ListNode* dummyHead = new ListNode(0);
    ListNode* curr = dummyHead;
    while (l1 && l2) {
        if (l1->val < l2->val) {
            curr->next = l1;
            l1 = l1->next;
            curr = curr->next;
        }
        else {
            curr->next = l2;
            l2 = l2->next;
            curr = curr->next;
        }
    }
    if (l1) {
        curr->next = l1;
    }
    else if (l2) {
        curr->next = l2;
    }
    return dummyHead->next;
}


};
