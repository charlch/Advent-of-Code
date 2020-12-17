data = """939
7,13,x,x,59,x,31,19"""
data = """1000509
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,739,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,971,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19"""

first,second = data.split("\n")

start_time = int(first)
buses = [int(i) for i in second.split(",") if i!="x"]

print(start_time, buses)


wait_time = 0
bus_found=False
while not bus_found:
    time = start_time + wait_time

    for bus in buses:
        if time%bus ==0:
            print("Bus",bus, " finished at time ", time, " wait: ", wait_time, " id: ", wait_time*bus)
            bus_found = True
            break;


    wait_time += 1

            
