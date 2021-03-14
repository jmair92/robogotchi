import random


class Numbers:
    def __init__(self):
        self.my_wins = 0
        self.robot_wins = 0
        self.draws = 0
        self.nbr_min = 0
        self.nbr_max = 1000000

    def read_input(self):
        while True:
            print("What is your number?")
            choice = input()
            print()
            try:
                choice = int(choice)
                if choice < self.nbr_min:
                    print("The number can't be negative!")
                    continue
                if choice > self.nbr_max:
                    print(f"Invalid input! The number can't be bigger than {self.nbr_max}.")
                    continue
                return choice

            except ValueError:
                if choice == "exit game":
                    return -1
                print("A string is not a valid input!")

    def choose_winner(self, your_choice):
        robot_choice = random.randint(self.nbr_min, self.nbr_max)
        print(f"The robot entered the number {robot_choice}.")

        goal_number = random.randint(self.nbr_min, self.nbr_max)
        print(f"The goal number is {goal_number}")

        if abs(goal_number - your_choice) < abs(goal_number - robot_choice):
            self.my_wins += 1
            print("You won!")
        elif abs(goal_number - your_choice) > abs(goal_number - robot_choice):
            self.robot_wins += 1
            print("The robot won!")
        else:
            self.draws += 1
            print("It's a draw!")
        print()

    def print_stats(self):
        print(f"You won: {self.my_wins},")
        print(f"The robot won: {self.robot_wins},")
        print(f"Draws: {self.draws}.")

    def run(self):
        while True:
            choice = self.read_input()
            if choice == -1:
                self.print_stats()
                break
            self.choose_winner(choice)


class RockPaperScissor:

    def __init__(self):
        self.my_wins = 0
        self.robot_wins = 0
        self.draws = 0

    def read_input(self):
        while True:
            print("What is your move?\n")
            choice = input()
            choice = choice.lower()

            if choice == "rock" or choice == "paper" or choice == "scissors":
                return choice
            elif choice == "exit game":
                return -1
            else:
                print("No such option! Try again!")
                continue

    def choose_winner(self, choice):
        robot_choice = random.randint(1, 3)
        winner = ""
        if robot_choice == 1:
            print("The robot chose rock\n")
            if choice == "rock":
                winner = "It's a draw!"
            elif choice == "paper":
                winner = "You won!"
            else:
                winner = "The robot won!!"
        elif robot_choice == 2:
            print("The robot chose paper\n")
            if choice == "rock":
                winner = "The robot won!!"
            elif choice == "paper":
                winner = "It's a draw!"
            else:
                winner = "You won!"
        else:
            print("The robot chose scissors\n")
            if choice == "rock":
                winner = "You won!"
            elif choice == "paper":
                winner = "The robot won!!"
            else:
                winner = "Its a draw!"
        if winner == "It's a draw!":
            self.draws += 1
        elif winner == "The robot won!!":
            self.robot_wins += 1
        else:
            self.my_wins += 1
        print(winner + "\n")

    def print_stats(self):
        print(f"You won: {self.my_wins},")
        print(f"The robot won: {self.robot_wins},")
        print(f"Draws: {self.draws}.")

    def run(self):
        while True:
            choice = self.read_input()
            if choice == -1:
                self.print_stats()
                break
            self.choose_winner(choice)

class Robot:

    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0
        self.rust = 0
        self._games = {"numbers": Numbers, "rock-paper-scissors": RockPaperScissor}
        self._rust_events = {
            0: None,
            10: f"Oh no, {self.name} stepped into a puddle!",
            30: f"Oh, {self.name} encountered a sprinkler!",
            50: f"Guess what! {self.name} fell into the pool!",
        }

    def play(self):
        choice = input("Which game would you like to play? ").lower()
        while choice not in self._games:
            choice = input(
                "\nPlease choose a valid option: Numbers or Rock-paper-scissors? "
            ).lower()
        if choice == "numbers":
            game = Numbers()
            game.run()
        elif choice == "rock-paper-scissors":
            game = RockPaperScissor()
            game.run()

        previous_boredom = self.boredom
        previous_overheat = self.overheat
        previous_rust = self.rust
        if self.boredom < 20:
            self.boredom = 0
        else:
            self.boredom -= 20
        self.overheat += 10
        print()
        rust = self.unpleasant_event()
        if rust:
            print(self._rust_events[rust])
            self.rust += rust
        print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom}.")
        print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat}.")
        if rust:
            print(f"{self.name}'s level of rust was {previous_rust}. Now it is {self.rust}")
        if self.boredom == 0:
            print(f"{self.name} is in a great mood!")


    def recharge(self):
        if self.battery == 100:
            print(f"{self.name} is charged!")
        else:
            previous_battery = self.battery
            previous_overheat = self.overheat
            previous_boredom = self.boredom
            self.boredom += 5
            self.battery += 10
            if self.overheat != 0:
                self.overheat -= 5
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat}.")
            print(f"{self.name}'s level of the battery was {previous_battery}. Now it is {self.battery}.")
            print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom}.")
            print()
            print(f"{self.name} is recharged!")

    def sleep(self):
        if self.overheat == 0:
            print(f"{self.name} is cool!")
        else:
            previous_overheat = self.overheat
            if self.overheat < 20:
                self.overheat = 0
            else:
                self.overheat -= 20
            if self.overheat != 0:
                print(f"{self.name} cooled off!\n")
            else:
                print(f"{self.name} is cool!")
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat}.\n")

    def info(self):
        print(f"{self.name}'s stats are:")
        print(f"battery is {self.battery},")
        print(f"overheat is {self.overheat},")
        print(f"skill level is {self.skills},")
        print(f"boredom is {self.boredom},")
        print(f"rust is {self.rust}.")
        print()

    def exit(self):
        print(f"Game over.")
        exit()

    def menu(self):
        options = ["exit", "info", "recharge", "sleep", "play", "oil", "work", "learn"]
        while True:
            print(f"Available interactions with {self.name}:")
            print("exit – Exit")
            print("info – Check the vitals")
            print("work – Work")
            print("play – Play")
            print("oil – Oil")
            print("recharge – Recharge")
            print("sleep – Sleep mode")
            print("learn – Learn skills")
            print()
            print("Choose:")
            choice = input()
            print()
            if choice in options:
                return choice
            else:
                print("Invalid input, try again!")
                print()
                continue

    def learn(self):
        if self.skills == 100:
            print(f"There's nothing for {self.name} to learn!")
        else:
            previous_skill = self.skills
            previous_overheat = self.overheat
            previous_battery = self.battery
            previous_boredom = self.boredom
            self.skills += 10
            if self.battery < 10:
                self.battery = 0
            else:
                self.battery -= 10
            self.overheat += 10
            self.boredom += 5
            print(f"{self.name}'s level of skill was {previous_skill}. Now it is {self.skills}.")
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat}.")
            print(f"{self.name}'s level of the battery was {previous_battery}. Now it is {self.battery}.")
            print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom}.")
            print(f"{self.name} has become smarter!\n")

    def work(self):
        if self.skills < 50:
            print(f"{self.name} has got to learn before working!")
        else:
            previous_overheat = self.overheat
            previous_battery = self.battery
            previous_boredom = self.boredom
            previous_rust = self.rust
            if self.battery < 10:
                self.battery = 0
            else:
                self.battery -= 10
            self.overheat += 10
            self.boredom += 10
            print()
            print(f"{self.name} did well!")
            print(f"{self.name}'s level of boredom was {previous_boredom}. Now it is {self.boredom}.")
            print(f"{self.name}'s level of overheat was {previous_overheat}. Now it is {self.overheat}.")
            print(f"{self.name}'s level of the battery was {previous_battery}. Now it is {self.battery}.")
            rust = self.unpleasant_event()
            if rust:
                self.rust += rust
                print(f"{self.name}'s level of rust was {previous_rust}. Now it is {self.rust}")
                print(self._rust_events[rust])


    def unpleasant_event(self):
        rust = random.choice(list(self._rust_events))
        return rust

    def oil(self):
        if self.rust == 0:
            print(f"{self.name} is fine, no need to oil!")
        else:
            previous_rust = self.rust
            if self.rust < 20:
                self.rust = 0
            else:
                self.rust -= 20
            print(f"{self.name}'s level of rust was {previous_rust}. Now it is {self.rust}. "
                  f"{self.name} is less rusty!")


def main():
    print("How will you call your robot?")
    name = input()
    print()
    robot = Robot(name)
    while True:
        if robot.overheat > 100:
            print(f"The level of overheat reached 100, {robot.name} has blown up! Game over. Try again?")
            exit()
        elif robot.rust > 100:
            print(f"{robot.name} is too rusty! Game over. Try again?")
            exit()
        choice = robot.menu()
        if robot.battery == 0 and choice != "recharge":
            print(f"The level of the battery is 0, {robot.name} needs recharging!\n")
            continue
        elif robot.boredom == 100 and choice != "play":
            print(f"{robot.name} is too bored! {robot.name} needs to have fun!\n")
            continue
        if choice == "exit":
            robot.exit()
        elif choice == "info":
            robot.info()
        elif choice == "recharge":
            robot.recharge()
        elif choice == "sleep":
            robot.sleep()
        elif choice == "play":
            robot.play()
        elif choice == "work":
            robot.work()
        elif choice == "learn":
            robot.learn()
        elif choice == "oil":
            robot.oil()



if __name__ == '__main__':
    main()
