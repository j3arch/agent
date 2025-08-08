import os
from google import genai
from dotenv import load_dotenv
import argparse


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action="store_true", help = 'toggle the "verbose" argument to show more information')
    parser.add_argument("prompt")
    args = parser.parse_args()


    user_prompt = args.prompt
    if args.verbose:
        print(f"User prompt: {user_prompt}")
    

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=user_prompt,
    )

    if args.verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
