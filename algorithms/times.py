# a function wrapper that times execution
import time

def time_execution(func):
    """
    Decorator function that measures the execution time of a given function.
    
    Args:
        func: The function to be executed and measured.
        
    Returns:
        The wrapped function that measures and prints the execution time, and returns the result of the original function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        if execution_time < 1:
            print(f"Execution time: {round(execution_time * 1000,2)} ms")
        else:
            print(f"Execution time: {round(execution_time,2)} s")
        
        return result
    return wrapper





if __name__ == "__main__":
    @time_execution
    def dummy():
        for i in range(1_000_0000):
            pass


