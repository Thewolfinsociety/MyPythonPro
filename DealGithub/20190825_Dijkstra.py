# _*_ coding:utf-8 _*_

#@Time :2019/8/25 

# @Author : litao

# @File : 20190825_Dijkstra.py

#目的计算最短路径
class Solution(object):
    def dijkstra(self, weight, start):

        # 接受一个有向图的权重矩阵weight，和一个起点编号start（从0编号，顶点存在数组中）
        # 返回一个int[]数组，表示从start到它的最短路径长度

        n = len(weight) # 顶点个数

        shortPath = [0]*n
        # 保存start到其他各点的最短路径
        path = [''] * n #保存start到其他各点最短路径的字符串表示

        for i in range(0, n):
            path[i] = str(start) + "-->" + str(i)
        visited = [0] * n  # 标记当前该顶点的最短路径是否已经求出, 1表示已求出
            # 初始化，第一个顶点已经求出
        shortPath[start] = 0
        visited[start] = 1

        for count in xrange(1, n): # 要加入n-1个顶点
            k = -1 #选出一个距离初始顶点start最近的未标记顶点
            dmin = 2^31 - 1
            for i in range(0, n):
                if (visited[i] == 0 and weight[start][i] < dmin):
                    dmin = weight[start][i]
                    k = i

        # 将新选出的顶点标记为已求出最短路径，且到start的最短路径就是dmin
            shortPath[k] = dmin
            visited[k] = 1

        # 以k为中间点，修正从start到未访问各点的距离
            for i in range(0, n):
            # 如果 '起始点到当前点距离' + '当前点到某点距离' < '起始点到某点距离', 则更新
                if (visited[i] == 0 and weight[start][k] + weight[k][i] < weight[start][i]):
                    weight[start][i] = weight[start][k] + weight[k][i]
                    path[i] = path[k] + "-->" + str(i)

        for i in range(0, n):

            print("从" + str(start) + "出发到" + str(i) + "的最短路径为：" + path[i])

        print("=====================================")
        return shortPath
s = Solution()
M = 10000
weight = [
                [0,4,M,2,M],
                [4,0,4,1,M],
                [M,4,0,1,3],
                [2,1,1,0,7],
                [M,M,3,7,0]
            ]

start = 0
s.dijkstra(weight, start)