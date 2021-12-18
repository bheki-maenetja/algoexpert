def minimumWaitingTime(queries):
    # Write your code here.
    if len(queries) == 1: return 0
    queries.sort()
    waiting_time = 0
    
    for i in range(1, len(queries)):
        waiting_time += sum(queries[:i])
    return waiting_time