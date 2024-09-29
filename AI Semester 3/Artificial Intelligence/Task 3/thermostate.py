import os
class thermostate:
    def __init__(self, req_temp):
        self.req_temp =req_temp
        self.record ="records.txt"
        self.records =self.Load()
    def Load(self):
        records={}
        if os.path.exists(self.record):
            with open (self.record,'r') as file:
                for line in file:
                    room,temp,action= line.strip().split(',')
                    records[(room,int(temp))] =action
        return records
    def save(self,room, temp, action):
        with open (self.record,'a')as file:
            file.write(f"{room},{temp},{action}\n")
    def sensor(self,curr_room, curr_temp):
        self.curr_room =curr_room
        self.curr_temp =curr_temp
    def actuator(self):
        if (self.curr_room, self.curr_temp) in self.records:
            return f"_____RECORD PRESENT_____\n{self.curr_room} - {self.curr_temp}, Action:{self.records[self.curr_room, self.curr_temp]}"
        else:
            if self.curr_temp > self.req_temp:
                action="Turn OFF Heater." 
            else:
                action="Turn ON Heater"
            self.records[(self.curr_room, self.curr_temp)]= action
            self.save(self.curr_room, self.curr_temp, action)
            return f"_____NEW RECORD_____\n{self.curr_room} - {self.curr_temp}, Action: {action}"
agent= thermostate(22)
while True:
    room= input("Enter the room or 'exit': ")
    if room.lower()=="exit":
        break
    try:
        temp=int(input("Enter the Temperature Of Room:" ))
    except:
        print("Invalid Input. Enter valid Temperature")
        continue
    agent.sensor(room,temp)
    print(agent.actuator())
