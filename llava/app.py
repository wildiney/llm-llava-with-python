import ollama

res = ollama.chat(
  model='llava:13b',
  messages=[
    {
    'role':'user',
    # 'content':'Describe this image',
    # 'content':'Describe this image C:\\Users\\wildi\\Repositories-Win\\IA-Recognizer\\ia_recognizer\\images\\anya_forger_bond_loid_forger_yor_briar_hd_spy_x_family-2560x1440.jpg',
    'content':'Descreva esta imagem',
    'images':['llava\\images\\image.jpg']
  }]
)

print(res["message"]["content"])