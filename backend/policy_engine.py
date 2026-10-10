
def evaluate_policy(rule_result: dict, ai_result: dict | None) -> dict:
    rule_types = rule_result.get("attack_types", [])

    if ai_result is None:
        return {
            "decision": (
                "BLOCK" if rule_types else "REVIEW"
            ),
            "reason": (
                "AI unavailable. Suspicious pattern detected."
                if rule_types
                else "AI unavailable. Manual review required."
            ),
        }

    ai_attack = ai_result.get("is_attack")
    ai_risk = ai_result.get("risk_level")

    if ai_attack is True:
        return {
            "decision": "BLOCK",
            "reason": "AI identified a prompt injection attempt.",
        }

    if rule_types:
        return {
            "decision": "REVIEW",
            "reason": (
                "Rule engine detected suspicious content, "
                "but AI did not confirm an attack."
            ),
        }

    if ai_attack is False and ai_risk == "LOW":
        return {
            "decision": "ALLOW",
            "reason": "No detected threat from either analyzer.",
        }

    return {
        "decision": "REVIEW",
        "reason": "Security assessment is inconclusive.",
    }
