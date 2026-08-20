from collections import deque


class TaskScheduler:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, name, condition):
        self.tasks.append((name, condition))
        print(f"Task '{name}' added.")

    def run_tasks(self, value):
        print("\nChecking tasks...")

        remaining = deque()

        while self.tasks:
            name, condition = self.tasks.popleft()

            # Lazy evaluation:
            # condition is evaluated only when needed
            if condition(value):
                print(f"✓ Executing: {name}")
            else:
                print(f"⏳ Condition not met: {name}")
                remaining.append((name, condition))

        self.tasks = remaining


def main():
    scheduler = TaskScheduler()

    while True:
        print("\n===== Task Scheduler =====")
        print("1. Add task")
        print("2. Run tasks")
        print("3. Show pending tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")

            threshold = int(input("Run task when value >=: "))

            # Lambda delays the condition until run_tasks()
            condition = lambda value, t=threshold: value >= t

            scheduler.add_task(name, condition)

        elif choice == "2":
            value = int(input("Enter current value: "))

            # Nested conditional logic
            if value < 0:
                print("Invalid value.")
            elif value == 0:
                print("Value is zero.")
            else:
                scheduler.run_tasks(value)

        elif choice == "3":
            if scheduler.tasks:
                print("\nPending tasks:")
                for name, _ in scheduler.tasks:
                    print("-", name)
            else:
                print("No pending tasks.")

        elif choice == "4":
            print("Exiting scheduler...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
