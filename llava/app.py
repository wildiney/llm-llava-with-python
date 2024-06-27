import ollama

res = ollama.chat(
  model='llava:13b', # or llava
  messages=[
    {
    'role':'user',
    'content':'Descreva esta imagem',
    'images':['llava\\images\\image.jpg']
  }]
)

print(res["message"]["content"])