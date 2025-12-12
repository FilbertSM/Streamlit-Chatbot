import json
from logger import logger

def fetch_role(role_id: str):
    with open("./data/prompt.json", "r", encoding="utf-8") as f:
        if f:            
            data = json.load(f)
            logger.info(f"Success to fetch ${len(data)} roleplay prompt")

            role_prompt = None
            target_id = role_id
            for entry in data:
                if entry["id"] == target_id:
                    role_prompt = entry["prompt"]
                    break

            return role_prompt
        else:
            logger.exception("Error to fetch roleplay prompt")
            raise