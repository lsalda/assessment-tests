Please implement your small-scale solution. Do not worry about there being 5 trillion edges yet. (You can worry about that once you join the company). As a reminder, here are the three necessary endpoints:

void addLink(String id1, String id2)
bool isLinked(String id1, String id2)
void removeID(String id)

Feel free to change your solution if you think of a better approach as you work through the code. If you do make changes, please explain why you chose to go with the new approach.

Note that you can add your own test cases by clicking the white + in the test window. An example test case is [[0, 1], ["abc1", "abc1"], ["abc2", "abc2"]] which means "call addLink('abc1', 'abc2'), then call isLinked('abc1', 'abc2')". The output should be [true, true].