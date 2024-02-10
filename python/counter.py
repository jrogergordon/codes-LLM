import statistics

def stat(numbers):
    # Calculate sum
    sum_ = sum(numbers)

    # Calculate average
    average = sum_ / len(numbers)

    # Calculate median
    median = statistics.median(numbers)

    # Calculate mode
    mode = statistics.mode(numbers)

    # Calculate range
    max_value = max(numbers)
    min_value = min(numbers)
    range_ = max_value - min_value

    # Return dictionary with all the stats
    return {
        "sum": sum_,
        "average": average,
        "median": median,
        "mode": mode,
        "range": range_
    }
 


ans = stat([6,1,2,1,3,3,3,4,2,])   
print(ans)  