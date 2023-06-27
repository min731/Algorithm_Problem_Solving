# nodes = ['cpp', 'java', 'python',
#          'backend', 'frontend',
#           'junior', 'senior',
#           'chicken', 'pizza']

def solution(info, query):
    answer = []

    par = {'-':-1,'cpp':0, 'java':1, 'python':2,
         'backend':3, 'frontend':4,
          'junior':5, 'senior':6,
          'chicken':7, 'pizza':8}

    for inf in info:
        inf = inf.split(" ")
        par_inf = []
        for i in range(4):
            par_inf.append(par[inf[i]])
        par_inf.append(int(inf[-1]))
    
        print(par_inf)

    

    return answer

solution(["java backend junior pizza 150",
          "python frontend senior chicken 210",
          "python frontend senior chicken 150",
          "cpp backend senior pizza 260",
          "java backend junior chicken 80",
          "python backend senior chicken 50"],

          ["java and backend and junior and pizza 100",
           "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250",
           "- and backend and senior and - 150",
           "- and - and - and chicken 100",
           "- and - and - and - 150"]

          )


class BTree:

    def __init__(self,r):
        self.root = r

class Node:

    def __init__(self,item):
        self.data = item
        self.left = None
        self.right = None