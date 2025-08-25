# Automação com Selenium – Formulário Hashtag Treinamentos

Fiz esse codigo para aprender e treinar um pouco de automação Web com Python e Selenium.

Script em **Python + Selenium** que:
1) Abre o Chrome,
2) Acessa `https://www.hashtagtreinamentos.com/`,
3) Clica no botão verde da home,
4) Navega até a opção **“Assinatura”** no menu,
5) Alterna para a nova aba,
6) Vai para `https://www.hashtagtreinamentos.com/curso-python`,
7) Preenche **nome, e-mail e telefone** e envia o formulário.

---

## 🧩 Tecnologias
- Python 3.10+
- Selenium 4 (com **Selenium Manager** para baixar o ChromeDriver automaticamente)
- Google Chrome instalado

---

## 📁 Arquivos
- `codigo_selenium.py` – script principal (abre o site, clica em elementos, muda de aba, preenche e envia o formulário)

---

## 🚀 Como executar

### 1) Crie e ative um ambiente virtual (opcional, recomendado)
```bash
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate
