"""
Browser History
---------------

https://leetcode.com/problems/design-browser-history/

"""

class BrowserHistory:
    
    def __init__(self, homepage: str):
        
        self.home_page = homepage
        self.history = [homepage]
        self.current_page = homepage
        
    def visit(self, page: str) -> None:
        
        self.history.append(page)
        self.current_page = page
        
    def move(self, positions: int) -> bool:
        
        current_position = self.history.index(self.current_page)
        
        if positions < 0:
            if abs(positions) > (current_position+1):
                move_to = 0
            else:
                move_to = current_position + positions
        else:
            if positions > (current_position - len(self.history))-1:
                move_to = len(self.history) - 1
            else:
                move_to = current_position + positions
                
        self.current_page = self.history[move_to]
        
        
        
########################################
if __name__ == "__main__":
    
    browser = BrowserHistory("google.com")
    browser.visit("leetcode.com")
    print(browser.current_page)
    browser.visit("myspace.com")
    print(browser.current_page)
    print(browser.history)
    browser.move(-1)
    print(browser.current_page)
    browser.move(2)
    print(browser.current_page)
        