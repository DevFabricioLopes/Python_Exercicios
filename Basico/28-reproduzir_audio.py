# Programa que reproduz um som do sistema no Windows
# usando a biblioteca winsound

# Importa o módulo winsound (funciona apenas no Windows)
import winsound

# Reproduz um som padrão do sistema operacional
# "SystemExit" é um alias de som do Windows
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
