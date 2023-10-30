import json

def print_nested_json(data, package, indent=""):
      print(f"{indent}- {package}")
      dependencies = data.get(package, [])
      for dep in dependencies:
            print_nested_json(data, dep, indent + "  ")

if __name__ == "__main__":
      path = 'tmp/deps.json'  

      with open(path, 'r') as file:
            data = json.load(file)

      for package in data:
            print_nested_json(data, package)