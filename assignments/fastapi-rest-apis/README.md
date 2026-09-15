# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar uma lista de livros usando o framework FastAPI. Nesta atividade, você praticará rotas HTTP, modelos Pydantic, validação de dados e códigos de status.

## 📝 Tasks

### 🛠️ Criar e executar a aplicação FastAPI

#### Descrição
Complete o código inicial e configure uma aplicação FastAPI que possa ser executada localmente. Adicione uma rota raiz para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI`.
- Disponibilizar uma rota `GET /`.
- Retornar uma mensagem JSON indicando que a API está funcionando.
- Iniciar corretamente com `uvicorn` e permitir acesso à documentação automática em `/docs`.

### 🛠️ Implementar endpoints de livros

#### Descrição
Use uma lista em memória para armazenar livros e implemente endpoints que permitam consultar e cadastrar itens.

#### Requisitos
O programa concluído deve:

- Disponibilizar `GET /books` para retornar todos os livros.
- Disponibilizar `GET /books/{book_id}` para retornar um livro pelo identificador.
- Disponibilizar `POST /books` para cadastrar um novo livro.
- Retornar o código `404` quando o identificador solicitado não existir.
- Retornar o livro criado na resposta do endpoint `POST /books`.

### 🛠️ Adicionar modelos e validação de dados

#### Descrição
Defina modelos Pydantic para representar os dados de entrada e saída da API. Use esses modelos para validar novos livros e documentar os endpoints.

#### Requisitos
O programa concluído deve:

- Criar um modelo `Book` com `id`, `title`, `author` e `year`.
- Exigir `title` e `author` como textos não vazios.
- Validar `year` como um número inteiro positivo.
- Usar um modelo separado para o corpo de criação quando o `id` for gerado pela API.
- Retornar o código `422` quando os dados enviados forem inválidos.

Exemplo de requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```

Exemplo de resposta:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "year": 1937
}
```