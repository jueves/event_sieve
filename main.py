from openai import OpenAI

client = OpenAI()

with open("prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": prompt},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://temporal.garimbaboy.com/forestarock.jpeg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
