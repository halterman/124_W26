class Counter: 
    def __init__(self, n: int) -> None: 
        self.limit = n 
        self.count = 0 
 
    def __repr__(self) -> str: 
        return f'{self.count}/{self.limit}' 
     
    def inc(self) -> None: 
        if self.count < self.limit: 
            self.count += 1 
 
    def dec(self) -> None: 
        if self.count > 0: 
            self.count -= 1 
 
    def reset(self) -> None: 
        self.count = 0 
 
    def get(self) -> int: 
        return self.count 
         
 
if __name__ == "__main__": 
    ctr1 = Counter(3) 
    ctr2 = Counter(5) 
 
    for _ in range(7): 
        ctr1.inc() 
        ctr2.inc() 
        print(f'ctr1 = {ctr1}, ctr2 = {ctr2}') 
 
    print('---------------') 
 
    for _ in range(5): 
        ctr1.dec() 
        ctr2.dec() 
        print(f'ctr1 = {ctr1}, ctr2 = {ctr2}') 
 
    print('---------------') 
 
    ctr1.inc() 
    ctr1.inc() 
    ctr1.inc() 
    print(ctr1.get()) 