
def enviar_para_crm(lead_processado):
    """
    Função que simula o envio dos dados organizados pela IA
    diretamente para o CRM (funil de vendas).
    """
    print(f"A ligar ao CRM...")
    print(f"A registar lead: {lead_processado.get('nome')}")
    print(f"Atribuindo Score: {lead_processado.get('score_ia')}")
    print(f"Dor principal: {lead_processado.get('dor_principal')}")
    
    # Simula o sucesso da sincronização
    return {
        "crm_status": "sucesso",
        "id_registo": "CRM-98765",
        "mensagem": "Lead inserido com sucesso no funil de vendas!"
    }

if __name__ == "__main__":
    # Testando a sincronização com o CRM isoladamente
    lead_finalizado = {
        "nome": "Carlos Silva",
        "email": "carlos@empresa-logistica.com.br",
        "score_ia": "Quente (Alta Prioridade)",
        "dor_principal": "Urgência operacional identificada na mensagem."
    }
    
    resposta_crm = enviar_para_crm(lead_finalizado)
    print("--- STATUS DO CRM ---")
    print(f"Estado: {resposta_crm['crm_status']}")
    print(f"ID no CRM: {resposta_crm['id_registo']}")
