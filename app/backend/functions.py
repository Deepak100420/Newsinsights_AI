import json




def load_animation(filepath:str):
            with open(filepath,'r') as f:
                return json.load(f)