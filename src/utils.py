def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("="*60)
    print("    STUDENT GRADE MANAGEMENT SYSTEM".center(60))
    print("         Developed by Rajat - VIT Bhopal".center(60))
    print("="*60)
