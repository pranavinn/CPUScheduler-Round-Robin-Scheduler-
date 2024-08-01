# cpu_scheduler.py

class Process:
    def __init__(self, pid, burst_time, arrival_time, priority=None):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = None
        self.start_time = None


class RoundRobinScheduler:
    def __init__(self, time_quantum):
        self.queue = []
        self.time_quantum = time_quantum
        self.current_time = 0
        self.completed_processes = []

    def add_process(self, process):
        if isinstance(process, Process):
            self.queue.append(process)
        else:
            raise TypeError("Only instances of Process can be added")

    def execute(self):
        while self.queue:
            process = self.queue.pop(0)
            if process.start_time is None:
                process.start_time = max(self.current_time, process.arrival_time)
                process.waiting_time = process.start_time - process.arrival_time
                if process.response_time is None:
                    process.response_time = process.waiting_time

            if process.remaining_time > self.time_quantum:
                print(f"Executing process {process.pid} for {self.time_quantum} units")
                process.remaining_time -= self.time_quantum
                self.current_time += self.time_quantum
                self.queue.append(process)
            else:
                print(f"Executing process {process.pid} for {process.remaining_time} units and completing it")
                self.current_time += process.remaining_time
                process.remaining_time = 0
                process.turnaround_time = self.current_time - process.arrival_time
                self.completed_processes.append(process)

    def print_metrics(self):
        total_waiting_time = 0
        total_turnaround_time = 0
        total_response_time = 0
        num_processes = len(self.completed_processes)

        for process in self.completed_processes:
            print(f"Process {process.pid}: Waiting Time = {process.waiting_time}, Turnaround Time = {process.turnaround_time}, Response Time = {process.response_time}")
            total_waiting_time += process.waiting_time
            total_turnaround_time += process.turnaround_time
            total_response_time += process.response_time

        avg_waiting_time = total_waiting_time / num_processes
        avg_turnaround_time = total_turnaround_time / num_processes
        avg_response_time = total_response_time / num_processes

        print(f"Average Waiting Time = {avg_waiting_time}")
        print(f"Average Turnaround Time = {avg_turnaround_time}")
        print(f"Average Response Time = {avg_response_time}")


class PriorityRoundRobinScheduler(RoundRobinScheduler):
    def __init__(self, time_quantum):
        super().__init__(time_quantum)
        self.queue = []

    def add_process(self, process):
        if isinstance(process, Process):
            self.queue.append(process)
            self.queue.sort(key=lambda x: x.priority)
        else:
            raise TypeError("Only instances of Process can be added")

    def execute(self):
        while self.queue:
            process = self.queue.pop(0)
            if process.start_time is None:
                process.start_time = max(self.current_time, process.arrival_time)
                process.waiting_time = process.start_time - process.arrival_time
                if process.response_time is None:
                    process.response_time = process.waiting_time

            if process.remaining_time > self.time_quantum:
                print(f"Executing process {process.pid} for {self.time_quantum} units (Priority {process.priority})")
                process.remaining_time -= self.time_quantum
                self.current_time += self.time_quantum
                self.queue.append(process)
                self.queue.sort(key=lambda x: x.priority)
            else:
                print(f"Executing process {process.pid} for {process.remaining_time} units and completing it (Priority {process.priority})")
                self.current_time += process.remaining_time
                process.remaining_time = 0
                process.turnaround_time = self.current_time - process.arrival_time
                self.completed_processes.append(process)


if __name__ == "__main__":
    # Define processes
    process1 = Process(pid=1, burst_time=5, arrival_time=0, priority=2)
    process2 = Process(pid=2, burst_time=3, arrival_time=2, priority=1)
    process3 = Process(pid=3, burst_time=8, arrival_time=4, priority=3)

    # Create and run the Round Robin Scheduler
    rr_scheduler = RoundRobinScheduler(time_quantum=2)
    rr_scheduler.add_process(process1)
    rr_scheduler.add_process(process2)
    rr_scheduler.add_process(process3)
    rr_scheduler.execute()
    rr_scheduler.print_metrics()

    print("\nPriority Round Robin Scheduling:\n")

    # Create and run the Priority Round Robin Scheduler
    prr_scheduler = PriorityRoundRobinScheduler(time_quantum=2)
    prr_scheduler.add_process(process1)
    prr_scheduler.add_process(process2)
    prr_scheduler.add_process(process3)
    prr_scheduler.execute()
    prr_scheduler.print_metrics()
