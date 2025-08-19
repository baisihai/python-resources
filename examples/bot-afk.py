# Purpose:
# This script demonstrates a simple AFK bot that can be used in various applications.
# Note: AFK = Away From Keyboard
#
# This bot will go AFK after 5 seconds of inactivity.
# You can type something to keep it active, or type 'exit' to stop the bot.
#
# Note: This is a simple example and can be improved with more robust error handling and features.
# It can be used as a starting point for more complex bots, and can be extended with more features like logging, notifications, etc.
# It uses threading to check for inactivity.
# The bot can be used in various applications (e.g chat applications, games) where tracking user activity is important.

import time
import threading

class BotAFK:
    def __init__(self, afk_time=5):
        self.afk_time = afk_time
        self.afk = False
        self.last_active = time.time()
        self.check_thread = threading.Thread(target=self.check_afk)
        self.check_thread.start()

    def activity(self):
        """Call this method whenever the bot is active."""
        self.last_active = time.time()
        if self.afk:
            print("Bot is now active.")
            self.afk = False

    def check_afk(self):
        """Check if the bot should go AFK."""
        while True:
            if time.time() - self.last_active > self.afk_time and not self.afk:
                print("Bot is now AFK.")
                self.afk = True
            time.sleep(1)
    
    def is_afk(self):
        """Check if the bot is currently AFK."""
        return self.afk
    
    def stop(self):
        """Stop the AFK check thread."""
        self.check_thread.join()

# Example usage
if __name__ == "__main__":
    bot = BotAFK(afk_time=5)  # Set AFK time to 5 seconds

    while True:
        user_input = input("Type something to keep the bot active (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            bot.stop()
            break
        bot.activity()  # Simulate activity
        print("You typed:", user_input)
        if bot.is_afk():
            print("The bot is currently AFK.")
        else:
            print("The bot is active.")
