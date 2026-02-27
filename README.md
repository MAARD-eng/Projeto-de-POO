# Sistema de Cadastro Acadêmico (POO)

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos (POO)**, com o objetivo de aplicar na prática os principais conceitos da matéria, como herança, encapsulamento, polimorfismo, organização em camadas e persistência de dados.

O sistema realiza o **cadastro de professores e estudantes**, com interface web e armazenamento dos dados em arquivo JSON.

---

## 👥 Autores

- **Renan Gomes Vieira**
- **Mateus Alvez de Almeida Rodrigues Dantas**

---

## Objetivo do Projeto

Criar um sistema de cadastro que permita:

- Cadastrar professores
- Cadastrar estudantes
- Listar usuários cadastrados
- Buscar usuários por matrícula
- Remover usuários
- Evitar usuários duplicados
- Persistir os dados em arquivo

Tudo isso utilizando corretamente os conceitos de **POO**.

---

## Estrutura do Projeto

```text
Projeto-de-POO/
│
├── modelo/
│   ├── usuario.py
│   ├── professor.py
│   └── estudante.py
│
├── controle/
│   └── cadastro.py
│
├── interface_web/
│   └── cadastro_view.py
│
├── dados.json
├── main.py
└── README.md