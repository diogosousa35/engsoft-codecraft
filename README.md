# 🕹️ CodeCraft - Plataforma Gamificada de Programação

Sistema de login futurista com interface neon e dashboard interativo desenvolvido com Django.

## ✨ Características

- 🎨 Interface futurista com efeitos neon
- 🔐 Sistema de autenticação seguro
- 🎮 Centro de jogos integrado
- 📱 Design totalmente responsivo
- ⚡ Performance otimizada
- 🐳 Docker ready

## 🛠️ Tecnologias

- **Backend**: Django 5.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Gerenciamento**: Poetry
- **Database**: SQLite/PostgreSQL
- **Cache**: Redis
- **Deploy**: Vercel

## 🚀 Instalação

### Usando Poetry

\`\`\`bash
# Clone o repositório
git clone https://github.com/diogosousa35/codecraft-ifpi.git
cd codecraft-ifpi

# Instale as dependências
poetry install

# Ative o ambiente virtual
poetry shell

# Configure as variáveis de ambiente
cp .env.example .env

# Execute as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Execute o servidor
python manage.py runserver
\`\`\`

### Usando Docker

\`\`\`bash
# Clone o repositório
git clone https://github.com/nexus-team/nexus-futuristic-login.git
cd nexus-futuristic-login

# Execute com Docker Compose
docker-compose up --build
\`\`\`

## 🎮 Funcionalidades

### Sistema de Autenticação
- Login com interface futurista
- Registro de usuários
- Recuperação de senha
- Perfil de usuário

### Dashboard
- Interface neon responsiva
- Estatísticas em tempo real
- Sistema de partículas interativo
- Efeitos visuais avançados

### Centro de Jogos
- Space Invaders
- Cyber Puzzle
- Neon Runner
- Sistema de pontuação

## 🔧 Comandos Úteis

\`\`\`bash
# Executar testes
poetry run pytest

# Verificar código
poetry run black .
poetry run isort .
poetry run flake8

# Criar migrações
python manage.py makemigrations

# Executar migrações
python manage.py migrate

# Coletar arquivos estáticos
python manage.py collectstatic
\`\`\`

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

## 📞 Suporte

- 📧 Email: codecraft25@gmail.com
- 💬 Discord: Em processo
- 🐦 Twitter: Em processo

---

**Feito com 💙 pela equipe CODECRAFT**
