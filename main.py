import os
import shutil

ARQUIVO_TXT = "atendimentos.txt"
ARQUIVO_BIN = "atendimentos_backup.bin"

def registrar_atendimento():
    nome = input("Nome do cliente: ")
    tipo = input("Tipo de atendimento (hardware, software, financeiro, outros): ").lower()
    resumo = input("Resumo do atendimento: ")
    status = input("Status (concluído, pendente, cancelado): ").lower()

    registro = f"Cliente: {nome}\nTipo: {tipo}\nResumo: {resumo}\nStatus: {status}\n---\n"

    with open(ARQUIVO_TXT, "a", encoding="utf-8") as f:
        f.write(registro)

    print("[OK] Atendimento registrado com sucesso.")

def criar_copia_binaria():
    with open(ARQUIVO_TXT, "rb") as f_txt, open(ARQUIVO_BIN, "wb") as f_bin:
        shutil.copyfileobj(f_txt, f_bin)
    print(f"[OK] Cópia de segurança criada: {ARQUIVO_BIN}")

def filtrar_atendimentos():
    if not os.path.exists(ARQUIVO_TXT):
        print("Nenhum atendimento registrado ainda.")
        return

    filtro = input("Filtrar por (1) Tipo ou (2) Status? Digite 1 ou 2: ")

    chave = ""
    if filtro == "1":
        chave = input("Digite o tipo de atendimento: ").lower()
        campo = "Tipo: "
    elif filtro == "2":
        chave = input("Digite o status: ").lower()
        campo = "Status: "
    else:
        print("Opção inválida.")
        return

    with open(ARQUIVO_TXT, "r", encoding="utf-8") as f:
        atendimentos = f.read().strip().split("---\n")

    resultados = [a for a in atendimentos if f"{campo}{chave}" in a.lower()]

    if resultados:
        print("\n=== RELATÓRIO FILTRADO ===")
        for r in resultados:
            print(r.strip())
            print("-" * 30)
    else:
        print("Nenhum atendimento encontrado com esse filtro.")

def main():
    while True:
        print("\nSISTEMA DE ATENDIMENTO TÉCNICO")
        print("1. Registrar novo atendimento")
        print("2. Filtrar atendimentos")
        print("3. Criar backup binário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_atendimento()
        elif opcao == "2":
            filtrar_atendimentos()
        elif opcao == "3":
            criar_copia_binaria()
        elif opcao == "4":
            print("Encerrando o sistema. Arquivos salvos:")
            print(f"TXT: {ARQUIVO_TXT}")
            print(f"BIN: {ARQUIVO_BIN}")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
