
const emailsAceitos = ['@gmail.com', '@hotmal.com', '@uol.com']
const linksmenu = document.querySelectorAll('.navegar a')
linksmenu.forEach(link => {
    link.addEventListener('click', function (event){
        event.preventDefault();

        const destino = link.getAttribute('href');
        const secao = document.querySelector(destino);

        secao.scrollIntoView({
            behavior: 'smooth'
        });
    });
});

const form = document.querySelector('.formulario')
const status = document.getElementById('mensagem-status')

form.addEventListener('submit', function (event){
    event.preventDefault();

    const nome = document.getElementById('nome').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensagem = document.getElementById('mensagem').value.trim();
    
    const resul = emailsAceitos.some(e => email.endsWith(e));

    if (resul === true && nome && email && mensagem) {
        status.textContent = '✅ Mensagem Enviada.'
        status.style.color = 'green'
        return;
    }

    if (!nome || !email || !mensagem) {
        status.textContent = '❌ Preencha todos os campos.'
        return;
    };

});