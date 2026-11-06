```bash
# Entra na pasta do projeto recém-criada no computador
cd lead-triage-ai-pipeline

# Renomeia a pasta de 'scr' para 'src' para corrigir o diretório dos scripts
ren scr src

# Executa o script de captação, simulando a chegada dos dados do lead
python src/webhook.py

# Executa o script de inteligência artificial para analisar a mensagem e definir o score
python src/ai_processor.py

# Executa o script final que simula o envio e registo dos dados no funil de vendas do CRM
python src/crm_sync.py
