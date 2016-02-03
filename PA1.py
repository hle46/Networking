import random
from math import sqrt
def flip(p):
    if random.random() <= p:
        return 1
    else:
        return 0

max_time_slots = 100000
departure_rate = 0.25
arrival_rate = 0.25
step = 1.0
arrival_rates = [0.0]
delays = [0.0]
while (arrival_rate <= 1.0):
    p = arrival_rate * (1 - departure_rate) / ((1 - arrival_rate) * departure_rate)
    mean_queue_length = 0.0
    std_queue_length = 0.0
    M2 = 0.0
    epoch = 0
    while True:
        epoch += 1
        n = 0
        random.seed(epoch)
        num_jobs = 0
        total_jobs = 0
        s2 = 0.0
        s = 0.0
        while (n < max_time_slots):
            if (flip(arrival_rate) == 1):
                num_jobs += 1
            if (num_jobs >= 1 and flip(departure_rate) == 1):
                num_jobs -= 1
            n += 1
            total_jobs += num_jobs
            s2 += num_jobs * num_jobs
        queue_length = float(total_jobs) / n
        print queue_length * 0.05
        print sqrt(((s2 - (total_jobs * total_jobs) / n) / (n - 1))) / sqrt(n)
        delta = queue_length - mean_queue_length
        mean_queue_length += delta / epoch
        M2 += delta * (queue_length - mean_queue_length)
        if (epoch > 1):
            std_queue_length = sqrt(M2 / (epoch - 1))
            if (std_queue_length <= 0.05 * mean_queue_length):
                break

    print "Num epochs: ", epoch
    print "Simulated Queue Length: ", mean_queue_length
    if (p < 1):
        print "Theoretical Queue Length: ", p / (1 - p)
    else:
        print "Cannot calculate theoretical queue length"
    print "----------------------------------------------"
    arrival_rates.append(arrival_rate)
    delays.append(mean_queue_length / arrival_rate)
    arrival_rate += step
print arrival_rates
print delays
import matplotlib.pyplot as plt
plt.semilogy(arrival_rates, delays)
plt.xlabel("Arrival Rate")
plt.ylabel("Job Expected Delay")
plt.title("Job Expected Delay vs Arrival Rate")
plt.grid(True)
plt.show()
