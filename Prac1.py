from dataclasses import dataclass,asdict
import json
import time

def execute_llm_call(prompt_text,model_engine="gpt-4",**kwargs):
    print(f"\nRouting request to model: {model_engine}")
    print(f"Prompt: {prompt_text}")
    print(f"Extra parameters: {kwargs}")
    print("Processing...\n")

    return{
        "text": "Mock response for prompt: {prompt_text}",
        "usage_metrics":{"tokens":120}
    }

def mock_api_call(prompt, simulate_timeout=False, simulate_missing_key=False):
    print("\nInitiating API CALL..")
    
    try:
        print("waiting for response 5 sec")
        time.sleep(5)

        response= execute_llm_call(prompt)
    
        if simulate_missing_key:
            print("simulating missing key error..")
            malformed_response = {"text": "Hello, world!"}
                #This line will cause a KeyError because 'usage_metrics' is not in the dictionary
            tokens = malformed_response['usage_metrics']
            print('Tokens used: ', tokens)
    
        if simulate_timeout:
            raise TimeoutError("LLM API time out")
    
        tokens= response["usage_metrics"]["tokens"]
        print("Toeken used: {tokens}")
        print("Response: ",response["text"])
   
    except KeyError as e:
        print("\n[CRITICAL ERROR] Missing key in response: {e}")
    
    except TimeoutError as e:
        print("\n[NETWORK ERROR] {e}")
    
    finally:
        print("API transaction finalized ")



if __name__ == "__main__":

    user_prompt = input("Enter your prompt: ")

    print("\n--- Test 1: Normal Call ---")
    mock_api_call(user_prompt)

    print("\n--- Test 2: Timeout Error ---")
    mock_api_call(user_prompt, simulate_timeout=True)

    print("\n--- Test 3: Missing Key Error ---")
    mock_api_call(user_prompt, simulate_missing_key=True)



