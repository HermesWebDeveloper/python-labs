# Método Estático Crie uma classe chamada Conversor com um método estático chamado celsius_para_fahrenheit que converte temperaturas de Celsius para Fahrenheit. Teste o método com diferentes valores.

class Conversor:

    @staticmethod
    def celsius_para_fahrenheit(graus_celsius):
         graus_fahrenheit = (graus_celsius * (9/5)) + 32
         return graus_fahrenheit
    
def exercicio02():
    conversor1 = Conversor()
    graus_celsius = float(input('Digite o valor em graus celsius: '))
    graus_fahrenheit = conversor1.celsius_para_fahrenheit(graus_celsius)
    print(f'A conversão para fahrenheit é de: {graus_fahrenheit:.2f}')
     
exercicio02()