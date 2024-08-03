import openai


class Chatbot:
    def __init__(self):
        openai.api_key = "your_openai_api_key"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            # Max no of words bot gives
            max_tokens=4000,
            # If we provide less temperature it provides more accurate answers but they will be less diverse
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    # Instantiate Chatbot
    chatbot = Chatbot()
    # Get response
    response = chatbot.get_response("Why temperature is used in chatbot code?")
    print(response)