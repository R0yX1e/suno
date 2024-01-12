import server_api

min_credits = 5 # price

class Account_manager:
    def __init__(self, Account, credits):
        self.id = Account.email
        self.credits = credits
        self.active_tasks = 0  # Initialize active tasks to zero

    def can_accept_task(self, min_credits):
        # Account can accept a task 0 if credits is above minimum and active tasks are less than 10
        return self.credits >= min_credits and self.active_tasks < 10

    def add_task(self):
        # Increment active tasks count
        if self.can_accept_task(min_credits):  # Check if account can accept another task
            self.active_tasks += 1
            return True
        return False

    def complete_task(self):
        # Decrement active tasks count
        if self.active_tasks > 0:
            self.active_tasks -= 1
        credits -= min_credits