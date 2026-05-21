import tkinter as tk
import json
import os

LISTA_TAREFAS = "tarefas.json"

class AppTarefas:
    def __init__(self, root):
        # Definções da janela do aplicativo
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("400x500")
        self.root.configure(bg="white")

        self.tarefas = self.carregar_dados()
        # Carrega dados salvos
        self.setup_ui()
        # Atribuições da interface de usuário
        self.atualizar_lista()
        # Atualiza a lista a cada ação

    def carregar_dados(self):
        # Lê o arquivo JSON para carregar as tarefas salvas
        # Se a lista não existir, cria um arquivo JSON
        if os.path.exists(LISTA_TAREFAS):
            try:
                with open(LISTA_TAREFAS, "r", encoding="utf-8") as f:
                    return json.load(f)
            except:
                return []
        return []

    def salvar_dados(self):
        # Reescreve e salva a lista toda vez que tiver alguma alteração
        with open(LISTA_TAREFAS, "w", encoding="utf-8") as f:
              json.dump(self.tarefas, f, ensure_ascii=False, indent=4)

    def setup_ui(self):
        # --- Topo (Entrada de dados) ---
        frame_topo = tk.Frame(self.root, bg="white", pady=20)
        frame_topo.pack(fill=tk.X, padx=20)

        self.entry_tarefa = tk.Entry(frame_topo, bd=1, relief="solid")
        self.entry_tarefa.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3)
        self.entry_tarefa.bind("<Return>", lambda e: self.adicionar_tarefa())

        btn_add = tk.Button(frame_topo, text="Adicionar", command=self.adicionar_tarefa, 
                           bg="#e1e1e1", relief="groove")
        btn_add.pack(side=tk.RIGHT, padx=(10, 0))

        # --- Meio (Lista de Tarefas) ---
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.frame_lista = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.frame_lista, anchor="nw", width=360)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20)

        # --- Rodapé (Botão Limpar) ---
        frame_rodape = tk.Frame(self.root, bg="white", pady=15)
        frame_rodape.pack(fill=tk.X, padx=20)

        btn_limpar = tk.Button(frame_rodape, text="Limpar Tarefas Concluídas", command=self.limpar_concluidas,
                               bg="#ff4c4c", fg="white", relief="flat", font=("", 10, "bold"))
        btn_limpar.pack(fill=tk.X)

    def adicionar_tarefa(self):
        texto = self.entry_tarefa.get().strip()
        if texto:
            novo_id = max([t['id'] for t in self.tarefas], default=0) + 1
            # Enumera as tarefas para ordená-las
            self.tarefas.append({"id": novo_id, "texto": texto, "feita": False})
            # Adiciona a tarefa no final da lista
            # Novas tarefas são marcadas como "não feitas"
            self.salvar_dados()
            self.entry_tarefa.delete(0, tk.END)
            # Deleta o texto da caixa de entrada
            self.atualizar_lista()

    def toggle_tarefa(self, tid, var, chk):
        # Marca as tarefas como "feita" ou volta para "não feita"
        # tid = tarefa id
        # var = verificador da checkbox
        # chk = checkbox, define o que ocorre quando marcamos a caixinha
        tfeita = var.get() == 1
        for t in self.tarefas:
            if t["id"] == tid:
                t["feita"] = tfeita
                break
        self.salvar_dados()
        nova_fonte = ("", 10, "overstrike") if tfeita else ("", 10)
        chk.config(font=nova_fonte, fg="gray" if tfeita else "black")
        # Fonte cinza riscada quando "feita"

    def limpar_concluidas(self):
        # Limpa a lista, mantendo APENAS as que não estão feitas (False)
        self.tarefas = [t for t in self.tarefas if not t["feita"]]
        self.salvar_dados()
        self.atualizar_lista()

    def atualizar_lista(self):
        # Atualiza a lista toda vez que tiver alteração alteração
        for w in self.frame_lista.winfo_children():
          w.destroy()
        # Primeiro apaga a lista na tela para poder escrever toda a lista de tarefas (evita duplicatas)

        for t in self.tarefas:
            f = tk.Frame(self.frame_lista, bg="white")
            f.pack(fill=tk.X, pady=2)

            var = tk.IntVar(value=1 if t["feita"] else 0)
            fonte_inicial = ("", 10, "overstrike") if t["feita"] else ("", 10)
            
            chk = tk.Checkbutton(f, text=t["texto"], variable=var, bg="white",
                                 font=fonte_inicial, fg="gray" if t["feita"] else "black",
                                 activebackground="white")
            
            chk.config(command=lambda tid=t["id"], v=var, c=chk: self.toggle_tarefa(tid, v, c))
            chk.pack(side=tk.LEFT, anchor=tk.W)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppTarefas(root)
    root.mainloop()