import os
class thermostate:
    def __init__(self, desired_temp):
        self.desired_temp =desired_temp
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
    def sensor(self,current_room, current_temp):
        self.current_room =current_room
        self.current_temp =current_temp
    def actuator(self):
        if (self.current_room, self.current_temp) in self.records:
            return f"_____RECORD PRESENT_____\n{self.current_room} - {self.current_temp}, Action:{self.records[self.current_room, self.current_temp]}"
        else:
            if self.current_temp > self.desired_temp:
                action= "Turn OFF Heater." 
            else:
                action="Turn ON Heater"
            self.records[(self.current_room, self.current_temp)]= action
            self.save(self.current_room, self.current_temp, action)
            return f"_____NEW RECORD_____\n{self.current_room} - {self.current_temp}, Action: {action}"
agent1= thermostate(22)
while True:
    room= input("Enter the room or 'exit': ")
    if room.lower()== "exit":
        break
    try:
        temp= int(input("Enter the Temperature Of Room:" ))
    except:
        print("Invalid Input. Enter valid Temperature")
        continue
    agent1.sensor(room,temp)
    print(agent1.actuator())
