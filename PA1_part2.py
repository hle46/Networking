import random
from math import sqrt
def flip(p):
    if random.random() <= p:
        return 1
    else:
        return 0

departure_rate1 = 0.1
departure_rate2 = 0.5
p_service = 0.25
arrival_rate = 0.01
step = 0.01
arrival_rates = [0.0]
delays = [0.0]
while (arrival_rate <= 1.0):
    num_jobs = 0
    mean_queue_length = 0.0
    M2 = 0.0
    epoch = 0
    while True:
        random.seed(epoch)
        if (flip(arrival_rate) == 1):
            num_jobs += 1
        if (num_jobs >= 1):
            if (flip(p_service) == 1):
                if (flip(departure_rate1) == 1):
                    num_jobs -= 1
            else:
                if (flip(departure_rate2) == 1):
                    num_jobs -= 1
        epoch += 1
        delta = num_jobs - mean_queue_length
        mean_queue_length += delta / epoch
        M2 += delta * (num_jobs - mean_queue_length)
        if (epoch > 1):
            var_queue_length = M2 / (epoch - 1)
            std_mean_queue_length = sqrt(var_queue_length / epoch)
            if (std_mean_queue_length > 0.0 and std_mean_queue_length <= (0.05 * mean_queue_length)):
                break
    print "Arrival rate: ", arrival_rate
    print "Num epochs: ", epoch
    print "Simulated Queue Length: ", mean_queue_length
    arrival_rates.append(arrival_rate)
    delays.append(mean_queue_length / arrival_rate)
    arrival_rate += step
print arrival_rates
print delays
import matplotlib.pyplot as plt
plt.plot(arrival_rates, delays)
plt.xlabel("Arrival Rate")
plt.ylabel("Job Expected Delay")
plt.title("Job Expected Delay vs Arrival Rate")
plt.grid(True)
plt.show()
