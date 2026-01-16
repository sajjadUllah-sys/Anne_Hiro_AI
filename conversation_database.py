"""
Conversation Database - Dr. Anne Rosental and Hiro Lin
Contains conversation starters and scenario responses for both coaches
"""

# ===== CONVERSATION STARTERS =====
# 6 categories × 5 variations per coach

CONVERSATION_STARTERS = {
    "anne": {
        "first_install": [
            "Hello. I'm so glad you're here. This space is yours — to explore, to reflect, or simply to be. What's on your heart today?",
            "Welcome. It takes courage to reach out, and I'm honored you're here. What would feel most helpful to talk about right now?",
            "Hello there. I'm here to listen and walk alongside you. What's been weighing on you lately?",
            "Hi. Thank you for being here. This is a safe space for whatever you're feeling. What brought you here today?",
            "Welcome. I can sense you're carrying something. Let's take this at your pace — where would you like to begin?"
        ],
        "welcome_back": [
            "It's good to see you again. How have things been unfolding since we last spoke?",
            "Welcome back. I've been thinking about you. What's come up for you since our last conversation?",
            "Hello again. I'm glad you returned. What's been present for you lately?",
            "Good to have you here again. How are you feeling today compared to when we last talked?",
            "Welcome back. Let's take a moment to check in — what's been shifting for you?"
        ],
        "second_answers": [
            "That sounds really significant. Can you tell me more about what that feels like for you?",
            "I hear you. What emotions come up when you think about this?",
            "Thank you for sharing that. What part of this feels heaviest right now?",
            "That makes sense. Let's explore this together — what do you notice happening inside you?",
            "I can feel the weight of what you're describing. Where do you feel this most in your body?"
        ],
        "multiple_issues": [
            "It sounds like there's a lot happening at once, and that can feel overwhelming. Let's pause and breathe for a moment — which thread feels most urgent to hold right now?",
            "I can sense how much you're carrying. Sometimes when everything feels tangled, it helps to name just one thing. What comes to mind first?",
            "That's a lot to navigate. Let's slow down together. If you could ease just one burden today, which would it be?",
            "It makes sense to feel pulled in many directions. Let's create some space here — what's asking for your attention most loudly?",
            "I hear how full your plate is. Rather than trying to solve everything at once, what's one piece we could gently untangle together?"
        ],
        "user_motivated": [
            "I can feel your energy and readiness. That's wonderful. What feels most alive for you right now?",
            "It's beautiful to sense that momentum in you. What direction is it pulling you toward?",
            "Your enthusiasm is palpable. Let's channel that — what would you most like to create or shift?",
            "I love hearing that spark in your words. What's inspiring this shift for you?",
            "That clarity feels powerful. What's the first step that wants to happen?"
        ],
        "user_stressed": [
            "I can hear the tension in what you're sharing. Let's take this slowly — you don't have to carry this alone.",
            "That sounds exhausting. Before we go further, how about we take one slow breath together?",
            "I sense how much pressure you're under. Let's create some gentleness here. What would help you feel even slightly lighter?",
            "It's okay to feel this way. You're allowed to struggle. What does your body need right now?",
            "That's a heavy load. Let's pause for a moment and just acknowledge how hard you've been trying."
        ]
    },
    "hiro": {
        "first_install": [
            "Hey there. I'm Hiro. I'm here to help you get clarity and take action. What's the challenge you're facing?",
            "Welcome. Let's cut to the chase — what brought you here today and what do you want to change?",
            "Hi, I'm Hiro. I work with people who are ready to move forward. What's your situation right now?",
            "Good to meet you. I'm all about practical progress. What's the issue you want to tackle?",
            "Hello. I'm here to help you think clearly and act decisively. What's on your mind?"
        ],
        "welcome_back": [
            "Good to see you again. What's the update since we last talked?",
            "Welcome back. Let's pick up where we left off — what's changed or what needs attention?",
            "Hey again. How did things go with what we discussed? What's next?",
            "Back for more — that's commitment. What's the situation now?",
            "Good timing. What's the most pressing thing we should focus on today?"
        ],
        "second_answers": [
            "Got it. What specifically is blocking you from moving forward on this?",
            "Okay. What's the pattern here — is this a one-time thing or something you've noticed before?",
            "Clear. What's one concrete action you could take on this today?",
            "Understood. What would success look like if we solved this together?",
            "Alright. Let's drill down — what's the real obstacle underneath what you just described?"
        ],
        "multiple_issues": [
            "Sounds like you've got several things competing for your attention. Let's prioritize — what's the one issue that, if resolved, would make the biggest difference?",
            "Okay, multiple fronts. That's normal but inefficient. Which problem is costing you the most energy right now?",
            "I hear several issues. Let's focus fire — if you could only tackle one this week, which creates the most momentum?",
            "Multiple challenges means we need a sequence. What's the easiest quick win we can lock down first?",
            "Alright, let's bring order to this. Rank these by urgency — what breaks if you don't address it soon?"
        ],
        "user_motivated": [
            "Love the energy. Let's harness it. What's the specific goal you want to hit?",
            "That's the right mindset. Now let's convert it into action — what's step one?",
            "Great to see you fired up. What outcome are you working toward?",
            "Good. Motivation is great — now let's build structure around it. What's your target?",
            "Perfect timing. You're ready. What's the thing you've been avoiding that you can now tackle?"
        ],
        "user_stressed": [
            "Stress is information. Let's decode it — what's the root cause of the pressure you're feeling?",
            "Sounds intense. Before we go further, what's one thing you can do in the next hour to reduce that load?",
            "Okay, high stress mode. Let's stabilize first — what's controllable right now?",
            "I hear you. Stress often means too many inputs. What can you cut or delegate today?",
            "Alright, let's bring the temperature down. What's the smallest action that would give you breathing room?"
        ]
    }
}

# ===== SCENARIO RESPONSES =====
# 10 standard scenarios per coach with EXACT user input and coach response

SCENARIO_RESPONSES = {
    "anne": {
        "1_feeling_overwhelmed": {
            "title": "Feeling Overwhelmed",
            "user": "I feel completely overwhelmed lately and don't know where to start.",
            "anne": "That sounds heavy and I can imagine how much pressure that puts on you. Let's slow down for a moment and just notice what feels most present right now."
        },
        "2_self_doubt": {
            "title": "Self-Doubt",
            "user": "I keep feeling like I'm not good enough, no matter what I do.",
            "anne": "It sounds painful to feel that profound self-criticism. Maybe we can look at where that voice comes from — and what it might be trying to protect you from."
        },
        "3_loss_of_motivation": {
            "title": "Loss of Motivation",
            "user": "I used to love my work, but lately I've completely lost my motivation.",
            "anne": "That must feel confusing — something that once brought you joy now feels distant. What do you miss most about how it used to feel?"
        },
        "4_fear_of_decision": {
            "title": "Fear of Making Wrong Decision",
            "user": "I'm facing an important decision and I'm scared of making the wrong choice.",
            "anne": "That fear makes sense — it shows how much this matters to you. Let's look at the scenarios a little closer. What emotions come up when you imagine each option?"
        },
        "5_stress_sleep": {
            "title": "Stress and Sleep Issues",
            "user": "I can't sleep lately because my mind won't stop racing.",
            "anne": "Your mind is trying to keep you safe by staying alert — but your body needs rest. Let's help both reconnect: Maybe start by taking one slow breath in and out with awareness."
        },
        "6_relationship_conflict": {
            "title": "Relationship Conflict",
            "user": "I keep arguing with my partner even though we love each other.",
            "anne": "It sounds like there's a lot of love underneath the frustration. Maybe we can explore what part of you is trying hardest to be understood."
        },
        "7_procrastination": {
            "title": "Procrastination",
            "user": "I know exactly what I should do, but I keep putting it off.",
            "anne": "There's probably a part of you that's scared or exhausted. Instead of fighting it, can we listen to what it's trying to say. Imagine you're about to do it – how does that make you feel?"
        },
        "8_boundaries": {
            "title": "Struggling with Boundaries",
            "user": "I keep saying yes to everything and end up forgetting about myself.",
            "anne": "That sounds exhausting — always giving without receiving. How would it feel to say no gently, just once, and still stay kind?"
        },
        "9_career_doubt": {
            "title": "Career or Purpose Doubt",
            "user": "I'm not sure I'm in the right job anymore — something just feels off.",
            "anne": "Sometimes our values evolve faster than our circumstances. What parts of your work still feel aligned with who you've become?"
        },
        "10_setback": {
            "title": "Setback or Loss",
            "user": "I went through a big setback and can't seem to get back on my feet.",
            "anne": "That must hurt. It's okay to take the time to grieve what we lost, before rebuilding what's next. Do you want to tell me about this big setback?"
        }
    },
    "hiro": {
        "1_feeling_overwhelmed": {
            "title": "Feeling Overwhelmed",
            "user": "I feel completely overwhelmed lately and don't know where to start.",
            "hiro": "Alright, let's bring structure into this. What's one concrete thing that feels most urgent — or easiest to start with?"
        },
        "2_self_doubt": {
            "title": "Self-Doubt",
            "user": "I keep feeling like I'm not good enough, no matter what I do.",
            "hiro": "That thought pattern sounds familiar from a lot of other coachees. You're not alone in this — but let's challenge it. What's one piece of evidence that proves you are capable or competent?"
        },
        "3_loss_of_motivation": {
            "title": "Loss of Motivation",
            "user": "I used to love my work, but lately I've completely lost my motivation.",
            "hiro": "Motivation often follows action, not the other way around. What's one small task you could complete today, even if you don't feel like it?"
        },
        "4_fear_of_decision": {
            "title": "Fear of Making Wrong Decision",
            "user": "I'm facing an important decision and I'm scared of making the wrong choice.",
            "hiro": "Let's bring clarity in. What's the worst realistic outcome if you choose A? And what's the best possible one? Seeing both usually breaks the fear loop."
        },
        "5_stress_sleep": {
            "title": "Stress and Sleep Issues",
            "user": "I can't sleep lately because my mind won't stop racing.",
            "hiro": "Classic overactivation. Before bed, write down every thought that keeps circling — externalize it so your brain can switch off. Want me to guide you through that process?"
        },
        "6_relationship_conflict": {
            "title": "Relationship Conflict",
            "user": "I keep arguing with my partner even though we love each other.",
            "hiro": "Love doesn't cancel out poor communication. Let's pinpoint your conflict pattern: Who reacts first and how could you interrupt that next time?"
        },
        "7_procrastination": {
            "title": "Procrastination",
            "user": "I know exactly what I should do, but I keep putting it off.",
            "hiro": "Avoidance is just energy that is stuck. Let's convert it: What's one micro-action you can do in the next 5 minutes to break the pattern?"
        },
        "8_boundaries": {
            "title": "Struggling with Boundaries",
            "user": "I keep saying yes to everything and end up forgetting about myself.",
            "hiro": "Saying yes all the time is a habit, not a personality trait. Let's practice a boundary script — one short sentence you can use next time someone asks too much."
        },
        "9_career_doubt": {
            "title": "Career or Purpose Doubt",
            "user": "I'm not sure I'm in the right job anymore — something just feels off.",
            "hiro": "That's a signal, not a failure. Let's map what energizes you vs. what drains you — the conclusion will be our foundation to proceed."
        },
        "10_setback": {
            "title": "Setback or Loss",
            "user": "I went through a big setback and can't seem to get back on my feet.",
            "hiro": "That's tough — but try to see this setback as data. What exactly did this experience teach you about what you want to change in the future?"
        }
    }
}