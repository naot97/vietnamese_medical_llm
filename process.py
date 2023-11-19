import pandas as pd
import os
data_dir = './corpus'
name_files = os.listdir(data_dir)
data = []
import re

def preprocess(text: str) -> str:
	text= '\n'.join(text.split('\n')[4:])
	return re.sub('<[^<>]*>','', text)
	
for name in name_files:
	file_path = os.path.join(data_dir, name)
	with open(file_path, 'r') as f:
		data.append({
			'name': name,
			'text': preprocess(str(f.read()))
		})
	


df = pd.DataFrame(data)
print(df.head(5))
df.to_csv('./kalapa.csv', encoding='utf-8')
