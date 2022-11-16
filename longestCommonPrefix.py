def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs)==1:
            return strs[0]
        count=0
        
        minn=min(strs)
        maxx=max(strs)
        
        for i in range(len(minn)):
            if minn[i]!=maxx[i]:
                break
            else: 
                count+=1
    
        return minn[:count]
