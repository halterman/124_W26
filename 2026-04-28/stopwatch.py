from time import perf_counter_ns

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

    def __repr__(self) -> str:
        sec = round(self.elapsed_time/1_000_000_000)
        hr = sec // 3600
        sec = sec % 3600
        min = sec // 60
        sec = sec % 60
        return f'{hr:02}:{min:02}:{sec:02}'

    def start(self) -> None:
        if not self.running:
            self.start_time = perf_counter_ns()
            self.running = True

    def stop(self) -> None:
        if self.running:
            self.elapsed_time = perf_counter_ns() - self.start_time
            self.running = False
    
    def elapsed(self) -> float:
        return self.elapsed_time /1_000_000_000
