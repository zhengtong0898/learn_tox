import json
import yaml

with open("github-actions-demo.yml") as f:
    resp = yaml.load(f, Loader=yaml.SafeLoader)
    print(json.dumps(resp, indent=4))
