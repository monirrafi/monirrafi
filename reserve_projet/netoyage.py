    def sorting(self):
        p = Hand()
        for i in range(self.leng_cards()):
            petit = self.cards[0]
            for j in range(i+1,self.leng_cards()):
                if self.cards[j].rank <= petit.rank:
                    self.move_one_card(self.cards[j],p)
                    petit=self.cards[j]
                    #self.cards[i],petit=petit,self.cards[i]
        return p
#    def brasser (self):
#        random.shuffle(self.cards)
#    def insert(self,i,carte):
#        self.cards.insert(i,carte)

#    def index(self,card):
#        for i in range(self.leng_cards()):
#            if card == self.cards[i]:
#                return i
    def sort_l(p):
        q=Hand()
        dic = {}
        for card in p.cards:
            dic[card.__repr__()]= card.rank
        stdls = list(dic.values())
#        for rank in range(len(stdls)):
#            q.add_card(list(dic.keys())[i])
        return sorted(p.cards)
    
    def s_l(stdls):
        
        for i in range(len(stdls)):
            minval = i
            for j in range(i+1, len(stdls)):
                if stdls[minval] >= stdls[j]:
                    minval = j
                    stdls[i], stdls[minval] = stdls[minval], stdls[i]
        return stdls
