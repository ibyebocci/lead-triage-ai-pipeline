def processar_lead(dados_brutos): #Criamos a função "processar_lead", que aceita o argumento "dados_brutos"
    """
    Função que recebe os dados do formuláriom web"
    Aqui faremos a chamada para o enriquecimento e triagem com IA
    """
    print(f"Lead recebido de: {dados_brutos.get('nome')}") #Mostrará a mensagem com a variável dentro do colchete, neste caso, a variável será o nome, que está dentro da base de dados "dados_brutos"
    print(f"E-mail corporativo: {dados_brutos.get('email')}")  #Mostrará a mensagem com a variável dentro do colchete, neste caso, a variável será o e-mail, que está dentro da base de dadaos "dados_brutos"
    
    # Próximo passo: Integrar com IA para gerar o Lead Scoring
    return {"status": "sucesso", "mensagem": "Lead enviado para triagem."} #Criando as tags de status e mensagem, será um arquivo no formato JSON para a API

if __name__ == "__main__": # o bloco de código abaixo só irá ser executado se este arquivo for rodado no terminal
    # Exemplo de payload simulado vindo do site, com dados de um cliente hipotético
    lead_teste = {
        "nome": "Carlos Silva",
        "email": "carlos@empresa-logistica.com.br",
        "mensagem": "Precisamos de uma solução para agilizar nossa logística."
    }
    processar_lead(lead_teste)  #A função construída "processar_lead" será executada com os dados do dicionário "lead_teste"
