
# 📘 Tarefa: Jogo da Forca

## 🎯 Objetivo

Desenvolver um jogo clássico de adivinhação de palavras em Python, praticando o uso de strings, listas, condicionais, loops e entrada de dados do usuário.

## 📝 Tarefas

### 🛠️ Criação da palavra secreta

#### Descrição
Crie a lógica inicial do jogo, escolhendo uma palavra aleatória de uma lista predefinida e preparando o estado do jogo para a interação com o usuário.

#### Requisitos
O programa concluído deve:

- Definir uma lista com palavras possíveis para o jogo
- Escolher uma palavra aleatória da lista
- Inicializar a palavra oculta com underscores para cada letra
- Mostrar ao jogador o estado atual da palavra e as tentativas restantes

### 🛠️ Entrada e validação de letras

#### Descrição
Implemente a interação com o usuário para receber palpites e validar se a letra informada é válida e se já foi usada antes.

#### Requisitos
O programa concluído deve:

- Solicitar ao usuário uma letra
- Verificar se a letra pertence à palavra secreta
- Atualizar a palavra revelada quando a letra for correta
- Evitar que o mesmo palpite seja contado mais de uma vez
- Informar ao jogador quando a letra estiver errada

### 🛠️ Controle do jogo e finalização

#### Descrição
Finalize a lógica do jogo, controlando o número de tentativas e exibindo mensagens de vitória ou derrota ao final da partida.

#### Requisitos
O programa concluído deve:

- Registrar a quantidade de tentativas restantes
- Diminuir as tentativas quando a letra for incorreta
- Encerrar o jogo quando a palavra for completamente revelada
- Encerrar o jogo quando o jogador esgotar todas as tentativas
- Exibir uma mensagem clara de vitória ou derrota