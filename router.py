class Router:
    def __init__(self, name, routing_table):
        self.name = name
        self.routing_table = routing_table

    def route(self, packet):
        packet.log_hop(self.name)
        if packet.dest in self.routing_table:
            next_hop = self.routing_table[packet.dest]
            return next_hop
        return None
