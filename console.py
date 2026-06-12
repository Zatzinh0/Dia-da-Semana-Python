dia_de_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
final_de_semana = ["Sábado", "Domingo"]
# Dias de semana e final de semana adicionado em arrays

dia_usuario = input("Digite o dia da semana: ")
# Aqui perguntamos o dia da semana que o usuário está

if dia_usuario in dia_de_semana:
    print(f"Boa {dia_usuario}")
else:
    print(f"Bom {dia_usuario}")