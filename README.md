# middleware
Projeto proposto como tarefa da disciplina de Sistemas Distribuídos do Curso GB em Sistemas de Informação da Universidade Federal do Piauí - Campus Senador Helvídeo Nunes de Barros.

Ideia Geral: Implementar um sistema distribuído com uso de middleware.
Requisito Funcional do Sistema: Software de TRANSFORMAÇÃO DE TEXTO.
Recursos Físicos: Smartphone, computador 01, computador 02, computador 03.

Arquitetura: O smartphone é um cliente que está conectado ao computador 01 (middleware), que por sua vez está conectado a dois servidores (computador 02 e 03).
O computador 02 realiza operações de CONCATENAR O TEXTO,
O computador 03 realiza operações de TORNAR O TEXTO CAIXA ALTA.

Modo de Demostração: O cliente requisita um serviço e o middleware encaminha a requisição AO MESMO TEMPO USANDO THREADS aos servidores. O resultado é retornado para o cliente pelo middleware quando este por sua vez receber os dois resultados.
Comunicação: Os serviços nos servidores serão providos por uma interface RESTful 

Ferramentas usadas
Webservices de transformação de texto com Flask
Middleware criado com ZeroMQ 
Cliente criado em java para demonstração
