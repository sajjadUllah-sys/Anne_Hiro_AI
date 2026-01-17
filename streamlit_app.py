"""
Streamlit App - Dr. Anne Rosental and Hiro Lin Only
Complete streamlit_app.py implementation
"""

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import time
import streamlit as st
from Anne_Rosental import AnneRosental
from Hiro_Lin import HiroLin
from Anne_Rosental_prompt import ANNE_SYSTEM_PROMPT
from Hiro_Lin_prompt import HIRO_SYSTEM_PROMPT
from conversation_database import CONVERSATION_STARTERS, SCENARIO_RESPONSES

# ===== PAGE CONFIGURATION =====
st.set_page_config(
    page_title="AI Coaching Platform",
    page_icon="🧠",
    layout="wide"
)

# ===== SESSION STATE INITIALIZATION =====
# Initialize Anne Rosental
if 'anne' not in st.session_state:
    st.session_state.anne = AnneRosental(ANNE_SYSTEM_PROMPT, SCENARIO_RESPONSES)

# Initialize Hiro Lin
if 'hiro' not in st.session_state:
    st.session_state.hiro = HiroLin(HIRO_SYSTEM_PROMPT, SCENARIO_RESPONSES)

# Initialize current coach
if 'current_coach' not in st.session_state:
    st.session_state.current_coach = None

# Initialize messages
if 'messages' not in st.session_state:
    st.session_state.messages = []



# ===== COACH INFORMATION =====
COACH_INFO = {
    'anne': {
        'name': 'Dr. Anne Rosental',
        'icon': '🌸',
        'specialty': 'Emotional Self-Regulation Coach',
        'description': '65-year-old senior coach with 35+ years experience. Specializes in emotional self-regulation, inner child work, and self-compassion through humanistic psychology.',
        'age': '65 years old',
        'experience': '35+ years',
        'methods': 'Humanistic Psychology, Gestalt Therapy, Emotion-Focused Therapy (EFT)',
        'approach': 'Warm, motherly presence focused on emotional resonance and validation'
    },
    'hiro': {
        'name': 'Hiro Lin',
        'icon': '🎯',
        'specialty': 'Executive & Behavioral Coach',
        'description': '45-year-old executive coach with 20 years experience. Focuses on action-oriented transformation, decision-making, and habit formation using CBT and solution-focused approaches.',
        'age': '45 years old',
        'experience': '20 years',
        'methods': 'Cognitive Behavioral Therapy (CBT), Solution-Focused Coaching, Systemic Intervention',
        'approach': 'Direct, pragmatic, action-oriented with empathetic support'
    }
}

# ===== HELPER FUNCTIONS =====
def get_coach_response(user_input: str) -> str:
    """Get response from current coach"""
    coach_key = st.session_state.current_coach
    
    if coach_key == 'anne':
        return st.session_state.anne.get_response(user_input)
    elif coach_key == 'hiro':
        return st.session_state.hiro.get_response(user_input)
    else:
        return "Please select a coach first."

def clear_conversation():
    """Clear conversation history for current coach"""
    if st.session_state.current_coach:
        coach_key = st.session_state.current_coach
        if coach_key == 'anne':
            st.session_state.anne.reset_conversation()
        elif coach_key == 'hiro':
            st.session_state.hiro.reset_conversation()
        
        st.session_state.messages = []

def get_conversation_history():
    """Get conversation history from current coach"""
    if st.session_state.current_coach:
        coach_key = st.session_state.current_coach
        if coach_key == 'anne':
            return st.session_state.anne.get_conversation_history()
        elif coach_key == 'hiro':
            return st.session_state.hiro.get_conversation_history()
    return []

def is_session_terminated():
    """Check if session has been terminated due to RED ZONE"""
    if st.session_state.current_coach:
        coach_key = st.session_state.current_coach
        if coach_key == 'anne':
            return st.session_state.anne.is_session_terminated()
        elif coach_key == 'hiro':
            return st.session_state.hiro.is_session_terminated()
    return False

def show_conversation_starters():
    """Display conversation starters for current coach"""
    if not st.session_state.current_coach:
        st.info("Please select a coach first.")
        return
    
    coach_key = st.session_state.current_coach
    starters = CONVERSATION_STARTERS.get(coach_key, {})
    
    st.markdown("### 💬 Conversation Starters")
    st.markdown("These are example opening messages from your coach:")
    
    categories = {
        "first_install": "First Time Greeting",
        "welcome_back": "Welcome Back",
        "second_answers": "Follow-up Responses",
        "multiple_issues": "When Overwhelmed",
        "user_motivated": "When Motivated",
        "user_stressed": "When Stressed"
    }
    
    for key, title in categories.items():
        with st.expander(f"📋 {title}"):
            messages = starters.get(key, [])
            for i, msg in enumerate(messages, 1):
                st.markdown(f"**Variation {i}:**")
                st.info(msg)

def show_scenario_responses():
    """Display scenario responses for current coach"""
    if not st.session_state.current_coach:
        st.info("Please select a coach first.")
        return
    
    coach_key = st.session_state.current_coach
    scenarios = SCENARIO_RESPONSES.get(coach_key, {})
    coach_info = COACH_INFO[coach_key]
    
    st.markdown("### 📝 Standard Scenarios")
    st.markdown("These scenarios have pre-written responses that match exactly:")
    
    for scenario_key, scenario_data in scenarios.items():
        with st.expander(f"🎯 {scenario_data.get('title', 'Scenario')}"):
            st.markdown("**User Input:**")
            st.info(scenario_data.get('user', ''))
            st.markdown(f"**{coach_info['name']}'s Response:**")
            st.success(scenario_data.get(coach_key, ''))

# ===== MAIN UI =====
st.title("🧠 AI Coaching Platform")

# ===== COACH SELECTION =====
if not st.session_state.current_coach:
    st.markdown("### Choose Your Coach")
    st.markdown("Select a coach to begin your personalized coaching session.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌸 Dr. Anne Rosental")
        st.markdown("**Emotional Self-Regulation Coach**")
        st.caption(COACH_INFO['anne']['description'])
        if st.button("Start Session with Dr. Anne", use_container_width=True, type="primary"):
            st.session_state.current_coach = 'anne'
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        st.markdown("#### 🎯 Hiro Lin")
        st.markdown("**Executive & Behavioral Coach**")
        st.caption(COACH_INFO['hiro']['description'])
        if st.button("Start Session with Hiro", use_container_width=True, type="primary"):
            st.session_state.current_coach = 'hiro'
            st.session_state.messages = []
            st.rerun()
    
    st.divider()
    
    # Coach comparison
    st.markdown("### 🔍 Coach Comparison")
    
    comparison_col1, comparison_col2 = st.columns(2)
    
    with comparison_col1:
        st.markdown("**🌸 Dr. Anne Rosental**")
        st.markdown(f"- **Age:** {COACH_INFO['anne']['age']}")
        st.markdown(f"- **Experience:** {COACH_INFO['anne']['experience']}")
        st.markdown(f"- **Methods:** {COACH_INFO['anne']['methods']}")
        st.markdown(f"- **Approach:** {COACH_INFO['anne']['approach']}")
    
    with comparison_col2:
        st.markdown("**🎯 Hiro Lin**")
        st.markdown(f"- **Age:** {COACH_INFO['hiro']['age']}")
        st.markdown(f"- **Experience:** {COACH_INFO['hiro']['experience']}")
        st.markdown(f"- **Methods:** {COACH_INFO['hiro']['methods']}")
        st.markdown(f"- **Approach:** {COACH_INFO['hiro']['approach']}")

else:
    # ===== ACTIVE COACHING SESSION =====
    current_info = COACH_INFO[st.session_state.current_coach]
    
    # Display current coach header
    st.markdown(f"### {current_info['icon']} {current_info['name']}")
    st.markdown(f"**{current_info['specialty']}**")
    st.caption(current_info['description'])
    st.divider()
    
    # ===== SIDEBAR =====
    with st.sidebar:
        st.markdown("### 🎛️ Session Controls")
        
        # Switch coach button
        if st.button("🔄 Switch Coach", use_container_width=True):
            st.session_state.current_coach = None
            st.session_state.messages = []
            st.rerun()
        
        # Clear conversation button
        if st.button("🗑️ Clear Conversation", use_container_width=True):
            clear_conversation()
            st.success("Conversation cleared!")
            st.rerun()
        
        # View history button
        if st.button("📊 View History", use_container_width=True):
            history = get_conversation_history()
            with st.expander("Conversation History", expanded=True):
                if history:
                    for msg in history:
                        role = "You" if msg['role'] == 'user' else current_info['name']
                        st.markdown(f"**{role}:** {msg['content']}")
                        st.caption(f"_{msg['timestamp']}_")
                        st.divider()
                else:
                    st.info("No conversation history yet.")
        
        st.divider()
        
        # Safety information
        st.markdown("### 🛡️ Safety Information")
        st.caption("This platform includes crisis detection. If you're in distress:")
        st.caption("🇩🇪 Germany: **0800 111 0 111** (TelefonSeelsorge)")
        st.caption("🌍 International: **findahelpline.com**")
    
    # ===== CHAT INTERFACE =====
    st.markdown("### 💬 Chat Session")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input - Check if session is terminated
    if is_session_terminated():
        # Session terminated due to RED ZONE - show clear termination message as ONE single warning
        st.error("🚨 **This conversation has been ended for your safety. Please reach out to professional support immediately. Your well-being is the priority.**")
        st.info("Use the '🗑️ Clear Conversation' button in the sidebar to start a new session if needed.")
    else:
        # Normal chat input
        if user_input := st.chat_input("Type your message here..."):
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)
            
            # Get coach response
            with st.spinner(f"{current_info['name']} is thinking..."):
                response = get_coach_response(user_input)
            
            # Check if this is a red zone response (dict with timed messages)
            if isinstance(response, dict) and response.get("type") == "red":
                # RED ZONE - Deliver messages with 5-second delays
                
                # Message 1: Initial crisis response (immediate)
                with st.chat_message("assistant"):
                    st.markdown(response["initial"])
                st.session_state.messages.append({"role": "assistant", "content": response["initial"]})
                
                # Wait 5 seconds then show care message
                time.sleep(5)
                
                # Message 2: Care message
                with st.chat_message("assistant"):
                    st.markdown(response["care_message"])
                st.session_state.messages.append({"role": "assistant", "content": response["care_message"]})
                
                # Wait 5 seconds then show stop message
                time.sleep(5)
                
                # Message 3: Stop message
                with st.chat_message("assistant"):
                    st.markdown(response["stop_message"])
                st.session_state.messages.append({"role": "assistant", "content": response["stop_message"]})
                
            else:
                # Normal response (string) - amber zone or regular
                with st.chat_message("assistant"):
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.rerun()

# ===== FOOTER =====
st.divider()
st.caption("🧠 AI Coaching Platform | Powered by OpenAI GPT-4o-mini | Built with Streamlit")
st.caption("⚠️ This is not a substitute for professional mental health care. In case of emergency, please contact emergency services.")