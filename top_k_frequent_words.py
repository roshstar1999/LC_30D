
#first time using Counter and lambda function,this was an upsolve
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=Counter(words)
        keys=list(d.keys())
        key.sort(key=lambda x: -d[x],x)
        return keys[:k]
        
        
        
        
    
