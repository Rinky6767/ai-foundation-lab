from dataclasses import dataclass,asdict
import json
import time

@dataclass
class AgentProfile:
    agent_name:str
    model_engine:str
    temperature:float

    #default 
    max_retries: int = 3
    is_active: bool = True

Agentic_prof=AgentProfile(agent_name="DataBot",model_engine="gpt-4.1",temperature=0.3)

config_FileName= "agent_config.json"

with open(config_FileName, "w")as file:
    json.dump(asdict(Agentic_prof),file,indent=4)

print("Saved!")