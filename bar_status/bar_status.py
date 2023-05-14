import sys, time

def progressBar(count, total, suffix=''):
    barLength = 60
    filledLength = int(round(barLength * count / float(total)))

    percent = round(100.0 * count / float(total), 1)
    bar = '=' * filledLength + '-' * (barLength- filledLength)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percent, '%', suffix))

for i in range(1000):
    time.sleep(1)
    progressBar(i, 1000)