class Solution:
    def rowWithMax1s(self, mat):
        max_ones=-1
        ind=-1

        for i,j in enumerate(mat):
          count=j.count(1)
          if count>max_count:
            max_count=count
            ind=i

        return ind
