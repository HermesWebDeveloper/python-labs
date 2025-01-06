# Exercício 3: Gestão de Animais
# Crie um sistema para gerenciar um zoológico:

# Uma classe Animal com os atributos nome e idade e um método emitir_som.
# Uma classe filha Cachorro, que sobrescreve o método emitir_som para exibir "Latido".
# Uma classe filha Gato, que sobrescreve o método emitir_som para exibir "Miado".
# Crie instâncias de cada animal e chame o método emitir_som para cada um.

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'
    
    def emitir_som(self):
        return print('')
    
class Cachorro(Animal):
    def emitir_som(self):
        return print('Latido')

class Gato(Animal):
    def emitir_som(self):
        return print('Miado')
    
animal1 = Cachorro('Luca', 10)
animal2 = Gato('Dodo', 2)

print('-'*30)
print(animal1)
animal1.emitir_som()

print('-'*30)
print(animal2)
animal2.emitir_som()