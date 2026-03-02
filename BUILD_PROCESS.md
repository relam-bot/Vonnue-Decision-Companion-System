Day 1


i am starting to do the project and i  decided that i should do the decision making assitant on the field of agriculture as my family income comes from it.so after searching on internet for a topic and finally by my father's opinion i have finalised my topic is Cardamom Farmer Assistant.
The Assitant will help the user on deciding:
>Irrigation
>Soil PH and Nutrition
>Labour
>Fertilizer And Pesticides
>Shade Requirement For Cardamom and Basic Requirements
>Different types of cardamom plant

i dont know to create the model so i asked chatgpt how to do it and it said i have to create a decision engine that will help in deciding which will help in making better decision for the farmer.Each property should have a decision engine on it own as every property is not same.The suggested ways are:
Irrigation	Hybrid (Rule + Weighted)	
Soil pH & Nutrition	(Rule-Based)	
Labour	(Weighted Scoring)
Fertilizer & Pesticide	(Weighted + Risk)	
Shade	(Rule + Light Scoring)	
Variety Selection	(Weighted Scoring)
i asked if we can start creating it module by module it said we can first build a solid base of everything like decision engine and input validation etc
thats all for day 1.


Day 2


We are gonna decide on a proper architecture for the system today.so this is the current architectue given by chatgpt

User Question
      ↓
Intent Detection (simple rule-based)
      ↓
Relevant Module (Irrigation / Soil / etc.)
      ↓
Decision Engine
      ↓
Explanation Generator
      ↓
Final Answer

I asked for a trial case and it showed basic logic and i felt that it doesnt work on every cases 
so i asked the gpt  "how will it handle when u say that he has only 1 plant and which irrigation is better".so gpt suggested that i add a context detection like explaination for different scenerio different user input and cases
As of now the model doesnt ask us its needed information it just assumes things in case which reduces accuracy of the assistant so i told gpt to change it way in which the assistant asks us for required information

Updated Architecture:

User Question
     ↓
Intent Detection
     ↓
Module
     ↓
Check Required Inputs
     ↓
Ask Missing Questions
     ↓
Update Context
     ↓
Run Decision Engine
     ↓
Generate Explanation

Now that these are sorted i thought to make human and assistant model interaction better i could use LLM  like gemini for its NLP(Natural Language Processing).It will make the conversion easy to understand ,fetch required data or ask for information based on context.i completely restrict gemini for dataprocessing it is only used in the communication process .

Updated Architecture:

User Question
      ↓
Gemini API (Intent + Info Extraction)
      ↓
Structured Context (JSON format)
      ↓
Your Rule-Based + Weighted Engine
      ↓
Ranking
      ↓
Gemini (Optional: convert explanation to natural text)
      ↓
Final Answer

Then i did more thinking about how the input part of the system should work and it should handle all the cases and information.i asked Gpt so many case like what if some intial question about ph and how information should be in the first query

Now as i continued with project Gpt asked if i wanna do a unified loop or each module completely independent.So i did a small research with GPT on that topic and it showed that if u have a unified loop every module with active in the chat itself but if i do independent loop then i will have to find which module it is from first and then contact it which is not efficient so finalize that doing the unified loop is the better way

Updated Architecture:
User Input
    ↓
Gemini (Intent + Info Extraction)
    ↓
Update Global Context
    ↓
Conversation Manager
    ↓
Call Appropriate Module
    ↓
Decision Engine (Rule + Weighted)
    ↓
Explanation Generator
    ↓
Response to User

Now that i have included all my doubt and design implementation into this i asked gpt for suugestion.it showed me so many conition but the ones that i choose for my model are
Add an Input Validation Layer for validating all the imput if its in correct or not
Persistent Memory Decision with option to delete for saving a persons history in chat for future reference
Add Explainability Breakdown Module for explaination if user asks
Add Sensitivity Analysis that also suggest things for providing the user with his side option in farming

Final Architecture:

User
  ↓
Conversation Manager (Unified Loop)
  ↓
Gemini Service (Intent + Entity Extraction)
  ↓
Input Validation Layer
  ↓
Context Manager
   ├── Session Context (In-Memory)
   └── Persistent Storage (JSON File)
  ↓
Module Router
  ↓
Decision Engine
   ├── Hard Constraint Filter
   ├── Weighted Scoring Engine
   ├── Risk Adjustment
   └── Ranking System
  ↓
Explainability Engine
   ├── Score Breakdown
   ├── Removed Options
   └── Contribution Analysis
  ↓
Sensitivity Analyzer 
  ↓
Response Generator
  ↓
User


Day 3

So today i started coding the system with help of chatgpt.We started with the main.py which is the start of the full operation.So the Layer are
A Question Handling Layer
A Decision Engine Layer
A Response Generator
i created a simple question handling layer ,decision and response layer and output was little bit funny then i realized some modules require some concrete information to provide answers so i think.the chatbot should ask if any information is required.Gpt then told that we need a context.py which will store all the data that model needs to understand which module it is and how it shuld perform
The input system looked so boring that it didnt get context half the time.So i thought that a gemini api can be implemented for its NLP property.then we sorted the global variable in all the modules so we could store them as one and other variables in their own module variables.I ran some test cases on the model the resuts were ohkey not great.then we implementedd the validateion layer which validates the data entered during input so that numbers get stored and number and characters are characters.
I needed the core of the project the conversation_manager this handles the context and intention and collets the requirement for the project the amount of time and pain that took make this properly working was concerning.Now we did the full modules like the irrigation,soil,fertilizer,pesticides,variety and shade.then we connected them into the conversation manager as it decides which module to be callded and which all details are required additionally.
As i completed the full model on a smaller version i thought i should run some test cases.It ended in disaster as the modules that read and intented were different and wrong.i tried to add more into the modules as debugged the issues with help of gpt.Now we have a expanded modules and new gemini integration that understands important details and takes all that input accordingly.But it later became a disaster as i didnt check it in every stage we caused every module and feature to fail. in the middle my free API key also hit daily limit.Then i finally made it better the model stopped taking my input and the whole model was returning values based on my previous runs so i understand that the persistant memory was causing the problem.I ended up reworking most of the modules.It still didnt work i just commited the code into the git as i was sleepy and exhausted.

Day 4

At the starting of the day i handed the whole code folder to the Gpt.It did rework all the code that prevents hallucination and recalling previous memory.It started working again so i thought i should run the full test case so i dont repeat my previous mistake.it was initially ohkey but then API key expired and the input layer was not working properly i tried to work on it but it was not working any how i gave the input.Then i was exhaushed because i was using the free api key and that expires every 20 query which dont even satisfy my test cases.so i took the decision of removing gemini and making my project smaller but which works.
then i changed the gemini service module to intent_extractor.I made the changes for the code to adapt to intent_extractor.i decreased the module size because i thought that making a small one that properly works is better than big one thats not working.I finally made a working one .I then fine tunned it as the converstion manager had bug and didnt work all the time so i told it give sample input in brackets after asking question and a program like user should decide which module to ask questions about.Then i made a simple ui for it using HTML which makes this like a nice chatbot.I made the UI better and pushed the whole code into github.

Day 5

I was not satisfied with the project but this is the version i submit due to time restrictions.I then researched on where i can host this for free.I found a website called render.I hosted my project on render .everyone can view it on https://vonnue-decision-companion-system-1.onrender.com/.i am on free plan so it may take some time for it to open up.i enjoyed doing this project and this was my build process.
