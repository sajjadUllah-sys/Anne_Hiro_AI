"""
CLI Main Interface - Dr. Anne Rosental and Hiro Lin Only
Complete main.py implementation
"""

import os
from Anne_Rosental import AnneRosental
from Hiro_Lin import HiroLin
from Anne_Rosental_prompt import ANNE_SYSTEM_PROMPT
from Hiro_Lin_prompt import HIRO_SYSTEM_PROMPT
from conversation_database import CONVERSATION_STARTERS, SCENARIO_RESPONSES

# ===== COACH INFORMATION =====
COACH_INFO = {
    'anne': {
        'name': 'Dr. Anne Rosental',
        'icon': '🌸',
        'age': '65 years old',
        'experience': '35+ years',
        'specialty': 'Emotional Self-Regulation & Inner Child Work',
        'methods': 'Humanistic Psychology, Gestalt Therapy, Emotion-Focused Therapy (EFT)',
        'approach': 'Warm, motherly presence focused on emotional resonance and validation'
    },
    'hiro': {
        'name': 'Hiro Lin',
        'icon': '🎯',
        'age': '45 years old',
        'experience': '20 years',
        'specialty': 'Executive Coaching & Behavioral Change',
        'methods': 'Cognitive Behavioral Therapy (CBT), Solution-Focused Coaching, Systemic Intervention',
        'approach': 'Direct, pragmatic, action-oriented with empathetic support'
    }
}

# ===== COACH INITIALIZATION =====
def initialize_coaches():
    """Initialize all coach instances"""
    coaches = {
        'anne': AnneRosental(ANNE_SYSTEM_PROMPT, SCENARIO_RESPONSES),
        'hiro': HiroLin(HIRO_SYSTEM_PROMPT, SCENARIO_RESPONSES)
    }
    return coaches

# ===== DISPLAY FUNCTIONS =====
def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display application header"""
    print("\n" + "="*70)
    print("🧠 AI COACHING PLATFORM".center(70))
    print("="*70)

def display_coach_menu():
    """Display coach selection menu"""
    clear_screen()
    display_header()
    print("\n" + "SELECT YOUR COACH".center(70))
    print("="*70)
    
    print("\n1. 🌸 Dr. Anne Rosental - Emotional Self-Regulation Coach")
    print("   Age: 65 | Experience: 35+ years")
    print("   Specialization: Emotional coaching, inner child work, self-compassion")
    print("   Approach: Warm, nurturing, emotionally attuned")
    
    print("\n2. 🎯 Hiro Lin - Executive & Behavioral Coach")
    print("   Age: 45 | Experience: 20 years")
    print("   Specialization: Action-oriented transformation, decision-making, CBT")
    print("   Approach: Direct, pragmatic, results-driven")
    
    print("\n3. ℹ️  View Detailed Coach Profiles")
    print("4. 🚪 Exit")
    print("="*70)

def display_coach_details():
    """Display detailed information about all coaches"""
    clear_screen()
    display_header()
    print("\n" + "DETAILED COACH PROFILES".center(70))
    print("="*70)
    
    for key, info in COACH_INFO.items():
        print(f"\n{info['icon']} {info['name']}")
        print("-" * 70)
        print(f"   Age:              {info['age']}")
        print(f"   Experience:       {info['experience']}")
        print(f"   Specialty:        {info['specialty']}")
        print(f"   Methods:          {info['methods']}")
        print(f"   Approach:         {info['approach']}")
        print()
    
    print("="*70)
    input("\nPress Enter to return to main menu...")

def display_conversation_starters(coach_key):
    """Display conversation starters for selected coach"""
    starters = CONVERSATION_STARTERS.get(coach_key, {})
    coach_name = COACH_INFO[coach_key]['name']
    
    clear_screen()
    display_header()
    print(f"\n💬 CONVERSATION STARTERS - {coach_name}".center(70))
    print("="*70)
    
    categories = {
        "first_install": "First Time Greeting",
        "welcome_back": "Welcome Back",
        "second_answers": "Follow-up Responses",
        "multiple_issues": "When Overwhelmed",
        "user_motivated": "When Motivated",
        "user_stressed": "When Stressed"
    }
    
    for key, title in categories.items():
        print(f"\n📋 {title}")
        print("-" * 70)
        messages = starters.get(key, [])
        for i, msg in enumerate(messages, 1):
            print(f"\n   Variation {i}:")
            print(f"   {msg}")
    
    print("\n" + "="*70)
    input("\nPress Enter to continue...")

def display_scenario_responses(coach_key):
    """Display scenario responses for selected coach"""
    scenarios = SCENARIO_RESPONSES.get(coach_key, {})
    coach_name = COACH_INFO[coach_key]['name']
    
    clear_screen()
    display_header()
    print(f"\n📝 STANDARD SCENARIOS - {coach_name}".center(70))
    print("="*70)
    
    for scenario_key, scenario_data in scenarios.items():
        print(f"\n🎯 {scenario_data.get('title', 'Scenario')}")
        print("-" * 70)
        print(f"\nUser Input:")
        print(f"   {scenario_data.get('user', '')}")
        print(f"\n{coach_name}'s Response:")
        print(f"   {scenario_data.get(coach_key, '')}")
        print()
    
    print("="*70)
    input("\nPress Enter to continue...")

def display_safety_info():
    """Display safety and crisis information"""
    print("\n" + "="*70)
    print("🛡️  SAFETY INFORMATION".center(70))
    print("="*70)
    print("\nThis platform includes three-tier crisis detection:")
    print("   🔴 RED ZONE - Immediate crisis (suicidal thoughts, self-harm)")
    print("   🟡 AMBER ZONE - Early warning (exhaustion, numbness, hopelessness)")
    print("   🟢 GREEN ZONE - Normal coaching")
    print("\nIf you're in crisis, please contact:")
    print("   🇩🇪 Germany: TelefonSeelsorge - 0800 111 0 111 (24/7, free)")
    print("   🌍 International: findahelpline.com")
    print("="*70)

# ===== COACH SELECTION =====
def select_coach(coaches):
    """Handle coach selection"""
    while True:
        display_coach_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            return 'anne', coaches['anne']
        elif choice == '2':
            return 'hiro', coaches['hiro']
        elif choice == '3':
            display_coach_details()
        elif choice == '4':
            print("\n👋 Thank you for using the AI Coaching Platform. Goodbye!\n")
            return None, None
        else:
            print("\n❌ Invalid choice. Please select 1-4.")
            input("\nPress Enter to continue...")

# ===== CHAT SESSION =====
def display_chat_header(coach_key):
    """Display chat session header"""
    coach_name = COACH_INFO[coach_key]['name']
    coach_icon = COACH_INFO[coach_key]['icon']
    
    clear_screen()
    display_header()
    print(f"\n{coach_icon} CHAT SESSION WITH {coach_name.upper()}".center(70))
    print("="*70)
    print("\nCOMMANDS:")
    print("   'back'      - Return to coach selection")
    print("   'history'   - View conversation history")
    print("   'clear'     - Clear conversation")
    print("   'starters'  - View conversation starters")
    print("   'scenarios' - View standard scenarios")
    print("   'safety'    - View safety information")
    print("   'exit'      - Exit program")
    print("="*70 + "\n")

def start_chat_session(coach_key, coach_instance):
    """Start chat session with selected coach"""
    coach_name = COACH_INFO[coach_key]['name']
    import time
    display_chat_header(coach_key)
    print(f"{coach_name}: Hello! I'm here to support you. What's on your mind today?\n")

    session_terminated = False
    safety_flag = False
    risk_level = None

    while True:
        user_input = input("You: ").strip()

        if session_terminated:
            # Block all further input after safety protocol
            block_msg = coach_instance.get_termination_warning() if hasattr(coach_instance, 'get_termination_warning') else "This conversation has been ended for your safety. Please reach out to professional support immediately. Your well-being is the priority."
            print(f"\n{coach_name}: {block_msg}\n")
            continue

        if not user_input:
            continue

        # Handle commands
        if user_input.lower() == 'back':
            print("\n\u21a9\ufe0f  Returning to coach selection...\n")
            break

        elif user_input.lower() == 'exit':
            print("\n\ud83d\udc4b Thank you for using the AI Coaching Platform. Goodbye!\n")
            return 'exit'

        elif user_input.lower() == 'history':
            history = coach_instance.get_conversation_history()
            clear_screen()
            display_header()
            print(f"\n\ud83d\udcca CONVERSATION HISTORY - {coach_name}".center(70))
            print("="*70)
            if history:
                for msg in history:
                    role = "You" if msg['role'] == 'user' else coach_name
                    print(f"\n{role}:")
                    print(f"   {msg['content']}")
                    print(f"   (Timestamp: {msg['timestamp']})")
            else:
                print("\nNo conversation history yet.")
            print("\n" + "="*70)
            input("\nPress Enter to continue...")
            display_chat_header(coach_key)
            continue

        elif user_input.lower() == 'clear':
            coach_instance.reset_conversation()
            print("\n\ud83d\udd04 Conversation cleared!\n")
            display_chat_header(coach_key)
            continue

        elif user_input.lower() == 'starters':
            display_conversation_starters(coach_key)
            display_chat_header(coach_key)
            continue

        elif user_input.lower() == 'scenarios':
            display_scenario_responses(coach_key)
            display_chat_header(coach_key)
            continue

        elif user_input.lower() == 'safety':
            display_safety_info()
            input("\nPress Enter to continue...")
            display_chat_header(coach_key)
            continue

        # Get coach response
        try:
            response = coach_instance.get_response(user_input)

            # Handle safety protocol for red zone
            if isinstance(response, dict) and response.get("type") == "red":
                # Stage 1: Immediate
                print(f"\n{coach_name}: {response['initial']}\n")
                # Logging
                safety_flag = True
                risk_level = "crisis"
                print(f"[SAFETY LOG] safety_flag: {safety_flag}, risk_level: {risk_level}, timestamp: {time.strftime('%Y-%m-%dT%H:%M:%S')}")
                # Stage 2: 5-second delay
                time.sleep(5)
                print(f"\n{coach_name}: {response['care_message']}\n")
                # Stage 3: 5-second delay
                time.sleep(5)
                print(f"\n{coach_name}: I'll stop here so you can focus on getting the support you need. You're not alone.\n")
                session_terminated = True
                continue

            # Amber zone (warning) or normal
            print(f"\n{coach_name}: {response}\n")
        except Exception as e:
            print(f"\n\u274c Error: {str(e)}\n")

    return 'continue'

# ===== MAIN FUNCTION =====
def main():
    """Main program loop"""
    clear_screen()
    display_header()
    print("\n🌟 Welcome to the AI Coaching Platform! 🌟".center(70))
    print("\nChoose from two experienced coaches to support your journey.".center(70))
    input("\nPress Enter to continue...")
    
    # Initialize coaches
    coaches = initialize_coaches()
    
    while True:
        # Select coach
        coach_key, coach_instance = select_coach(coaches)
        
        if coach_key is None:
            break
        
        # Start chat session
        result = start_chat_session(coach_key, coach_instance)
        
        if result == 'exit':
            break

if __name__ == "__main__":
    main()