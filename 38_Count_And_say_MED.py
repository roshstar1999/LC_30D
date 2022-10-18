
class Solution:
    def countAndSay(self,n):
        if n==1:
            return '1'
    
        l=self.countAndSay(n-1)
    
        x=''
        count=1
        i=0
        #for i in range(len(l)-1):
        while i<len(l)-1:

            if l[i]==l[i+1]:
                count+=1
            else:
                x+=str(count)+str(l[i])
                count=1
            i+=1
        x+=str(count)+str(l[i])
        return x


        
