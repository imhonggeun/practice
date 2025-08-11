from datasets import load_dataset
import os
#dataset = load_dataset("honggeun/ai_test")
#print(dataset)

# jsonFile = "ai_test.jsonl"
# dataset = load_dataset("json", data_files=jsonFile)
# print(dataset)

repo_name = "honggeun/ai_test"
token = os.getenv("Hugging_Face")
# dataset.push_to_hub(repo_name, token=token)


from huggingface_hub import login,delete_repo
login(token=token)
delete_repo(repo_id=repo_name,repo_type="dataset")
