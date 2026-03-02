# Vonnue-Decision-Companion-System

#🌿 Cardamom Farmer Assistant
Decision Companion System for Structured Agricultural Decision Making

#1️⃣ Understanding of the Problem
The objective of this project is to design and build a Decision Companion System that helps users make better decisions using structured, explainable logic.
Unlike static comparison tools, the system must:
Accept multiple dynamic inputs
Evaluate options based on criteria
Process inputs logically
Provide a recommendation
Explain why the recommendation was made
Allow different outcomes for different inputs
For this implementation, the chosen domain is Cardamom Farm Management, where farmers often need structured support for decisions related to irrigation, fertilizer, pest control, soil health, shade management, variety selection, and labour planning.
The system is built to simulate real-world agricultural reasoning using deterministic logic.

#2️⃣ Assumptions Made
During development, the following assumptions were made:
Farmers can provide structured numeric and categorical inputs (e.g., soil pH, plant count).
Agricultural recommendations can be simplified into rule-based logic.
The system acts as an advisory tool and not a certified agronomic authority.
Each interaction focuses on one decision module at a time.
Decisions can be modeled using deterministic rules rather than probabilistic models.

#3️⃣ Why the Solution Is Structured This Way
The system follows a modular architecture to ensure clarity, scalability, and maintainability.
Architecture Overview

User Interface (Chatbot UI)
        ↓
Flask Backend API
        ↓
Conversation Manager
        ↓
Decision Modules

Key Components

#Conversation Manager
Handles user interaction
Manages module selection
Performs input validation
Collects missing inputs (slot-filling)
Triggers decision modules
Handles explanation requests

#Context Manager
Temporarily stores session data
Prevents incorrect assumptions
Clears state after each decision cycle

#Decision Modules Each module:
Defines required fields
Collects missing inputs
Applies rule-based evaluation
Returns summary + explanation

This structure ensures:
Clear separation of responsibilities
Independent module scalability
Transparent decision logic
Easy testing and debugging

#4️⃣ Design Decisions and Trade-offs

✔ Rule-Based Logic Instead of Full AI
Reason:
The system must not rely entirely on AI.
Trade-off:
Less natural language flexibility, but:
Fully explainable
Deterministic outputs
Easier to validate
Predictable behavior

✔ Explicit Module Selection
Users must choose which module to explore.
Benefit:
Prevents misclassification
Reduces routing errors
Ensures structured decision flow

✔ Slot-Filling Pattern
Each module defines required inputs and collects them step-by-step.
Benefit:
No hidden assumptions
No premature diagnosis
Structured input validation

✔ Explanation Layer
Each recommendation includes reasoning.
Benefit:
Transparency
User trust
Meets evaluation requirement for explainability

#5️⃣ Edge Cases Considered
The system handles:
Missing required inputs
Invalid numeric values
Negative values
Switching modules mid-process
Repeated explanation requests
Small-scale farms (e.g., 5 plants)
Large-scale farms
Empty inputs
Incorrect module names
Infinite input loops
Unit tests validate:
Module logic correctness
Slot-filling behavior
Conversation transitions
Validation handling

#6️⃣ How to Run the Project

The project active in the link: https://vonnue-decision-companion-system-1.onrender.com/
It may take time to load the web as it sleeps when it is not used(Free plan)

#7️⃣ What I Would Improve With More Time

If more time were available, the following enhancements would be implemented:
Sensitivity analysis (show impact of changing one parameter)
Weighted scoring engine instead of static rule sets
Farm profile persistence
Integration with real agronomic datasets
AI-assisted natural language parsing (while keeping deterministic decision logic)
Data visualization dashboard
