
# Copilot Instructions for Anne_Lin Project

## Project Overview
Anne_Lin is a conversational AI system focused on emotionally resonant, psychologically informed responses. The architecture is persona-driven, with each persona (e.g., Anne Rosental, Hiro Lin) defined by its own logic and communication rules. The system is designed for natural, non-repetitive dialogue and is accessible via a Streamlit web interface.

## Architecture & Key Components
- **main.py**: Application entry point; likely routes requests and initializes personas.
- **Anne_Rosental.py / Hiro_Lin.py**: Define core persona logic and response generation. Each persona is guided by its own `*_prompt.py` file.
- **Anne_Rosental_prompt.py / Hiro_Lin_prompt.py**: Contain persona-specific communication rules and psychological principles. These files are the canonical source for conversational style and validation logic.
- **conversation_database.py**: Handles storage and retrieval of conversation data, supporting context continuity.
- **streamlit_app.py**: Launches the Streamlit web UI for user interaction.

## Developer Workflows
### Environment Setup
1. Activate the virtual environment:
   ```powershell
   & .venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
- Start the web interface:
  ```bash
  streamlit run streamlit_app.py
  ```

### Testing & Validation
- Manually validate persona responses in the Streamlit UI.
- Ensure all changes to persona logic or prompts are consistent with the rules in the relevant `*_prompt.py` file.

## Project-Specific Conventions
- **Conversational Rules**: Avoid repetitive nicknames, overuse of names, and templated phrasing. Use metaphors sparingly (max 1 in 3-4 responses). Acknowledge understanding in a single sentence. Maintain a professional, human-like tone.
- **Persona Guidance**: All persona logic must reference its `*_prompt.py` for rules and principles. Do not hardcode rules in multiple places.
- **Psychological Principles**: Focus on emotional resonance, validation, and fostering self-compassion. Avoid suppression of emotions.

## Integration & Data Flow
- All user interactions flow through the Streamlit UI to the selected persona module, which generates responses using its prompt rules. Conversation history is managed by `conversation_database.py`.
- No external APIs are called by default; all logic is local unless extended.

## External Dependencies
- **Streamlit**: For the web interface.
- **Python packages**: See `requirements.txt` for the full list.

## Examples
**Correct:**
> "That's a powerful realization, Sarah."

**Incorrect:**
> "Dear, I understand..." (condescending)
> "Sarah, Sarah, I hear you Sarah" (overuse of name)

---
Update this guide as the project evolves. For new personas or workflows, document conventions and integration points here.