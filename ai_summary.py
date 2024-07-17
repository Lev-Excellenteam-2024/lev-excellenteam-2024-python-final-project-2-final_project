import os
import asyncio
import openai
import concurrent.futures

async def slide_summary_by_AI(slide_text: str, timeout: int = 30) -> str:

    with open('api.txt', 'r') as f:
        api_key = f.read().strip()
        openai.api_key = api_key

    # Prepare the messages for the API call
    messages = [
        {"role": "system", "content": "Summarize for me as briefly and succinctly as possible"},
        {"role": "user", "content": slide_text}
    ]

    loop = asyncio.get_event_loop()

    try:
        # Use ThreadPoolExecutor to run the API call in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as pool:
            completion = await asyncio.wait_for(
                loop.run_in_executor(
                    pool,
                    lambda: openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                ),
                timeout=timeout
            )
        # Extract the response content from the API response
        response = completion.choices[0].message['content']
    except asyncio.TimeoutError:
        response = "Error: API request timed out"
    except openai.error.OpenAIError as e:
        response = f"OpenAI API error: {str(e)}"
    except Exception as e:
        response = f"Unexpected error: {str(e)}"

    return response
