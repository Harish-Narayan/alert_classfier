import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI

def serialize_object(obj):
    """Custom serialization for objects that are not natively serializable by JSON."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__  # Attempt to serialize object attributes as a dictionary
    else:
        return str(obj)  # As a fallback, convert to string

def generate_context(context, given_alert):
    if "GOOGLE_API_KEY" not in os.environ:
        os.environ["GOOGLE_API_KEY"] = ""  # Replace with your actual API key

    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    # Create a dictionary to structure the request
    request_data = {
        "Given_alert": given_alert,
        "similiar_alerts": context,
        "task": "You are an AI security analyst. Analyze the given alert information and information about similar alerts. Give possible alert risk and triage steps in crisp steps"
    }
    
    # Convert the dictionary to a JSON string
    try:
        request_json = json.dumps(request_data, default=serialize_object)
    except TypeError as e:
        return f"Error serializing the request data: {str(e)}"

    # Generating detailed physical profiles for actors
    result = llm.invoke(request_json)
    return result.content

