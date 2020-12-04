"""

"""
import pytest
from collections import defaultdict

class Ticket:
    
    def __init__(self, id: int, station_name: str, time: str):
        
        self.id = id
        self.station_name = station_name
        self.time = time
        
    def __repr__(self):
        
        return f"Ticket({self.id}, {self.station_name}, {self.time})"
    
    
class UndergroundSystem:
    
    def __init__(self):
        
        self.check_ins = defaultdict(list)
        self.check_outs = defaultdict(list)
        
        
    def buy_ticket(self, id: int, station_name: str, time: str) -> Ticket:
        return Ticket(id, station_name, time)
    
    
    def make_checkout_ticket(self, id: int, station_name: str, time: str) -> Ticket:
        return Ticket(id, station_name, time)
        
    
    def check_in(self, station_name: str, ticket: Ticket):
        self.check_ins[station_name].append(ticket)
    
    
    def check_out(self, station_name: str, ticket: Ticket):

        self.check_outs[station_name].append(ticket)
        
        
    def get_average(self, start_station: str, end_station: str) -> int:
        
        start_check_ins = self.check_ins[start_station]
        end_check_outs = self.check_outs[end_station]
        
        if len(start_check_ins) < 2:
            if end_check_outs[0].id == start_check_ins[0].id:
                return (end_check_outs[0].time - start_check_ins[0].time)
            return None
        else:
            all_averages = []
            for i in range(len(start_check_ins)):
                for j in range(len(end_check_outs)):
                    if start_check_ins[i].id == end_check_outs[j].id:
                        start, finish = start_check_ins[i].time, end_check_outs[j].time
                        total = finish - start
                
                        all_averages.append(total)
                
            return sum(all_averages) / len(all_averages)
            
            
            
################################################################

if __name__ == "__main__":
    
    system = UndergroundSystem()
    
    ticket1 = system.buy_ticket(45, "Leyton", 3)
    system.check_in("Leyton", ticket1)
    
    ticket2 = system.buy_ticket(32, "Paradise", 8)
    system.check_in("Paradise", ticket2)
    
    ticket3 = system.buy_ticket(27, "Leyton", 10)
    system.check_in("Leyton", ticket3)
    
    ticket4 = system.make_checkout_ticket(45, "Waterloo", 15)
    system.check_out("Waterloo", ticket4)
    
    ticket5 = system.make_checkout_ticket(27, "Waterloo", 20)
    system.check_out("Waterloo", ticket5)
    
    ticket6 = system.make_checkout_ticket(32, "Cambridge", 22)
    system.check_out("Cambridge", ticket6)
    
    print(system.check_ins)
    print()
    print(system.check_outs)
    print()
    
    print(system.get_average("Paradise", "Cambridge"))
    print(system.get_average("Leyton", "Waterloo"))
        
    