def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        #creating a dictionary this will have size at max 26 only
        d={}
        
        for i in sentence:
            #feed into dictionary all the letters only once.
            if i not in d:
                d[i]=1
               
        if len(d)==26:
            return True
        return False
                
