def simple_prompt(animal_statement):
    return f"""動物に関する記述が提供されます。あなたの仕事は、その動物の脚の本数を判断することです。
    
    以下が動物に関する記述です。
    <animal_statement>{animal_statement}</animal_statement>
    
    この動物の脚は何本ですか？数字で回答してください。"""

def better_prompt(animal_statement):
    return f"""動物に関する記述が提供されます。あなたの仕事は、その動物の脚の本数を判断することです。
    
    以下が動物に関する記述です。
    <animal_statement>{animal_statement}</animal_statement>
    
    この動物の脚は何本ですか？2や9のような1桁の数字のみで回答してください。"""

def chain_of_thought_prompt(animal_statement):
    return f"""動物に関する記述が提供されます。あなたの仕事は、その動物の脚の本数を判断することです。
    
    以下が動物に関する記述です。
    <animal_statement>{animal_statement}</animal_statement>
    
    この動物の脚は何本ですか？ 
    まず、<thinking>タグ内で段階的に思考し、動物の脚の本数について推論してください。  
    その後、<answer>タグ内に最終的な答えを出力してください。 
    <answer>タグ内には、脚の本数を整数のみで返し、それ以外は何も含めないでください。"""