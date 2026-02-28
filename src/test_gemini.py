from gemini_service import extract_intent_and_entities

def run_test(query):
    print("\nUser Input:")
    print(query)
    print("\nExtracted Output:")
    result = extract_intent_and_entities(query)
    print(result)
    print("-" * 50)


if __name__ == "__main__":

    test_queries = [
        "I have 200 plants in a hot region with low water and steep terrain.",
        "Leaves are yellow and soil pH is 5.2, nitrogen low.",
        "How to control capsule borer during monsoon?",
        "Shade is around 35% and temperature is hot.",
        "Which variety is good for high rainfall and high disease pressure?"
    ]

    for query in test_queries:  
        run_test(query)