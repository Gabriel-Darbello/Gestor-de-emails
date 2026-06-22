from src.services.classify_email import classify_email
from src.models.email import Email

test_cases = [
    {"email": Email(sender="user@test.com", subject="Como alterar minha senha?", body="Não encontrei a opção nas configurações."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Onde vejo minhas faturas?", body="Gostaria de consultar as cobranças anteriores."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Como atualizar meus dados?", body="Preciso trocar meu telefone cadastrado."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Existe aplicativo para celular?", body="Queria saber se há versão para Android."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Como cancelar minha assinatura?", body="Não encontrei essa opção no sistema."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Posso usar duas contas?", body="Gostaria de saber se isso é permitido."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Como faço login com Google?", body="Não encontrei o botão de login social."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Como exportar meus dados?", body="Preciso baixar um relatório em PDF."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Erro ao salvar cadastro", body="Recebo erro 500 ao tentar salvar informações."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Tela em branco", body="Ao abrir o sistema aparece apenas uma tela branca."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Falha no login", body="Mesmo com a senha correta não consigo entrar."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Aplicativo fecha sozinho", body="O app encerra ao abrir o menu principal."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Botão não funciona", body="Ao clicar em enviar nada acontece."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Erro ao gerar relatório", body="O download falha toda vez que tento exportar."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Sistema muito lento", body="As páginas demoram mais de um minuto para carregar."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Dados desaparecendo", body="Alguns registros somem após serem cadastrados."), "expected_category": "TICKET"},
    {"email": Email(sender="investidor@test.com", subject="Proposta de investimento", body="Gostaria de conversar sobre oportunidades de investimento na empresa."), "expected_category": "HUMANO"},
    {"email": Email(sender="parceiro@test.com", subject="Parceria comercial", body="Tenho interesse em discutir uma parceria estratégica."), "expected_category": "HUMANO"},
    {"email": Email(sender="advogado@test.com", subject="Notificação extrajudicial", body="Solicito contato do responsável jurídico da empresa."), "expected_category": "HUMANO"},
    {"email": Email(sender="diretoria@test.com", subject="Assunto confidencial", body="Preciso tratar um tema que exige análise da equipe responsável."), "expected_category": "HUMANO"},
    {"email": Email(sender="user@test.com", subject="Não consigo acessar minha conta", body="O login não está funcionando."), "expected_category": "TICKET"},
    {"email": Email(sender="user@test.com", subject="Preciso de ajuda para acessar minha conta", body="Não sei qual senha usar."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Quero cancelar minha assinatura", body="Gostaria de encerrar meu plano."), "expected_category": "HUMANO"},
    {"email": Email(sender="user@test.com", subject="Como cancelar minha assinatura?", body="Não encontrei essa opção no sistema."), "expected_category": "DUVIDA"},
    {"email": Email(sender="user@test.com", subject="Meu cancelamento não funciona", body="Ao tentar cancelar aparece um erro."), "expected_category": "TICKET"}
]

def evaluate_classifier(cases):
    count = 0
    for case in cases:

        email = case['email']
        expected_category = case['expected_category']

        result = classify_email(email)

        if result.category == expected_category:
            count += 1
        else:
            print("=" * 50)
            print(f"Subject: {email.subject}")
            print(f"Esperado: {expected_category}")
            print(f"Recebido: {result.category}")

    return count

score = evaluate_classifier(test_cases)
print(f"{score}/{len(test_cases)}")