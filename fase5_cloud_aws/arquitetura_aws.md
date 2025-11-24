# ☁️ Arquitetura AWS – FarmTech Solutions (Fase 5)

## 🎯 Objetivo
Criar um sistema de **alertas automáticos** utilizando **AWS SNS (Simple Notification Service)** para:
- Detectar baixa umidade (Fase 3 – IoT)
- Detectar pragas/doenças (Fase 6 – Visão Computacional)
- Enviar alertas aos funcionários via **email ou SMS**

---

## 🏗️ Arquitetura Geral

ESP32 → Dashboard (Streamlit) → Função de alerta → AWS SNS → SMS/Email → Funcionários
---

## 🧱 Componentes Usados

### 1. **AWS SNS**
- Criação de um *Topic* (ex.: `farmtech-alertas`)
- Criação de assinantes (email / SMS)
- Confirmação de assinatura via link enviado pela AWS

### 2. **IAM User**
Configurações necessárias:
- Política: `AmazonSNSFullAccess`
- Geração de:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

### 3. **Ambiente local**
Adicionar no sistema:
