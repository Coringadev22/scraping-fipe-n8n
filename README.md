# 🚀 Scraping FIPE com Integração ao n8n

Este projeto realiza **web scraping e requisições na API da Tabela FIPE** para extrair informações de preços de **motos** com base em **marca, modelo e ano**. O resultado é enviado automaticamente para um **webhook do n8n**, onde pode ser formatado e enviado via WhatsApp ou outros canais.

---

## 📌 Tecnologias Utilizadas

- Python 3.10+
- requests
- json
- time
- n8n (integração via webhook)

---

## ⚙️ Como executar

1. Clone o projeto:

```bash
git clone https://github.com/Coringadev22/scraping-fipe-n8n.git
cd scraping-fipe-n8n
```

2. Ative o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script:

```bash
python srcp.py
```

---

## 🔄 Integração com n8n

O envio dos dados é feito via webhook. Exemplo de envio:

```python
requests.post("https://seu-endpoint-n8n.app/webhook/scraping-carros", json=data)
```

No n8n, o fluxo pode:
- Receber os dados
- Formatar com Markdown ou JSON
- Enviar via WhatsApp (Z-API), Telegram ou e-mail

---

## 🖼️ Exemplo de saída no terminal

```
🔎 Marca: HONDA
📍 Modelo: ADV 160
   📆 Ano: 2024 - 💸 Valor: R$ 24.358,00
```

---

## ✍️ Autor

Feito com 💻 e ☕ por **Lucas Coelho** – [@coringadev22](https://github.com/Coringadev22)

📬 Em caso de dúvidas ou sugestões, fique à vontade para abrir uma _issue_ ou entrar em contato!

---

> "A melhor maneira de prever o futuro é criá-lo." – Peter Drucker
