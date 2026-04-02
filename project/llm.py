import os
from openai import OpenAI, RateLimitError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question, context_chunks):
    context = "\n".join(context_chunks)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are an assistant for the KMITL Robotics and AI Engineering program.

Rules:
- Use ONLY the provided context.
- If the answer is not in the context, say "I don't know".
- Be clear and helpful.

Context:
{context}
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except RateLimitError:
        return "⚠️ OpenAI quota exceeded. Please check billing or switch to a local model."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"