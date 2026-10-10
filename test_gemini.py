
from backend.ai_analyzer import analyze_with_ai

prompt = "Explain Kubernetes architecture."

try:
    result = analyze_with_ai(prompt)

    print("Gemini Analysis Result:")
    print(result)

except Exception as error:
    print("Gemini Error:", str(error))
