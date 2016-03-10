class gobblers():
    self.a=[0,0,0,0,0,0,0,0,0]
    def __init__(self):
        self.small="small"
        self.medium="medium"
        self.big="big"
    def a_hand(self):
        self.hand1=self.small+""+"orange"+self.small+""+"orange"+self.medium+""+"orange"+self.medium+""+"orange"+self.big+""+"orange"+self.big+""+"orange"
    def b_hand(self):
        self.hand2=self.small+""+"blue"+self.small+""+"blue"+self.medium+""+"blue"+self.medium+""+"blue"+self.big+""+"blue"+self.big+""+"blue"
    def game(self,whoplays):
        if x==0:
            print "Player with orange gobblers plays"
            y=raw_input("What gobbler do you want to play? S for small M for medium and B for big")
            if y=="S":
                q=raw_input("Where do you want to put the gobbler? 1 for 1st ...9 for last")
                while self.a[int(q)]!=0:
                    if y>str(self.a[q]):
                        print "YOU CANNOT PUT IT THERE"
                        q=raw_input()
                else:
                    self.a.insert(y+" orange",int(q))
                    self.hand1.remove("small orange")
            if y=="M":
                q=raw_input("Where do you want to put the gobbler? 1 for 1st ...9 for last")
                while self.a[int(q)]!=0:
                    if y>str(self.a[q]):
                        print "YOU CANNOT PUT IT THERE"
                        q=raw_input()
                else:
                    self.a.insert(y+" orange",int(q))
                    self.hand1.remove("medium orange")
            if y=="B":
                q=raw_input("Where do you want to put the gobbler? 1 for 1st ...9 for last")
                self.a.insert(y+" orange",int(q))
                self.hand1.remove("big orange") 
        else:
            print "Player with blue gobblers plays"
            y=raw_input("What gobbler do you want to play? S for small M for medium and B for big")
            if y=="S":
                q=raw_input("Where do you want to put the gobbler? 1 for 1st ...9 for last")
                while self.a[int(q)]!=0:
                    if y>str(self.a[q]):
                        print "YOU CANNOT PUT IT THERE"
                        q=raw_input()
 
                self.a.insert(y+"blue",int(q))
                self.hand2.remove("small blue") 
            if y=="M":
                q=raw_input("Where do you want to put the gobbler? 1 for 1st ...9 for last")
                while self.a[int(q)]!=0:
                    if y>str(self.a[q]):
                        print "YOU CANNOT PUT IT THERE"
                        q=raw_input()
                else:
                    self.a.insert(y+"orange",int(q))
                    self.hand2.remove("medium blue")
            if y=="B":
                q=raw_input("Where do you want to put the gobbler? 1 for 1st ...9 for last")
                a.insert(y+"blue",int(q))
                self.hand2.remove("big blue")
    def whoplays(self,x):
        if x==0:
            x=1
        else :
            x=0
        return x