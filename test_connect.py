from openai import OpenAI

if __name__ == "__main__":
    client = OpenAI(
        # openai系列的sdk，包括langchain，都需要这个/v1的后缀
        base_url="https://api.closeai-proxy.xyz/v1",
        api_key="sk-W49Vw1nrTbEXv5koXnM0s80gsK7aN5XYxisgtsl6uJisUTKA",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say hi",
            }
        ],
        model="o1-preview",
        # model="o1-2024-12-17",
    )

    print(chat_completion)
