import recipes.factory

receita = recipes.factory.make_recipe()
print(receita['cover']['url'])
