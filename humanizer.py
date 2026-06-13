from transformers import pipeline
from prompts import PROMPTS

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

def humanize(text, mode):

    prompt = PROMPTS[mode].format(
        text=text
    )

    result = generator(
        prompt,
        max_length=512,
        do_sample=True,
        temperature=0.8
    )

    return result[0]["generated_text"]
