import time
import statistics

def time_solver(func):
    """Decorator to measure and print the execution time of a function with adaptive averaging."""
    def wrapper(*args, **kwargs):
        # Run once to get the result and initial timing
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        first_run = end_time - start_time
        
        # Determine number of iterations based on execution time
        if first_run >= 1.0:
            # Slow functions (≥1s): single run is sufficient
            iterations = 1
            times = [first_run]
        elif first_run >= 0.01:
            # Medium functions (10ms-1s): 3-10 runs
            iterations = min(10, max(3, int(0.5 / first_run)))
            times = [first_run]
            for _ in range(iterations - 1):
                start = time.perf_counter()
                func(*args, **kwargs)
                times.append(time.perf_counter() - start)
        else:
            # Fast functions (<10ms): many runs for accuracy
            iterations = min(1000, max(10, int(0.1 / first_run)))
            times = [first_run]
            for _ in range(iterations - 1):
                start = time.perf_counter()
                func(*args, **kwargs)
                times.append(time.perf_counter() - start)
        
        # Calculate statistics
        avg_time = statistics.mean(times)
        
        if iterations > 1:
            stdev = statistics.stdev(times) if len(times) > 1 else 0
            median_time = statistics.median(times)
            min_time = min(times)
        
        # Format time appropriately based on magnitude
        print(f"[{func.__name__}] Result: {result}")
        
        if avg_time >= 1.0:
            time_str = f"{avg_time:.3f} s"
        elif avg_time >= 0.001:
            time_str = f"{avg_time * 1000:.3f} ms"
        elif avg_time >= 0.000001:
            time_str = f"{avg_time * 1_000_000:.3f} µs"
        else:
            time_str = f"{avg_time * 1_000_000_000:.0f} ns"
        
        if iterations > 1:
            if stdev / avg_time > 0.1:  # High variance (>10%)
                print(f"[{func.__name__}] Time: {time_str} (avg of {iterations} runs, ±{stdev/avg_time*100:.1f}%)")
            else:
                print(f"[{func.__name__}] Time: {time_str} (avg of {iterations} runs)")
        else:
            print(f"[{func.__name__}] Time: {time_str}")
        
        return result
    return wrapper