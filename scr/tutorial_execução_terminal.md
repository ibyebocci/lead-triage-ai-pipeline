## Tutorial de execução no terminal

webhook captura de dados da lead
AI processor analisa os dados da lead
e crm sync envia essa análise


cd lead-triage-ai-pipeline  # Entra na pasta do projeto recém-criada no computador
ren scr src                 # Renomeia a pasta de 'scr' para 'src' para corrigir o diretório dos scripts
python src/webhook.py       # Executa o script de captação, simulando a chegada dos dados do lead
python src/ai_processor.py  # Executa o script de inteligência artificial para analisar a mensagem e definir o score
python src/crm_sync.py      # Executa o script final que simula o envio e registo dos dados no funil de vendas do CRM
