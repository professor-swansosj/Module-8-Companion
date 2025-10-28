"""
Network Automation ASCII Art Display
Complete the TODO items to create awesome ASCII art!
"""

def display_welcome_art():
    """
    TODO: Create an awesome welcome ASCII art
    Hint: Use triple quotes for multi-line strings
    
    STEP 1: Generate ASCII art using one of these methods:
    - Command line: toilet "YourName" or figlet "YourName" 
    - Online: Visit patorjk.com/software/taag and try fonts like "Big" or "Block"
    - Copy the generated ASCII art and paste it between triple quotes
    
    Example themes: your name, "Docker", "Network", "FSCJ"
    """
    # TODO: Replace 'pass' with your ASCII art from toilet/figlet/online generator
    # Example using figlet "Docker":
    # print("""
    #  ____             _              
    # |  _ \  ___   ___| | _____ _ __ 
    # | | | |/ _ \ / __| |/ / _ \ '__|
    # | |_| | (_) | (__|   <  __/ |   
    # |____/ \___/ \___|_|\_\___|_|   
    # """)
    
    # Or try toilet "Network":  
    # print("""
    # ████   █  ██████ ████████ ██   ██  ███████  ██████  ██   ██
    # ██ ██  █  ██        ██    ██   ██  ██    ██ ██   ██ ██  ██ 
    # ██  ██ █  ████      ██    ██ █ ██  ██    ██ ███████ █████  
    # ██   ███  ██        ██    ██ ███   ██    ██ ██   ██ ██  ██ 
    # ██    ██  ██████    ██     ███ ███  ███████  ██   ██ ██   ██
    # """)
    pass

def display_container_art():
    """
    TODO: Create Docker/container themed ASCII art
    
    STEP 1: Generate "Docker" or "Container" ASCII art:
    - Try: toilet "Docker" or figlet "Container" 
    - Online: Use patorjk.com with fonts like "Slant", "Big", or "Block"
    - Or draw simple ASCII whale (Docker mascot) or shipping container
    """
    # TODO: Add container-themed ASCII art from generator
    # Example with toilet "Docker" -f mono12:
    # print("""
    # ██████   ██████   ██████ ██   ██ ███████ ██████  
    # ██   ██ ██    ██ ██      ██  ██  ██      ██   ██ 
    # ██   ██ ██    ██ ██      █████   █████   ██████  
    # ██   ██ ██    ██ ██      ██  ██  ██      ██   ██ 
    # ██████   ██████   ██████ ██   ██ ███████ ██   ██ 
    # """)
    
    # Or simple whale ASCII:
    # print("""
    #                     ##        .            
    #               ## ## ##       ==            
    #            ## ## ## ##      ===            
    #        /""""""""""""""""___/ ===        
    #   ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
    #        \______ o          __/            
    #         \    \        __/             
    #          \____\______/   
    # """)
    pass

def display_network_art():
    """
    TODO: Create network equipment ASCII art  
    
    STEP 1: Generate "Network" or "Router" ASCII art:
    - Try: toilet "Network" or figlet "Router"
    - Online: Use patorjk.com with your favorite font
    - Or create simple ASCII network diagram
    """
    # TODO: Add network-themed ASCII art from generator
    # Example with figlet "Network":
    # print("""
    # _   _      _                      _    
    #| \ | | ___| |___      _____  _ __| | __
    #|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
    #| |\  |  __/ |_ \ V  V / (_) | |  |   < 
    #|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
    # """)
    
    # Or simple router/switch diagram:
    # print("""
    #     [Router-01]
    #         |
    #     ====+====
    #     |       |
    # [Switch-A] [Switch-B]
    #     |       |
    #   [PC-1]  [PC-2]
    # """)
    pass

def main():
    """Main function - calls all your art functions"""
    print("🎨 Welcome to Network Automation Containers!")
    print("=" * 50)
    
    # TODO: Call your art functions here
    display_welcome_art()
    display_container_art() 
    display_network_art()
    
    print("\n🐳 Container successfully executed!")

if __name__ == "__main__":
    main()