"""The main module to show the decorator design pattern"""
import time

def example_timing():
    """function to show how to decorator a function to add timing"""
    def time_it(fn):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            fn(*args, **kwargs)
            print(f"fn took: {time.time() - start_time} seconds")

        return wrapper

    @time_it
    def run():
        time.sleep(0.1)

    run()

def example_logging():
    """function to show how to decorator a function to add logs"""
    def logger_fn(fn):
        def wrapper(*args, **kwargs):
            print("logging to a file: " + " ".join([str(arg) for arg in args]))
            return fn(*args, **kwargs)

        return wrapper

    @logger_fn
    def my_fn(a: int, b: int, c: int = 20) -> int:
        return a * b * c

    print(my_fn(20, 54))

def main() -> None:
    """The main function to show the decorator example"""
    example_timing()
    example_logging()

main()
