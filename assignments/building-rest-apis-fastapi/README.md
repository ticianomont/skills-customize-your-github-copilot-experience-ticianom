# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construir uma API REST simples usando o framework FastAPI, aprendendo como criar rotas, validar dados com Pydantic, retornar respostas em JSON e lidar com erros comuns em endpoints web.

## 📝 Tarefas

### 🛠️ Configuração da Aplicação

#### Descrição
Crie uma aplicação FastAPI básica com uma rota de saúde para verificar se o servidor está funcionando.

#### Requisitos
O programa concluído deve:

- Importar `FastAPI` e criar uma instância da aplicação.
- Incluir uma rota `GET /health` que retorne um JSON com o status da API.
- Executar a aplicação localmente com `uvicorn`.
- Confirmar que a rota responde corretamente em um navegador ou com `curl`.

### 🛠️ Modelagem de Dados e Criação de Itens

#### Descrição
Defina modelos de dados para os itens da API e implemente a rota para criar novos registros.

#### Requisitos
O programa concluído deve:

- Criar um modelo de entrada usando `BaseModel` para representar um item.
- Incluir campos como `name`, `description` e `price`.
- Validar que `name` tenha uma quantidade mínima de caracteres e que `price` seja maior que zero.
- Criar a rota `POST /items` que adiciona um novo item ao armazenamento em memória.
- Retornar o item criado com status `201 Created`.

### 🛠️ Consulta e Busca de Itens

#### Descrição
Implemente endpoints para listar todos os itens e buscar um item específico por ID.

#### Requisitos
O programa concluído deve:

- Criar a rota `GET /items` que retorna a lista completa de itens.
- Criar a rota `GET /items/{item_id}` que busca um item pelo ID.
- Retornar `404 Not Found` quando o item não existir.
- Utilizar nomes de rotas e respostas consistentes com a API REST.

### 🛠️ Melhorias e Validação Avançada

#### Descrição
Melhore a API com ao menos uma funcionalidade extra que mostre o uso de boas práticas em FastAPI.

#### Requisitos
O programa concluído deve:

- Adicionar pelo menos uma melhoria, como:
  - ordenação de itens;
  - suporte a busca por query parameter;
  - documentação automática via Swagger UI;
  - tratamento de erros personalizados.
- Garantir que a API continue funcionando com dados válidos.
- Explorar a documentação gerada automaticamente em `/docs`.

## ✅ Critérios de Conclusão

Para concluir esta atividade, o aluno deve ser capaz de:

- criar uma API REST funcional com FastAPI;
- validar dados de entrada usando Pydantic;
- criar endpoints para leitura e escrita de recursos;
- lidar com erros básicos de API e entender a documentação automática do framework.
