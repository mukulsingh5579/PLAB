#One-Line Progress Bars (Enlighten)
import enlighten
import time

manager = enlighten.get_manager()
pbar = manager.counter(total=100, desc='Processing Data', unit='ticks')

for i in range(100):
    time.sleep(0.05) # Simulate work
    pbar.update()