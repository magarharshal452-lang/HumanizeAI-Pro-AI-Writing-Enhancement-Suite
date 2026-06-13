PROMPTS = {

    "casual": """
Rewrite the following text so it sounds naturally written by a human.

Requirements:
- Preserve all facts and information.
- Do not add new information.
- Do not remove important details.
- Improve flow and readability.
- Use natural sentence structure.
- Avoid robotic or repetitive wording.

Text:
{text}
""",

    "professional": """
Rewrite the following text in a professional and polished style.

Requirements:
- Preserve all information.
- Improve clarity and readability.
- Use professional language.
- Avoid robotic wording.
- Keep the meaning exactly the same.

Text:
{text}
""",

    "academic": """
Rewrite the following text in a clear academic writing style.

Requirements:
- Preserve all information.
- Improve coherence and flow.
- Use formal language.
- Maintain technical accuracy.
- Do not add or remove facts.

Text:
{text}
""",

    "creative": """
Rewrite the following text in a natural and engaging way.

Requirements:
- Preserve the original meaning.
- Make the writing more human and expressive.
- Improve readability.
- Avoid repetitive phrasing.
- Do not invent information.

Text:
{text}
"""
}
