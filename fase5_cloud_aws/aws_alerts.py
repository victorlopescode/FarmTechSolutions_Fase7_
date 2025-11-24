import os
# import boto3  # descomente se for usar de verdade com AWS


def send_alert(message: str, subject: str = "Alerta FarmTech"):
    """
    Versão pensada para produção usando boto3 e SNS.

    - Configure AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY e SNS_TOPIC_ARN
      nas variáveis de ambiente do sistema.
    """
    # Exemplo real (comentado para não quebrar sem credenciais):
    # client = boto3.client("sns", region_name=os.getenv("AWS_REGION", "us-east-1"))
    # topic_arn = os.getenv("SNS_TOPIC_ARN")
    # if not topic_arn:
    #     raise ValueError("SNS_TOPIC_ARN não configurado.")
    # client.publish(TopicArn=topic_arn, Message=message, Subject=subject)
    #
    # Por enquanto, para não depender de credenciais, apenas simulamos:
    print(f"[SIMULAÇÃO SNS] {subject}: {message}")


def send_test_alert():
    """
    Função usada na Fase 7 para o botão de teste.
    """
    send_alert("Este é um alerta de teste disparado pela dashboard da Fase 7.")
