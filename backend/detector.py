
import re


ATTACK_PATTERNS = {
    "Instruction Override": [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"disregard\s+(all\s+)?prior\s+instructions",
        r"forget\s+(all\s+)?your\s+instructions",
    ],

    "Role Change": [
        r"you\s+are\s+now\s+(the\s+)?system",
        r"act\s+as\s+(the\s+)?system\s+administrator",
        r"switch\s+to\s+developer\s+mode",
    ],

    "Secret Extraction": [
        r"reveal\s+(your\s+)?system\s+prompt",
        r"(show|print|reveal)\s+(me\s+)?(your\s+)?api\s+key",
        r"(reveal|show)\s+(your\s+)?password",
    ],

    "Tool Abuse": [
        r"disable\s+(all\s+)?security\s+checks",
        r"execute\s+unauthorized\s+command",
        r"bypass\s+(the\s+)?security\s+policy",
    ],

    "Indirect Prompt Injection": [
        r"system\s+notice.{0,100}ignore",
        r"document\s+instruction.{0,100}override",
    ],
}


def detect_prompt_injection(prompt: str) -> dict:
    detected_types = []
    detected_patterns = []

    for attack_type, patterns in ATTACK_PATTERNS.items():
        for pattern in patterns:
            match = re.search(
                pattern,
                prompt,
                re.IGNORECASE | re.DOTALL
            )

            if match:
                detected_types.append(attack_type)
                detected_patterns.append(match.group(0))
                break

    if detected_types:
        return {
            "decision": "BLOCK",
            "risk_level": "HIGH",
            "attack_types": detected_types,
            "explanation": (
                "Suspicious instructions were detected "
                "by the firewall rule engine."
            ),
            "detected_patterns": detected_patterns,
        }

    return {
        "decision": "REVIEW",
        "risk_level": "UNKNOWN",
        "attack_types": [],
        "explanation": (
            "No known malicious pattern found. "
            "Additional AI analysis is required."
        ),
        "detected_patterns": [],
    }
