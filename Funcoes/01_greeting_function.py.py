# Define uma função chamada 'greeting'
# Ela recebe dois parâmetros:
# - name: nome da pessoa
# - department: departamento da pessoa
def greeting(name, department):
    # Exibe uma mensagem de boas-vindas com o nome
    print("Welcome, " + name)

    # Exibe o departamento ao qual a pessoa pertence
    print("You are part of " + department)


# Chamada da função passando valores fixos
greeting("Blake", "Software engineering")

# Segunda chamada da função com outro nome
greeting("Ellis", "Software engineering")
