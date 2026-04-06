
## Passo a passo para rodar

### 1. Clonar o repositório

```bash
git clone <link-do-repositorio>
cd <nome-da-pasta>
```

---

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Ativar no Windows (PowerShell):

```bash
.venv\Scripts\Activate
```

---

### 3. Instalar dependências

```bash
python -m pip install pymongo
```

### 4. Configurar conexão com o MongoDB

No arquivo `.py`, verifique a variável `uri`:

```python
uri = "mongodb+srv://usuario:senha@cluster.mongodb.net/"
```

Substitua pelo seu usuário e senha do MongoDB Atlas.

---

### 5. Rodar o projeto

```bash
python mercadolivre.py
```

## 🗄️ Visualizar dados no MongoDB

1. Acesse o MongoDB Atlas
2. Clique em **Browse Collections**
3. Abra o banco `mercadolivre`
4. Visualize as coleções e documentos

---

