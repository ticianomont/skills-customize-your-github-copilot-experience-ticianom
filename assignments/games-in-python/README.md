
# 📘 Tarefa: Jogo da Forca

## 🎯 Objetivo

Praticar conceitos fundamentais de Python, como manipulação de strings, uso de listas, condicionais e loops, ao desenvolver o clássico jogo da forca.

## 📝 Tarefas

### 🛠️ Selecionar e ocultar a palavra

#### Descrição
Escolha uma palavra aleatória de uma lista predefinida e prepare uma versão oculta para que o jogador possa tentar adivinhar as letras sem ver a resposta completa.

#### Requisitos
O programa concluído deve:

- Definir uma lista com palavras possíveis para o jogo
- Selecionar uma palavra aleatória da lista
- Representar a palavra escondida com underscores ou espaços vazios
- Exibir o progresso atual da palavra para o jogador
- Mostrar a quantidade de tentativas restantes no início da partida

### 🛠️ Receber palpites e validar letras

#### Descrição
Crie a interação com o usuário para receber letras, verificar se elas fazem parte da palavra e atualizar o estado do jogo conforme as respostas.

#### Requisitos
O programa concluído deve:

- Solicitar ao jogador uma letra por vez
- Verificar se a letra informada está presente na palavra secreta
- Atualizar a palavra oculta quando a letra for correta
- Informar ao jogador quando a letra for incorreta
- Evitar que a mesma letra seja contabilizada mais de uma vez

### 🛠️ Controlar tentativas e encerrar o jogo

#### Descrição
Finalize a lógica do jogo, controlando as tentativas restantes e exibindo mensagens claras de vitória ou derrota ao final da partida.

#### Requisitos
O programa concluído deve:

- Diminuir as tentativas quando a letra for errada
- Encerrar o jogo quando a palavra for completamente revelada
- Encerrar o jogo quando o jogador esgotar todas as tentativas
- Exibir uma mensagem de vitória quando o jogador acertar a palavra
- Exibir uma mensagem de derrota quando o jogador perder