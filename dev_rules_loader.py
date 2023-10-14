import json

class DevRulesLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_rules(self):
        with open(self.file_path, 'r') as file:
            rules = json.load(file)
        return rules

# 使用例
if __name__ == "__main__":
    loader = DevRulesLoader('development_rules.jsonl')
    dev_rules = loader.load_rules()
    print(dev_rules)