
class ModelBasedReflexAgent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.previous_action = None 

    def sensor(self, current_temp):
        self.current_temp = current_temp

    def performance(self):
        # Decision logic
        if self.current_temp < self.desired_temp:
            action = "Turn ON the Heater"
        elif self.current_temp > self.desired_temp:
            action = "Turn OFF the Heater"
        else:
            action = "Do Nothing"

        # Avoid repeating same unnecessary action
        if action == self.previous_action:
            action = "No Change (Keep previous state)"
        else:
            self.previous_action = action

        return action

    def actuator(self, room_name):
        action = self.performance()
        print(f"{room_name} | Current Temp: {self.current_temp}°C → Action: {action}")
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 25,
    "Study Room": 20
}

# Desired temperature = 22°C
agent = ModelBasedReflexAgent(22)

print("=== Model-Based Reflex Agent: Smart Home Temperature Control ===\n")

for room, temp in rooms.items():
    agent.sensor(temp)
    agent.actuator(room)
