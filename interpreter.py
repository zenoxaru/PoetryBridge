from openai import OpenAI

client = OpenAI()


def interpret_poem(poem):
    response = client.responses.create(
        model="gpt-5-mini",
        input=f"""
You are PoetryBridge, an AI poetry interpretation assistant.

Read the poem below and explain its meaning clearly for an English learner.

Give:
1. The overall meaning
2. The main themes
3. The tone or feeling
4. Important imagery or symbolism

Use simple, clear English. Do not just summarize the poem. Explain what the poet is trying to communicate.

Poem:
{poem}
"""
    )

    return response.output_text