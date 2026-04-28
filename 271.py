#Measuring Execution Time
import time

start_time = time.time()

# A dummy task: summing 1 million numbers
total = sum(range(1_000_000))

end_time = time.time()
print(f"Task completed in {end_time - start_time:.4f} seconds.")