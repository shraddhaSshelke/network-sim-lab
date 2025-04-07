class Packet:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.path = []

    def log_hop(self, router_name):
        self.path.append(router_name)

    def __str__(self):
        return f"Packet from {self.src} to {self.dest} via {self.path}"
