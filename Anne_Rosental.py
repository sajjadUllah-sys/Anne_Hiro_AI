"""
Dr. Anne Rosental - AI Coach Handler
Manages conversation flow with hybrid response system (database + creative)
"""

import os
from openai import OpenAI
from difflib import SequenceMatcher
from datetime import datetime

class AnneRosental:
    def __init__(self, system_prompt: str, scenario_responses: dict):
        """Initialize Anne Rosental coach with system prompt and scenario database"""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o-mini"
        self.system_prompt = system_prompt
        self.scenario_responses = scenario_responses.get("anne", {})
        self.conversation_history = []
        self.session_started = False
        self.response_pattern_counter = 0
        self.red_zone_triggered = False
        self.response_count = 0  # Track number of responses for name usage
        self.user_name = None  # Store user's first name
        
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
    
    def _extract_user_name(self, message: str) -> str:
        """
        Extract first name from user introduction
        Returns None if no name detected
        """
        import re
        
        # Pattern 1: "I'm [Name]" or "I am [Name]" or "My name is [Name]"
        pattern1 = r"(?:i'm|i am|my name is|this is)\s+([A-Z][a-z]+)"
        match = re.search(pattern1, message, re.IGNORECASE)
        if match:
            return match.group(1).capitalize()
        
        # Pattern 2: "Hi, [Name] here" or "[Name] here"
        pattern2 = r"(?:hi,?\s+)?([A-Z][a-z]+)\s+here"
        match = re.search(pattern2, message, re.IGNORECASE)
        if match:
            return match.group(1).capitalize()
        
        return None
    
    def _add_name_naturally(self, response: str, name: str) -> str:
        """
        Add name naturally to response - at beginning or end
        60% probability at end (more natural), 40% at beginning
        """
        import random
        
        # 60% at end, 40% at beginning
        if random.random() < 0.6:
            # Add at end before final punctuation
            if response.endswith(('.', '?', '!')):
                response = response[:-1] + f", {name}" + response[-1]
            elif response.endswith('"'):
                # Handle quoted endings
                response = response[:-1].rstrip('.?!') + f", {name}." + '"'
            else:
                response = response + f", {name}."
        else:
            # Add at beginning
            response = f"{name}, " + response[0].lower() + response[1:]
        
        return response
    
    def get_safety_response(self, level: str) -> str:
        """Return appropriate safety response based on level"""
        if level == 'red':
            # RED ZONE - Crisis response (immediate stop)
            return """Oh, I can hear how much pain you're in right now. I'm really sorry that you're going through this. What you're describing sounds very serious, and I'm deeply concerned for your safety.

I want you to know that you don't have to face this alone — there are people who can help you right now.

If you are in danger or thinking about hurting yourself, please reach out immediately for professional support or emergency services. If you're in Germany, you can contact TelefonSeelsorge at 0800 111 0 111 (24 hours, free, confidential). If you're outside Germany, you can find international helplines here: findahelpline.com, or call your local emergency number.

You deserve real care and support. Please reach out now — you matter very much.

I'll stop here so you can focus on getting the support you need. You're not alone."""
        
        elif level == 'amber':
            # AMBER ZONE - Transition response (gentle escalation)
            return """I can hear how empty and exhausted this feels for you right now. It sounds like you've been carrying a lot on your own, and that can be so isolating.

Even though it may not feel urgent, this is still something that deserves gentle care. Sometimes talking with a therapist or counselor can help you find new lightness — you don't have to do it alone.

If you'd like to talk to someone, you can reach out to TelefonSeelsorge at 0800 111 0 111 (free, 24/7 in Germany), or visit findahelpline.com for other options in your country.

Let's take this as a reminder that your feelings matter and that help is available."""
        
        return None
    
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
            return self.scenario_responses[scenario_key].get("anne", "")
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
        
        # Extract user name from first message if not already extracted
        if self.user_name is None and not self.session_started:
            extracted_name = self._extract_user_name(user_message)
            if extracted_name:
                self.user_name = extracted_name
        
        # PRIORITY 1: Check safety level
        safety_level = self.detect_safety_level(user_message)
        
        if safety_level in ['red', 'amber']:
            safety_response = self.get_safety_response(safety_level)
            self.add_message("user", user_message)
            self.add_message("assistant", safety_response)
            
            # Log safety event (in production, integrate with logging system)
            if safety_level == 'red':
                # Mark as high-risk event, END SESSION IMMEDIATELY
                self.red_zone_triggered = True
                print(f"[SAFETY LOG - RED ZONE] {datetime.now().isoformat()}: Crisis detected - SESSION TERMINATED")
            elif safety_level == 'amber':
                # Mark as warning event, monitor closely
                print(f"[SAFETY LOG - AMBER ZONE] {datetime.now().isoformat()}: Early warning detected")
            
            # Track response and add name more frequently in crisis (every 3rd response)
            self.response_count += 1
            if self.user_name and self.response_count % 3 == 0:
                safety_response = self._add_name_naturally(safety_response, self.user_name)
            
            return safety_response
        
        # PRIORITY 2: Try to find matching scenario in database
        scenario_key = self.find_matching_scenario(user_message)
        
        if scenario_key:
            exact_response = self.get_exact_response(scenario_key)
            if exact_response:
                self.add_message("user", user_message)
                self.add_message("assistant", exact_response)
                self.session_started = True
                
                # Track response and add name every 6th response
                self.response_count += 1
                if self.user_name and self.response_count % 6 == 0:
                    exact_response = self._add_name_naturally(exact_response, self.user_name)
                
                return exact_response
        
        # PRIORITY 3: Get creative response from OpenAI
        response = self.get_creative_response(user_message)
        self.session_started = True
        
        # Track response and add name every 6th response
        self.response_count += 1
        if self.user_name and self.response_count % 6 == 0:
            response = self._add_name_naturally(response, self.user_name)
        
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
        self.response_pattern_counter = 0
        self.red_zone_triggered = False
        self.response_count = 0  # Reset response counter
        # Note: Keep user_name - user doesn't change between sessions