
from backend.detector import detect_prompt_injection
from backend.ai_analyzer import analyze_with_ai
from backend.policy_engine import evaluate_policy


def scan_with_agent(prompt: str) -> dict:
    steps = []

    rule_result = detect_prompt_injection(prompt)
    steps.append("Rule-based inspection completed")

    ai_result = None
    ai_error = None

    try:
        ai_result = analyze_with_ai(prompt)
        steps.append("Gemini AI analysis completed")
    except Exception as exc:
        ai_error = type(exc).__name__
        steps.append("Gemini unavailable; fallback policy applied")

    policy = evaluate_policy(rule_result, ai_result)
    steps.append("Final security policy evaluated")

    attack_types = list(dict.fromkeys(
        rule_result.get("attack_types", [])
        + (
            ai_result.get("attack_types", [])
            if ai_result else []
        )
    ))

    risk_level = (
        "HIGH" if policy["decision"] == "BLOCK"
        else "LOW" if policy["decision"] == "ALLOW"
        else "UNKNOWN"
    )

    return {
        "prompt": prompt,
        "decision": policy["decision"],
        "risk_level": risk_level,
        "attack_types": attack_types,
        "explanation": policy["reason"],
        "detected_patterns": rule_result.get(
            "detected_patterns", []
        ),
        "model_used": (
            ai_result.get("model_used")
            if ai_result else None
        ),
        "analysis_steps": steps,
        "ai_error": ai_error,
    }
