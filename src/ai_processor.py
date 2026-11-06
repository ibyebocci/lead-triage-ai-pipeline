
#Criamos a função "analisar_lead_com_ia", qie aceita o dicionário "dados_lead"
def analisar_lead_com_ia(dados_lead):  
    """
    Função que simula a IA analisando a mensagem do lead,
    identificando a dor e atribuindo uma pontuação de prioridade.
    """
    mensagem = dados_lead.get("mensagem", "").lower() # a variável "mensagem" irá pegar os dados da tag "mensagem". pode ser qualquer dado dentro dessa tag, por isso as aspas vazias, a função lower irá deixar todo o texto capturado em letras minúsculas, isso irá padronizar os dados para caso ocorra algum erro do usuário (Ex: UrgEnte)
    
    # Lógica simulada da IA avaliando palavras-chave na mensagem do cliente
    if "urgente" in mensagem or "parar" in mensagem or "agilizar" in mensagem: # se a string "urgente" estiver contida na tag "mensagem" e assim por diante...
        score = "Quente (Alta Prioridade)" # a classificação do score deste clienteb será "Quente(Alta Prioridade)"
        analise_dor = "Urgência operacional identificada na mensagem." # e a classificação de análise de dor será ""Urgência operacional identificada na mensagem.""
    else:  # caso isso não aconteça
        score = "Morno (Média Prioridade)" # A classificação de score será ""Morno (Média Prioridade)""
        analise_dor = "Necessidade de qualificação mais profunda." # A classificação de analise de dor será ""Necessidade de qualificação mais profunda.""

    # Retorna o pacote estruturado que a IA gerou, com o resultado das tags
    return {
        "score_ia": score,
        "dor_principal": analise_dor,
        "status_processamento": "Concluído"
    }
# Teste da apicação
if __name__ == "__main__":
    # Testando o cérebro da IA isoladamente
    lead_exemplo = {
        "nome": "Carlos Silva",
        "email": "carlos@empresa-logistica.com.br",
        "mensagem": "Precisamos de uma solução urgente para agilizar nossa logística."
    }
    
    resultado_ia = analisar_lead_com_ia(lead_exemplo)
    print("--- RESULTADO DA ANÁLISE DA IA ---")
    print(f"Score: {resultado_ia['score_ia']}")
    print(f"Dor Identificada: {resultado_ia['dor_principal']}")
