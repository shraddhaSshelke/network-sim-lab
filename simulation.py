from router import Router
from packet import Packet

# Set up the routers and their routing tables
r1 = Router("R1", {"10.0.0.2": "R2"})
r2 = Router("R2", {"10.0.0.3": "R3"})
r3 = Router("R3", {})

routers = {"R1": r1, "R2": r2, "R3": r3}

# Simulate packet flow
packet = Packet("10.0.0.1", "10.0.0.3")

current_router = "R1"
while current_router:
    next_hop = routers[current_router].route(packet)
    if next_hop:
        current_router = next_hop
    else:
        break

print(packet)
