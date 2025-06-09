document.addEventListener('DOMContentLoaded', function() {
    const operacaoSelect = document.getElementById('operacao');
    const mensagemDiv = document.getElementById('mensagemDiv');
    const imagemInput = document.getElementById('imagem');
    const form = document.querySelector('form');
    const submitButton = form.querySelector('input[type="submit"]');

    // Função para alternar a visibilidade do campo de mensagem
    function toggleMensagemCampo() {
        if (operacaoSelect.value === 'Esconder') {
            mensagemDiv.style.display = 'block';
            mensagemDiv.querySelector('input').setAttribute('required', 'required'); // Torna o campo obrigatório ao esconder
        } else {
            mensagemDiv.style.display = 'none';
            mensagemDiv.querySelector('input').removeAttribute('required'); // Remove a obrigatoriedade ao extrair
        }
    }

    // Inicializa o estado do campo de mensagem ao carregar a página
    toggleMensagemCampo();

    // Adiciona o evento de mudança ao select de operação
    operacaoSelect.addEventListener('change', toggleMensagemCampo);

    // Feedback de carregamento ao enviar o formulário
    form.addEventListener('submit', function() {
        submitButton.value = 'Processando...';
        submitButton.disabled = true;
        submitButton.style.backgroundColor = '#6c757d';
    });


});