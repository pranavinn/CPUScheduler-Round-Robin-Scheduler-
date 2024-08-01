Done using:
1. Round Robin Scheduling:
Algorithm: Round Robin (RR) is a CPU scheduling method that assigns each process a fixed time slice or quantum in a cyclic order. When a process's time slice expires, it is moved to the end of the queue, and the CPU is allocated to the next process in line. If a process completes before its time slice expires, it is removed from the queue.
Objective: To provide a fair distribution of CPU time among processes and prevent starvation, ensuring that all processes get a chance to execute.
2. Priority Scheduling:
Algorithm: Priority Scheduling assigns the CPU to processes based on their priority levels. Higher priority processes are scheduled before lower priority ones. In preemptive priority scheduling, if a new process arrives with a higher priority than the currently executing process, the CPU is reassigned to the higher priority process.
Objective: To ensure that critical processes are executed earlier, potentially improving responsiveness for high-priority tasks. However, it can lead to starvation for low-priority processes.
3. Priority Round Robin Scheduling:
Algorithm: Priority Round Robin combines the principles of Round Robin and Priority Scheduling. Processes are assigned priorities, and within each priority level, Round Robin scheduling is used. This means processes are executed in a cyclic order within their priority level, and higher priority processes are scheduled before lower priority ones.
Objective: To ensure both fair time-sharing among processes of the same priority and prioritize more important processes. It balances the benefits of Round Robin scheduling with the efficiency of priority-based scheduling.
