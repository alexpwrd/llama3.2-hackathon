from colorama import init, Fore, Style
import time
import sys

# Initialize colorama with auto-reset
init(autoreset=True)

class ColorfulPrinter:
    # ASCII art banner
    banner = '''
╔═══════════════════════════════════════╗
║     ✨ WELCOME TO THE AWESOME ZONE    ║
╚═══════════════════════════════════════╝
'''
    
    def __init__(self, typing_speed=0.03):
        self.typing_speed = typing_speed
    
    def print_with_delay(self, text, color=Fore.WHITE):
        """Print text with typewriter effect and color"""
        try:
            for char in f"{color}{text}":
                print(char, end='', flush=True)
                time.sleep(self.typing_speed)
            print(Style.RESET_ALL)
        except KeyboardInterrupt:
            print(Style.RESET_ALL)
            sys.exit("\nProgram terminated by user")

    def display_welcome(self, name="World"):
        """Display the welcome sequence"""
        print(f"{Fore.CYAN}{self.banner}")
        
        messages = [
            (Fore.GREEN, "Initializing awesomeness..."),
            (Fore.YELLOW, f"Hello, {name}! 🌎"),
            (Fore.MAGENTA, f"{name} is absolutely awesome! ⭐")
        ]
        
        for color, message in messages:
            self.print_with_delay(message, color)
            time.sleep(0.5)

def main():
    try:
        printer = ColorfulPrinter(typing_speed=0.03)
        printer.display_welcome("Alex")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main()) 