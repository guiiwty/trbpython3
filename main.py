import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox

ARQUIVO_TXT = "atendimentos.txt"
ARQUIVO_BIN = "atendimentos_backup.bin"

def registrar_atendimento():
    nome = entry_nome.get()
    tipo = combo_tipo.get()
    resumo = text_resumo.get("1.0", tk.END).strip()
    status = combo_status.get()

    registro = f"Cliente: {nome}\nTipo: {tipo}\nResumo: {resumo}\nStatus: {status}\n---\n"

    with open(ARQUIVO_TXT, "a", encoding="utf-8") as f:
        f.write(registro)

    messagebox.showinfo("Sucesso", "[OK] Atendimento registrado com sucesso.")
    limpar_campos()

def criar_copia_binaria():
    try:
        with open(ARQUIVO_TXT, "rb") as f_txt, open(ARQUIVO_BIN, "wb") as f_bin:
            shutil.copyfileobj(f_txt, f_bin)
        messagebox.showinfo("Sucesso", f"[OK] Cópia de segurança criada: {ARQUIVO_BIN}")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhum atendimento registrado para criar o backup.")

def filtrar_atendimentos():
    filtro_tipo = combo_filtro_tipo.get().lower()
    filtro_status = combo_filtro_status.get().lower()
    resultados = []

    if not os.path.exists(ARQUIVO_TXT):
        messagebox.showinfo("Informação", "Nenhum atendimento registrado ainda.")
        return

    with open(ARQUIVO_TXT, "r", encoding="utf-8") as f:
        atendimentos = f.read().strip().split("---\n")

    for atendimento in atendimentos:
        if filtro_tipo and filtro_tipo in atendimento.lower() and filtro_status and filtro_status in atendimento.lower():
            resultados.append(atendimento)
        elif filtro_tipo and filtro_tipo in atendimento.lower() and not filtro_status:
            resultados.append(atendimento)
        elif filtro_status and filtro_status in atendimento.lower() and not filtro_tipo:
            resultados.append(atendimento)

    if resultados:
        relatorio = "\n RELATÓRIO FILTRADO \n"
        for r in resultados:
            relatorio += r.strip() + "\n" + "-" * 30 + "\n"
        messagebox.showinfo("Resultados da Busca", relatorio)
    else:
        messagebox.showinfo("Informação", "Nenhum atendimento encontrado com esse filtro.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    combo_tipo.set("")
    text_resumo.delete("1.0", tk.END)
    combo_status.set("")

root = tk.Tk()
root.title("Sistema de Atendimento Técnico")

tk.Label(root, text="Nome do Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

tk.Label(root, text="Tipo de Atendimento:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
tipos = ["hardware", "software", "financeiro", "outros"]
combo_tipo = ttk.Combobox(root, values=tipos, width=37, state="readonly")
combo_tipo.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

tk.Label(root, text="Resumo:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
text_resumo = tk.Text(root, height=5, width=40)
text_resumo.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

tk.Label(root, text="Status:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
status = ["concluído", "pendente", "cancelado"]
combo_status = ttk.Combobox(root, values=status, width=37, state="readonly")
combo_status.grid(row=3, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

btn_registrar = tk.Button(root, text="Registrar Atendimento", command=registrar_atendimento)
btn_registrar.grid(row=4, column=0, padx=5, pady=10, columnspan=3, sticky=tk.W+tk.E)

tk.Label(root, text="Filtrar por Tipo:").grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
combo_filtro_tipo = ttk.Combobox(root, values=tipos, width=37, state="readonly")
combo_filtro_tipo.grid(row=5, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

tk.Label(root, text="Filtrar por Status:").grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
combo_filtro_status = ttk.Combobox(root, values=status, width=37, state="readonly")
combo_filtro_status.grid(row=6, column=1, padx=5, pady=5, columnspan=2, sticky=tk.W+tk.E)

btn_filtrar = tk.Button(root, text="Filtrar Atendimentos", command=filtrar_atendimentos)
btn_filtrar.grid(row=7, column=0, padx=5, pady=10, columnspan=3, sticky=tk.W+tk.E)

btn_backup = tk.Button(root, text="Criar Backup Binário", command=criar_copia_binaria)
btn_backup.grid(row=8, column=0, padx=5, pady=10, columnspan=3, sticky=tk.W+tk.E)

root.mainloop()
