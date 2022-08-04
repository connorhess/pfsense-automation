import time
from progress.bar import Bar
from pfsense.core import run

days = 7
hours = days*24
minutes = hours * 60
seconds = minutes * 60
seconds = 60

for i in range(10):
    run()
    bar = Bar('Sleeping', max=seconds)
    for i in range(seconds):
        # Do some work
        bar.next()
        time.sleep(1)
    bar.finish()

