# Copilot Instructions for Anne_Lin Project

## Project Overview
The Anne_Lin project appears to be a conversational AI system designed to provide emotionally resonant and psychologically informed responses. The system emphasizes natural, human-like interactions and avoids repetitive or overly templated communication patterns.

### Key Components
- **`main.py`**: Likely the entry point of the application.
- **`Anne_Rosental.py` and `Hiro_Lin.py`**: Core modules, possibly defining distinct personas or conversational styles.
- **`*_prompt.py` files**: Contain communication rules and psychological principles guiding the AI's conversational tone and structure.
- **`conversation_database.py`**: Manages data storage or retrieval for conversations.
- **`streamlit_app.py`**: Provides a web interface for interacting with the AI.

### Communication Rules
- Avoid repetitive nicknames like "dear" or overusing the user's name.
- Use the user's name sparingly (every 6-7 responses at most).
- Vary response structures to prevent templated conversations.
- Limit metaphors to 1 in every 3-4 responses.
- Acknowledge understanding in one sentence only; avoid repetitive phrases like "I understand."
- Maintain a professional, human-like tone without heavy jargon.

### Psychological Principles
- Focus on emotional resonance and validation.
- Help users integrate emotions rather than suppress them.
- Foster self-soothing, self-compassion, and inner calm.

## Developer Workflows
### Setting Up the Environment
1. Activate the virtual environment:
   ```powershell
   & .venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
- To start the Streamlit app:
  ```bash
  streamlit run streamlit_app.py
  ```

### Testing
- Ensure all modules adhere to the communication rules outlined in the `*_prompt.py` files.
- Validate that the AI's responses align with the psychological principles.

## Project-Specific Conventions
- Follow the communication rules strictly to maintain the intended conversational tone.
- Use the `*_prompt.py` files as the source of truth for conversational guidelines.
- Ensure any updates to the AI's behavior are consistent with the psychological principles.

## External Dependencies
- **Streamlit**: For the web interface.
- **Python packages**: Listed in `requirements.txt`.

## Examples
### Response Structure
**Correct:**
- "That's a powerful realization, Sarah."

**Incorrect:**
- "Dear, I understand..." (too condescending)
- "Sarah, Sarah, I hear you Sarah" (overuse of name)

---

This document is a living guide. Update it as the project evolves to ensure AI agents remain productive and aligned with the project's goals.