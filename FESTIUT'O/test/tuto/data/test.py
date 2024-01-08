import yaml
cpt=0

# Charger le fichier YAML
with open('data.yml', 'r') as file:
    data = yaml.safe_load(file)

# Ajouter la catégorie à chaque livre
for livre in data:
    if cpt==0:
        livre['category'] = 'Fiction'  # Remplacez 'Science Fiction' par la catégorie souhaitée
    if cpt==1:
        livre['category'] = 'Fantasy'  # Remplacez 'Science Fiction' par la catégorie souhaitée
    if cpt==2:
        livre['category'] = 'Action'  # Remplacez 'Science Fiction' par la catégorie souhaitée
    if cpt==3:
        livre['category'] = 'Adventure'  # Remplacez 'Science Fiction' par la catégorie souhaitée
    if cpt==4:
        livre['category'] = 'Detective Story'  # Remplacez 'Science Fiction' par la catégorie souhaitée
        cpt=-1
    cpt+=1

# Enregistrer les modifications dans un nouveau fichier YAML
with open('data_with_categories.yml', 'w') as file:
    yaml.dump(data, file)
