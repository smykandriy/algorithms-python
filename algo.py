from functools import wraps
import time


def measure_execution_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_timestamp = time.perf_counter()
        result = function(*args, **kwargs)
        end_timestamp = time.perf_counter()
        execution_time = end_timestamp - start_timestamp
        print(f"Function {function.__name__}{args} took {execution_time}")
        return result

    return wrapper


@measure_execution_time
def get_minimum_sorting_range(int_list: list[int]) -> tuple[int, int]:
    index_range = len(int_list) - 1
    first_unsorted_index = last_unsorted_index = -1

    if index_range > 1:
        for index in range(index_range):
            if int_list[index] >= int_list[index + 1]:
                first_unsorted_index = index
                break
        for index in range(index_range, 0, -1):
            if int_list[index] <= int_list[index - 1]:
                last_unsorted_index = index
                break

    return first_unsorted_index, last_unsorted_index
