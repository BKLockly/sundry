#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MACHINE_NUM 3

void MultiScheduling(vector<vector<int>>& works, vector<vector<pair<int, int>>>& arrange, vector<int>& runTime) {
	if (MACHINE_NUM >= works.size()) {
        //机器数目大于等于作业个数时直接分配
		for (int i = 0; i < works.size(); i++) {
			auto work = make_pair(works[i][0], works[i][1]);
			arrange[i].push_back(work);
			runTime[i] = works[i][1];
		}
		return;
	}

	sort(works.begin(), works.end(),
		[](vector<int>& a, vector<int>& b) ->bool {
			return a[1] > b[1];
		});
        //按照作业所需时间降序排序

	int curMinTimeIndex = 0;
    //最小运行时间的机器编号
	for (int i = 0; i < works.size(); ++i) {	
		curMinTimeIndex = min_element(runTime.begin(), runTime.end()) - runTime.begin();
		runTime[curMinTimeIndex] += works[i][1];
        //机器执行作业的时间
		arrange[curMinTimeIndex].push_back({ make_pair(works[i][0],works[i][1]) });
        //第i个作业被分配的情况
	}
}

//打印每台机器被调度之后的结果
void Print(vector<vector<pair<int, int>>>& arrange, vector<int>& runTime) {
	for (int i = 0; i < arrange.size(); i++) {
		cout << "第" << i + 1 << "台机器的作业: " << endl;
		for (int j = 0; j < arrange[i].size(); j++) {
			cout << arrange[i][j].first << "号作业时长: " 
				 << arrange[i][j].second << "h" << endl;
		}
		cout << "第" << i + 1 << "台机器总运行时长: " 
			 << runTime[i] << endl << endl;
	}
}

int main() {
	vector<vector<int>> works{
		{1,2},{2,14},{3,4},{4,6},{5,16},{6,5},{7,3}
        // 将7个作业依次从1到7命名组成数组
	};
	vector<vector<pair<int, int>>> arrange(MACHINE_NUM);
	//记录每台机器全部作业时间
	vector<int> runTime(MACHINE_NUM, 0);
	MultiScheduling(works, arrange, runTime);
	Print(arrange, runTime);
	return 0;
}
