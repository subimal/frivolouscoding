from fractions import Fraction
from copy import deepcopy

class matrix:
    def __init__(self, M=[[]]):
        assert type(M[0])==type([]), "Check matrix dimensions."
        self.M = deepcopy(M)
        self.size = [len(list(M)), len(M[0])]
        N1, N2 = self.size
        for i in range(N1):
            for j in range(N2):
                self.M[i][j] = Fraction(M[i][j])
                
    def __repr__(self):
        return str(self.M)
    
    def __getitem__(self, i):
        return self.M[i]

    def __setitem__(self, i, value):
        self.M[i] = value

    def __add__(self, M2):
        N1, N2 = self.size
        assert M2.size==self.size, "Check matrix dimensions."
        ans = deepcopy(self.M)
        #ans = matrix([ [0 for i in range(N2)] for j in range(N1)])
        for i in range(N1):
            for j in range(N2):
                ans[i][j] = ans[i][j] + M2[i][j] 
        return matrix(ans)
    
    def __sub__(self, M2):
        N1, N2 = self.size
        assert M2.size==self.size, "Check matrix dimensions."
        ans = deepcopy(self.M)
        for i in range(N1):
            for j in range(N2):
                ans[i][j] = ans[i][j] - M2[i][j] 
        return matrix(ans)

    def __mul__(self, M2):

        N1, N2 = self.size
        if isinstance(M2, int) or isinstance(M2, float) or isinstance(M2, Fraction):
            ans = deepcopy(self.M)
            for i in range(N1):
                for j in range(N2):
                    ans[i][j] = Fraction(M2)*ans[i][j]
        elif isinstance(M2, matrix):
            assert self.size[1] == M2.size[0], "Matrix dimensions mismatch. Can't multiply."
            N3 = M2.size[1]
            ans = matrix([ [0 for i in range(N3)] for j in range(N1)])
            for i in range(N1):
                for j in range(N3):
                    for k in range(N2):
                        ans[i][j] = ans[i][j] + self.M[i][k]*M2[k][j]
        else:
            raise TypeError, "Wrong object type being multiplied to a matrix."
        
        return matrix(ans)
    
    __rmul__ = __mul__

    def tr(self):
        from copy import deepcopy
        N1, N2 = self.size
        M = deepcopy(self.M)
        ans = matrix([ [0 for i in range(N1)] for j in range(N2)])
        for i in range(N2):
            for j in range(N1):
                ans[i][j] = M[j][i]
        return ans

    def O(self, M, N):
        return matrix([ [0 for i in range(N)] for j in range(M)])
    
    def ones(self, M, N):
        return matrix([ [1 for i in range(N)] for j in range(M)])
    
    def I(self, M):
        ans = matrix([ [0 for i in range(M)] for j in range(M)])
        for i in range(M):
            ans[i][i] = Fraction(1)
        return ans
    
    def det(self):
        assert self.size[0]==self.size[1], "Need a square matrix."
        if self.size == [1,1]:
            return self.M[0][0]
        else:
            ans = 0
            for i in range(self.size[0]):
                    M1 = deepcopy(self.M)
                    del M1[i]
                    M1 = matrix(M1)
                    M1 = list(M1.tr())
                    del M1[0]
                    M1 = matrix(M1)
                    M1 = M1.tr()
                    ans = ans + ((-1)**(i))*self.M[i][0]*M1.det()
        return ans
    
    def minors(self):
        ans = matrix(self.M)*0
        for j in range(self.size[1]):
            for i in range(self.size[0]):
                M1 = deepcopy(self.M)
                del M1[i]
                M1 = matrix(M1)
                M1 = list(M1.tr())
                del M1[j]
                M1 = matrix(M1)
                M1 = M1.tr()
                ans[i][j] = M1.det()
        return ans
        
    def cofactors(self):
        ans = matrix(self.M).minors()
        for j in range(self.size[1]):
            for i in range(self.size[0]):
                ans[i][j] = ((-1)**(i+j))*ans[i][j]
        return ans
    
    def adjoint(self):
        ans = matrix(self.M).cofactors()
        ans = ans.tr()
        return ans
    
    def inverse(self):
        det = matrix(self.M).det()
        ans = matrix(self.M).adjoint()
        ans = ans*(1/det)
        return ans

if __name__=='__main__':
    M = matrix([[1,2],[3,4]])
    M1 = matrix([[1,2],[3,5]])
    M2 = matrix([[1],[3]])
    M3 = matrix([[1,2]])
    M4 = matrix([[1,2,3], [4,5,6], [7,8,10]])
    print M4.det()
    m5 = matrix([[3,8],[4,6]])
    print m5.det()
    m6 = matrix([[6,1,1], [4,-2,5], [2,8,7]])
    print m6.det()
    
    M = matrix([[3,0,2],[2,0,-2],[0,1,1]])
    print M.minors()
    print M.cofactors()
    print M.adjoint()
    print M.det()
    print M.inverse()
