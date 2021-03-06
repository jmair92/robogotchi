class Robot:
    def __init__(self, name, variety):
        self.name = name
        self.variety = variety
        print("Robot")

    def get_info(self):
        return "{} is a {} robot".format(self.name, self.variety)


class ServiceRobot(Robot):
    def __init__(self, name):
        self.name = name
        super().__init__(self.name, 'service')


chappi = ServiceRobot("Chappi")
print(chappi.get_info())
