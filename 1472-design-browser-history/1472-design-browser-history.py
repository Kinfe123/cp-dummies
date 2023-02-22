class BrowserHistory:

    def __init__(self, homepage: str):
        self.hasVisited = []
        self.willVisited = []
        self.currPage = homepage 
        

    def visit(self, url: str) -> None:
        self.hasVisited.append(self.currPage)
        self.currPage = url
        self.willVisited = []
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.hasVisited:
            self.willVisited.append(self.currPage )
            self.currPage = self.hasVisited.pop()
            steps-=1
        return self.currPage 
        

    def forward(self, steps: int) -> str:
        while steps> 0 and self.willVisited:
            self.hasVisited.append(self.currPage)
            self.currPage = self.willVisited.pop()
            steps -= 1
        return self.currPage
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)