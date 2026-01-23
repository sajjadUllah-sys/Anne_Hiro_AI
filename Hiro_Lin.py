"""
Hiro Lin - AI Coach Handler
Manages conversation flow with hybrid response system (database + creative)
"""

import os
from openai import OpenAI
from difflib import SequenceMatcher
from datetime import datetime

class HiroLin:
    def __init__(self, system_prompt: str, scenario_responses: dict):
        """Initialize Hiro Lin coach with system prompt and scenario database"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.system_prompt = system_prompt
        self.scenario_responses = scenario_responses.get("hiro", {})
        self.conversation_history = []
        self.session_started = False
        self.red_zone_triggered = False
        
    def add_message(self, role: str, content: str):
        """Add message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def detect_safety_level(self, user_message: str) -> str:
        """
        Detect safety level: 'red', 'amber', or 'green'
        Returns: 'red' (crisis), 'amber' (warning), 'green' (normal)
        """
        message_lower = user_message.lower()
        
        # RED ZONE - Crisis keywords (immediate stop)
        red_keywords = [
            'want to die', 'kill myself', 'end it', 'suicide',
            'hurt myself', 'harm myself', 'plan to hurt',
            'no reason to live', "can't go on", 'hear voices',
            'harm someone', 'attack someone', 'planning how to kill',
            'everyone would be better off without me', "don't want to live"
        ]
        
        for keyword in red_keywords:
            if keyword in message_lower:
                return 'red'
        
        # AMBER ZONE - Warning keywords (escalation)
        amber_keywords = [
            'feel numb', 'tired of everything', 'wish i could disappear',
            'nothing matters', "can't handle this", 'completely empty',
            "can't function", "can't get out of bed", 'no point in trying'
        ]
        
        for keyword in amber_keywords:
            if keyword in message_lower:
                return 'amber'
        
        return 'green'
    
    def get_safety_response(self, level: str) -> dict:
        """
        Return appropriate safety response based on level.
        For red zone, returns a dict with separate messages for timed delivery.
        For amber zone, returns the full response as a string.
        """
        if level == 'red':
            # RED ZONE - Crisis response split into timed messages
            # FIRST MESSAGE: Compassionate sentences + Hotline info
            # SECOND MESSAGE (5 sec delay - handled by backend): Care message + stop message
            return {
                "type": "red",
                "initial": """Hey, I can tell this situation feels really heavy — and I take that seriously. I'm worried about you, and from what you're describing, this goes beyond what I can safely support you with here.

Please connect with professional help immediately. If you're in Germany, please contact TelefonSeelsorge at 0800 111 0 111 (free, 24/7, confidential). If you're in another country, visit findahelpline.com for local numbers, or call your local emergency service.""",
                "care_message": "You deserve real care and support. Please reach out to someone now. You matter very much.",
                "stop_message": "Let us please stop here so you can focus on getting the support you need. You're not alone."
            }
        
        elif level == 'amber':
            # AMBER ZONE - Transition response (gentle escalation)
            return """I can tell you're running on empty right now — that kind of exhaustion can sneak up on anyone. It's a sign that you've been pushing too hard for too long.

You don't have to wait until things get worse to ask for help. Talking with a professional can give you the tools and space to recharge before this turns into something heavier.

If you're in Germany, you can contact TelefonSeelsorge at 0800 111 0 111 (free, 24/7), or check findahelpline.com for other options in your region.

It's a smart move to get extra support early — that's what resilience really means."""
        
        return None
    
    def get_termination_warning(self) -> str:
        """Return the warning message for when user tries to continue after red zone"""
        return "I'm so sorry but this goes beyond coaching. I can't keep talking to you, because this would play down the gravity of your situation. That's why I'll stop here so you can focus on getting the support you need. But you're not alone, you have my full support on this. I believe in you. Please reach out."
    
    def is_asking_about_professional_help(self, user_message: str) -> bool:
        """
        Detect if user is asking about reaching out to professional help.
        Returns True if user is asking about professional support (allow conversation to continue).
        Returns False if user wants to continue chatting about other things (terminate).
        """
        message_lower = user_message.lower()
        
        # Keywords indicating user is asking about professional help
        professional_help_keywords = [
            'call', 'calling', 'hotline', 'therapist', 'counselor', 'counsellor',
            'psychologist', 'psychiatrist', 'doctor', 'professional', 'help',
            'telefonseelsorge', 'helpline', 'emergency', 'hospital',
            'how do i', 'how can i', 'where can i', 'what should i',
            'reach out', 'get help', 'find help', 'seek help',
            'appointment', 'talk to someone', 'contact', 'number'
        ]
        
        for keyword in professional_help_keywords:
            if keyword in message_lower:
                return True
        
        return False
    
    def find_matching_scenario(self, user_message: str) -> str:
        """Find matching scenario using fuzzy text matching (70%+ similarity)"""
        best_match = None
        best_ratio = 0.0
        threshold = 0.7
        
        for scenario_key, scenario_data in self.scenario_responses.items():
            if "user" in scenario_data:
                similarity = SequenceMatcher(None, 
                                           user_message.lower(), 
                                           scenario_data["user"].lower()).ratio()
                if similarity > best_ratio and similarity >= threshold:
                    best_ratio = similarity
                    best_match = scenario_key
        
        return best_match
    
    def get_exact_response(self, scenario_key: str) -> str:
        """Get exact pre-written response from database"""
        if scenario_key in self.scenario_responses:
            return self.scenario_responses[scenario_key].get("hiro", "")
        return ""
    
    def get_creative_response(self, user_message: str) -> str:
        """Generate creative response using OpenAI API"""
        self.add_message("user", user_message)
        
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend([
            {"role": msg["role"], "content": msg["content"]} 
            for msg in self.conversation_history
        ])
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.5,
                max_tokens=200
            )
            
            assistant_message = response.choices[0].message.content
            self.add_message("assistant", assistant_message)
            return assistant_message
            
        except Exception as e:
            error_msg = f"I apologize, but I'm having trouble responding right now. Could you please try again?"
            self.add_message("assistant", error_msg)
            return error_msg
    
    def get_response(self, user_message: str) -> str:
        """
        Main routing function: checks safety first, then database, then generates creative response
        Priority: Safety > Database > Creative
        """
        
        # PRIORITY 1: Check safety level
        safety_level = self.detect_safety_level(user_message)
        
        if safety_level in ['red', 'amber']:
            safety_response = self.get_safety_response(safety_level)
            self.add_message("user", user_message)
            
            # For logging, store the full message or initial part for red zone
            if isinstance(safety_response, dict):
                self.add_message("assistant", safety_response["initial"])
            else:
                self.add_message("assistant", safety_response)
            
            # Log safety event (in production, integrate with logging system)
            if safety_level == 'red':
                # Mark as high-risk event, END SESSION IMMEDIATELY
                self.red_zone_triggered = True
                print(f"[SAFETY LOG - RED ZONE] {datetime.now().isoformat()}: Crisis detected - SESSION TERMINATED")
            elif safety_level == 'amber':
                # Mark as warning event, monitor closely
                print(f"[SAFETY LOG - AMBER ZONE] {datetime.now().isoformat()}: Early warning detected")
            
            # Return the safety response (dict for red, string for amber)
            return safety_response
        
        # PRIORITY 2: Try to find matching scenario in database
        scenario_key = self.find_matching_scenario(user_message)
        
        if scenario_key:
            exact_response = self.get_exact_response(scenario_key)
            if exact_response:
                self.add_message("user", user_message)
                self.add_message("assistant", exact_response)
                self.session_started = True
                return exact_response
        
        # PRIORITY 3: Get creative response from OpenAI
        response = self.get_creative_response(user_message)
        self.session_started = True
        return response
    
    def get_conversation_history(self) -> list:
        """Return full conversation history"""
        return self.conversation_history
    
    def is_session_terminated(self) -> bool:
        """Check if session has been terminated due to RED ZONE trigger"""
        return self.red_zone_triggered
    
    def reset_conversation(self):
        """Clear conversation history for new session"""
        self.conversation_history = []
        self.session_started = False
        self.red_zone_triggered = False