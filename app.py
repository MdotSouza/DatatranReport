# Importanto a função do arquivo modules/__init__.py
import os
import sys
sys.path.insert(0, os.getcwd())
from modules import main

# Executando as aplicações
main()