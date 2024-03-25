import tree_main # Importa o módulo tree_main, que contém a implementação da árvore AVL
import string     

BookQuincas = 'QuincasCap1a5.txt' # Define o caminho do arquivo a ser processado

# Lista de palavras a serem removidas
words_to_remove = set(["e", "ou", "mas", "a", "o"])

# Função para carregar o arquivo, separar em palavras e remover palavras indesejadas
def process_text_file(file_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
       
        text = file.read()

       # Converte todo o texto para minúsculas
        text = text.lower()

      # Remove pontuação e caracteres especiais
        text = ''.join(char for char in text if char not in string.punctuation)

       # Divide o texto em palavras usando espaços como delimitadores
        words = text.split()

      # Remova as palavras indesejadas  
        filtered_words = [word for word in words if word not in words_to_remove]

        return filtered_words

# Processa o arquivo de texto e obtém uma lista de palavras filtradas
filtered_words = process_text_file(BookQuincas)


avl_tree = tree_main.AVLTree()

# Preenche a árvore com as palavras filtradas
for word in filtered_words:
    avl_tree.add(word)

# Solicita ao usuário que digite um prefixo
prefix = input("Digite o prefixo: ")

# Exibe o prefixo digitado pelo usuário
print("prefixo digitado:", prefix)

#Contador de palavras repetidas
repetition_counter = {}

for word in filtered_words:
    if word.startswith(prefix):
        if word not in repetition_counter:
            repetition_counter[word] = 1
        else:
            repetition_counter[word] += 1

print("Palavras com prefixo'{}'   Repetições:".format(prefix))
for word, repetitions in repetition_counter.items():
    print("{}: {}".format(word, repetitions))

