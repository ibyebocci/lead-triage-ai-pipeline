## Lead Triage AI Pipeline ##
 pipeline inteligente e autônomo para captação, enriquecimento e qualificação de leads in-bound utilizando Inteligência Artificial, projetado para mitigar o trabalho operacional do time comercial.

  ## Sobre o Projeto
   Em operações de vendas, velocidade de resposta e qualificação precisa são pilares importantes para o fluxo de um negócio. Quando um lead chega pelo site, a análise do domínio é feita pelo pipeline de forma instantânea, cruzando dados de mercado, pontuando a prioridade (Lead Scoring) e sincroniza as informações estruturadas direto no CRM, tudo em poucos segundos e sem intervenção manual.


  ```mermaid
graph TD
    A[📥 Webhook / Formulário Web] -->|Dados Brutos| B(🔍 Enriquecimento de Domínio)
    B -->|Dados de Mercado| C{🤖 Inteligência Artificial}
    C -->|Avalia Dores & Score| D[⚡ Sincronização no CRM & Alertas]
