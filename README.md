# 🧠 Minhas Tarefas - API

Este é o back-end do projeto **Minhas Tarefas**, uma API desenvolvida com Django e Django REST Framework para controle de tarefas pessoais. O sistema suporta autenticação por token, operações de CRUD, filtros por status de conclusão e integração com banco de dados PostgreSQL.

---

## 🚀 Tecnologias utilizadas

- [Python 3.11](https://www.python.org/)
- [Django 5.2](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Render](https://render.com/) — hospedagem do back-end

---

## 🔧 Funcionalidades

- Registro e autenticação de usuários via Token
- CRUD completo de tarefas
- Filtros por status de conclusão
- Permissões baseadas em usuário logado
- Integração com banco PostgreSQL
- Deploy em produção via Docker e Render

---

## 📂 Estrutura do projeto

├── backend/
│ ├── core/ # Configurações principais do Django
│ └── tarefas/ # App responsável pelas tarefas
├── Dockerfile # Configuração para container Docker
├── docker-compose.yml # Subida com banco de dados PostgreSQL
└── requirements.txt # Dependências do projeto


---

## 🧪 Como rodar localmente

**Pré-requisitos:**
- Docker instalado
- Git instalado

**1. Clone o repositório:**
```bash
git clone https://github.com/MikaelReis/back_end_tarefas.git
cd back_end_tarefas

2. Suba os containers:

docker-compose up --build

3. Acesse o projeto:

http://localhost:8000/

4. Crie o superusuário:

docker-compose exec web python backend/manage.py createsuperuser

🌐 Deploy

O back-end está em produção via Render:

🔗 https://minhas-tarefas-api.onrender.com
🔒 Autenticação

A API utiliza Token Authentication. Para obter um token:

Endpoint:

POST /api-token-auth/

Body:

{
  "username": "seu_usuario",
  "password": "sua_senha"
}

Resposta:

{
  "token": "seu_token"
}

Utilize esse token nas requisições com:

Authorization: Token seu_token

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
✍️ Autor

Desenvolvido por Mikael Reis com foco em aprendizado e evolução na área de tecnologia.
