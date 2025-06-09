from flask import Flask, render_template, request
import os
import main

# Cria a aplicação Flask
app = Flask(__name__)

# Define as pastas para upload e imagens processadas
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'

# Cria essas pastas caso ainda não existam
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Mensagem secreta fixa que será usada pela função de esconder
SECRET_MESSAGE_TO_HIDE = "Mensagem secreta!"

# Define a rota principal da aplicação, aceita GET e POST
@app.route("/", methods=['GET', 'POST'])
def index():
    error_message = None
    operation_done = None
    original_image_url = None
    processed_image_url = None
    extracted_message = None
    if request.method == "POST":
        file = request.files.get('imagem')
        operation = request.form.get('operacao') # 'Esconder' ou 'Extrair'
        mensagem_secreta = request.form.get('mensagem')  # <-- Adicione esta linha

        if not file or not file.filename:
            error_message = "Nenhuma imagem foi enviada."
        elif not file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            error_message = "Formato de arquivo inválido. Apenas .jpg, .jpeg, .png são permitidos."
        elif not operation:
            error_message = "Nenhuma operação foi selecionada."
        else:
            original_filename = file.filename
            # Caminho para salvar a imagem original e para uso pelas funções do main.py
            original_save_path = os.path.join(UPLOAD_FOLDER, original_filename)
            file.save(original_save_path)
            
            # Caminho para URL, relativo à pasta 'static'
            original_image_url = os.path.join('uploads', original_filename)

            if operation == 'Esconder':
                base, ext = os.path.splitext(original_filename)
                # Adiciona um sufixo para evitar sobrescrever a original se tiver o mesmo nome
                # e para diferenciar a imagem processada.
                processed_filename = f"{base}_steg{ext}" 
                
                processed_save_path = os.path.join(PROCESSED_FOLDER, processed_filename)
                processed_image_url = os.path.join('processed', processed_filename)
                try:
                    # Use a mensagem digitada, se fornecida, senão use uma padrão
                    main.hide_text_in_image(
                        original_save_path,
                        processed_save_path,
                        mensagem_secreta if mensagem_secreta else "Mensagem secreta!"
                    )
                    operation_done = 'esconder'
                except Exception as e:
                    error_message = f"Erro ao ocultar mensagem: {str(e)}"
            
            elif operation == 'Extrair':
                try:
                    extracted_message = main.extract_text_from_image(original_save_path)
                    operation_done = 'extrair'
                except Exception as e:
                    error_message = f"Erro ao extrair mensagem: {str(e)}"
            else:
                error_message = "Operação inválida selecionada."

    return render_template('index.html',
        error=error_message,
        operation_done=operation_done,
        original_image_url=original_image_url.replace("\\", "/") if original_image_url else None,
        processed_image_url=processed_image_url.replace("\\", "/") if processed_image_url else None,
        extracted_message=extracted_message)
            


if __name__== "__main__":
    app.run(debug=True) # Inicia o servidor Flask (por padrão, roda em localhost:5000)