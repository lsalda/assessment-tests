
# Sample solution

class IdentityResolutionApi:
    def __init__ (self):
        self.graph = {}

    def addLink(self, id1, id2):
        self.graph.setdefault(id1, set()).add(id2)
        self.graph.setdefault(id2, set()).add(id1)
        return True

    def isLinked(self, id1, id2):
        if id1 == id2:
            return True
        q = []
        q.append(id1)
        visited = set()
        while q:
            v = q.pop(0)
            visited.add(v)
            for n in self.graph.get(v, set()):
                if n in visited:
                    continue
                if n == id2:
                    return True
                q.append(n)
        return False

    def removeId(self, id):
       for n in self.graph.get(id, set()):
           if n != id: ### self link case
                self.graph[n] |= self.graph[id]
                self.graph[n].remove(id)
       self.graph.pop(id, None)
       return True

# Boilerplate below to emulate successive API calls.
# Do not change

def solution(operationsToPerform, firstArgs, secondArgs):
    isLinkedResults = []
    api = IdentityResolutionApi()

    for opNum in range(len(operationsToPerform)):
        isLinkedResults.append(callOperation(api, operationsToPerform[opNum], firstArgs[opNum], secondArgs[opNum]))

    return isLinkedResults;

def callOperation(api, operationType, firstArg, secondArg):
    if (operationType == 0):
        api.addLink(firstArg, secondArg)
    elif (operationType == 1):
        return api.isLinked(firstArg, secondArg)
    elif (operationType == 2):
        api.removeId(firstArg)

    return True

if __name__ == "__main__":

    test_cases = [
        # test1 [basic linkage]
        [[0,1],["a1","a1"],["a2","a2"],[True,True]],
        # test2 [bidirectional linkage]
        [[0,1],["a1","a2"],["a2","a1"],[True,True]],
        # test3 [self linkage]
        [[0,1],["a1","a1"],["a1","a1"],[True,True]],
        # test4 [basic remove]
        [[0,1,2,1],["a1","a1","a1","a1"],["a2","a2","na","a2"],[True,True,True,False]],
        # test5 [multiple linkages]
        [[0,0,1,1],["a1","a1","a1","a1"],["a2","a3","a2","a3"],[True,True,True,True]],
        # test6 [disjoint identifiers]
        [[0,0,1,1,1,1],["a1","a3","a1","a3","a1","a2"],["a2","a4","a2","a4","a3","a4"],[True,True,True,True,False,False]],
        # test7 [nonexistent remove]
        [[0,2,1],["a1","a3","a1"],["a2","na","a2"],[True,True,True]],
        # test8 [transitivity]
        [[0,0,0,0,1,1,1,1,1],["a1","a2","a3","a4","a1","a2","a3","a4","a1"],["a2","a3","a4","a5","a2","a3","a4","a5","a5"],[True,True,True,True,True,True,True,True,True]],
        # test9 [transitivity post removal]
        [[0,0,2,1,1],["a1","a2","a2","a1","a1"],["a2","a3","na","a2","a3"],[True,True,True,False,True]],
        # test10 [joining identifier sets]
        [[0,0,1,0,1,1,1,1,1,1],["a1","a3","a1","a1","a1","a1","a1","a2","a2","a3"],["a2","a4","a3","a3","a2","a3","a4","a3","a4","a4"],[True,True,False,True,True,True,True,True,True,True]],
    ]

    f = 0
    for t in test_cases:
        try:
            assert t[3] == solution(t[0],t[1],t[2])
        except:
            f += 1

    print 'Passed {}/{}'.format(len(test_cases)-f,len(test_cases))