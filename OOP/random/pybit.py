# https://pybit.es/codechallenge20.html
from typing import List
from datetime import datetime

class Session:

    def __init__(self, 
        speaker, # speaker obj
        location: str, #"November-12-2020"
        date: str, 
        topics: List[str], 
        start_time_est: str, #13:30
        end_time_est: str):
        
        self.speaker = speaker
        self.location = location
        self.date = datetime.strptime(date, "%B-%d-%Y").date()
        self.topics = topics
        self.start_time_est = datetime.strptime(start_time_est, "%H:%M").time()
        self.end_time_est = datetime.strptime(end_time_est, "%H:%M").time()


session = Session("Nick", "Gym", "November-12-2020", ["Python", "Data Science"], "13:30", "14:30")

print(session.date)
print(session.start_time_est)