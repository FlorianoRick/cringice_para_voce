from flask import Flask, render_template_string


app = Flask(__name__)


HTML = """

<!DOCTYPE html>

<html lang="pt-BR">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Página Interativa</title>


    <style>


        /* =========================================
           CONFIGURAÇÕES
           ========================================= */

        :root {

            --cor-fundo: #FA8072;

            --cor-caixa: #E0FFFF;

            --cor-botao-sim: #dd0003;

            --cor-botao-nao: #0066ff;

            --cor-botao-sim-hover: #b00002;

            --cor-botao-nao-hover: #004ecc;

            --cor-titulo: #00EEEE;

            --cor-subtitulo: #000000;

            --cor-frase: #ff0000;

            --cor-texto-after: #FF4500;

            --fonte-texto-after: cursive;


            --tamanho-caixa: 400px;

            --arredondamento: 20px;

            --tamanho-titulo: 32px;

            --tamanho-subtitulo: 15px;

            --tamanho-frase: 32px;

            --tamanho-botao: 18px;

        }


        /* =========================================
           PÁGINA
           ========================================= */

        body {

            margin: 0;

            min-height: 100vh;

            display: flex;

            justify-content: center;

            align-items: center;

            background-image: url("/static/boat.jpg");

            background-size: cover;

            background-position: center;

            background-repeat: no-repeat;

            font-family: Arial, sans-serif;

        }


        /* =========================================
           CAIXA PRINCIPAL

           O código original tinha:

           min-height: 317px
           padding: 40px

           Portanto a altura externa era:

           317 + 40 + 40 = 397px

           Aqui mantemos exatamente essa dimensão.
           ========================================= */

        .caixa {

            width: calc(var(--tamanho-caixa) + 80px);

            height: 397px;

            padding: 40px;

            box-sizing: border-box;

            background: var(--cor-caixa);

            border-radius: var(--arredondamento);

            text-align: center;

            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);

            position: relative;

            overflow: hidden;

        }


        /* =========================================
           GIF PRINCIPAL
           ========================================= */

        #gifFundo {

            position: absolute;

            top: 0;

            left: 0;

            width: 100%;

            height: 100%;

            object-fit: cover;

            z-index: 0;

            opacity: 0;

            pointer-events: none;

            transition: opacity 1s ease;

        }


        #gifFundo.mostrar {

            opacity: 1;

        }


        /* =========================================
           IMAGEM AFTER
           ========================================= */

        #imagemAfter {

            position: absolute;

            top: 0;

            left: 0;

            width: 100%;

            height: 100%;

            object-fit: cover;

            z-index: 0;

            opacity: 0;

            pointer-events: none;

            transition: opacity 1s ease;

        }


        #imagemAfter.mostrar {

            opacity: 1;

        }


        /* =========================================
           CONTEÚDO

           Ocupa exatamente a área interna
           da caixa.
           ========================================= */

        .conteudo {

            position: relative;

            z-index: 2;

            width: 100%;

            height: 317px;

            display: flex;

            justify-content: center;

            align-items: center;

            flex-direction: column;

        }


        /* =========================================
           TELA INICIAL
           ========================================= */

        #inicio {

            width: 100%;

            opacity: 1;

            transition: opacity 1s ease;

            display: flex;

            flex-direction: column;

            align-items: center;

            justify-content: center;

        }


        #inicio.esconder {

            opacity: 0;

            pointer-events: none;

        }


        /* =========================================
           TÍTULO
           ========================================= */

        #inicio h1 {

            color: var(--cor-titulo);

            font-size: var(--tamanho-titulo);

            margin: 0 0 8px 0;

            line-height: 1.2;

        }


        /* =========================================
           SUBTÍTULO
           ========================================= */

        #subtitulo {

            color: var(--cor-subtitulo);

            font-size: var(--tamanho-subtitulo);

            font-weight: normal;

            margin: 0 0 20px 0;

        }


        /* =========================================
           BOTÕES
           ========================================= */

        .botoes {

            display: flex;

            justify-content: center;

            align-items: center;

            gap: 15px;

            margin-top: 0;

        }


        button {

            padding: 14px 30px;

            border: none;

            border-radius: 10px;

            color: white;

            font-size: var(--tamanho-botao);

            cursor: pointer;

            transition: 0.3s;

        }


        /* =========================================
           BOTÃO SIM
           ========================================= */

        #botaoSim {

            background: var(--cor-botao-sim);

        }


        #botaoSim:hover {

            background: var(--cor-botao-sim-hover);

            transform: scale(1.05);

        }


        /* =========================================
           BOTÃO NÃO
           ========================================= */

        #botaoNao {

            background: var(--cor-botao-nao);

        }


        #botaoNao:hover {

            background: var(--cor-botao-nao-hover);

            transform: scale(1.05);

        }


        /* =========================================
           GIF JINSHI

           Fica abaixo dos botões.

           IMPORTANTE:
           position: relative não altera o
           tamanho da caixa porque a caixa
           possui altura fixa.
           ========================================= */

        #gifInicial {

            display: block;

            width: 150px;

            height: 70px;

            object-fit: contain;

            margin-top: 18px;

            opacity: 1;

            transition: opacity 1s ease;

        }


        /* =========================================
           MENSAGEM AFTER
           ========================================= */

        #mensagemAfter {

            width: 90%;

            position: relative;

            z-index: 3;

            color: var(--cor-texto-after);

            font-family: var(--fonte-texto-after);

            font-size: var(--tamanho-frase);

            font-weight: normal;

            text-align: center;

            line-height: 1.3;

            text-shadow:

                -1px -1px 0 #000,

                 1px -1px 0 #000,

                -1px  1px 0 #000,

                 1px  1px 0 #000;

            opacity: 0;

            transform: translateY(20px);

            transition: opacity 1s ease, transform 1s ease;

        }


        #mensagemAfter.mostrar {

            opacity: 1;

            transform: translateY(0);

        }


        /* =========================================
           MENSAGEM NÃO
           ========================================= */

        #mensagemNao {

            position: relative;

            z-index: 3;

            color: white;

            font-family: "Times New Roman", Times, serif;

            font-size: 42px;

            font-weight: bold;

            text-align: center;

            opacity: 0;

            transform: scale(0.8);

            transition: opacity 1s ease, transform 1s ease;

        }


        #mensagemNao.mostrar {

            opacity: 1;

            transform: scale(1);

        }


        /* =========================================
           BOTÃO VOLTAR
           ========================================= */

        .botaoVoltar {

            position: relative;

            z-index: 4;

            margin-top: 25px;

            background: rgba(0, 0, 0, 0.75);

            color: white;

            opacity: 0;

            pointer-events: none;

            transition: opacity 1s ease;

        }


        .botaoVoltar.mostrar {

            opacity: 1;

            pointer-events: auto;

        }


        .botaoVoltar:hover {

            background: rgba(0, 0, 0, 0.9);

            transform: scale(1.05);

        }


        /* =========================================
           CAMADA ESCURA AFTER
           ========================================= */

        #camadaAfter {

            position: absolute;

            top: 0;

            left: 0;

            width: 100%;

            height: 100%;

            background: rgba(0, 0, 0, 0.25);

            z-index: 1;

            opacity: 0;

            pointer-events: none;

            transition: opacity 1s ease;

        }


        #camadaAfter.mostrar {

            opacity: 1;

        }


        /* =========================================
           CAMADA ESCURA NÃO
           ========================================= */

        #camadaNao {

            position: absolute;

            top: 0;

            left: 0;

            width: 100%;

            height: 100%;

            background: rgba(0, 0, 0, 0.3);

            z-index: 1;

            opacity: 0;

            pointer-events: none;

            transition: opacity 1s ease;

        }


        #camadaNao.mostrar {

            opacity: 1;

        }


    </style>

</head>


<body>


    <div class="caixa">


        <!-- GIF PRINCIPAL -->

        <img
            id="gifFundo"
            src=""
            alt=""
        >


        <!-- IMAGEM AFTER -->

        <img
            id="imagemAfter"
            src="/static/after.jpg"
            alt=""
        >


        <!-- CAMADA ESCURA AFTER -->

        <div id="camadaAfter"></div>


        <!-- CAMADA ESCURA NÃO -->

        <div id="camadaNao"></div>


        <!-- CONTEÚDO -->

        <div class="conteudo">


            <!-- =================================
                 TELA INICIAL
                 ================================= -->

            <div id="inicio">


                <h1 id="titulo">

                    Você ja sabe a pergunta
                    <br>
                    começa com N

                </h1>


                <div id="subtitulo">

                    o homemzinho fez com seu estagiario

                </div>


                <div class="botoes">


                    <button
                        id="botaoSim"
                        onclick="escolherSim()">

                        Sim

                    </button>


                    <button
                        id="botaoNao"
                        onclick="escolherNao()">

                        Não

                    </button>


                </div>


                <!-- GIF DA TELA INICIAL -->

                <img
                    id="gifInicial"
                    src="/static/jinshi.gif"
                    alt=""
                >


            </div>


            <!-- =================================
                 TEXTO DO SIM
                 ================================= -->

            <div id="mensagemAfter">

                Sei que ainda sou um homenzinho e com erros,
                mas vou tentar ser o seu homenzinho.
                (abre a caixinha agora)

            </div>


            <!-- =================================
                 TEXTO DO NÃO
                 ================================= -->

            <div id="mensagemNao">

                DESCULPA

            </div>


            <!-- =================================
                 BOTÃO VOLTAR
                 ================================= -->

            <button
                id="botaoVoltar"
                class="botaoVoltar"
                onclick="voltarSelecao()">

                Voltar

            </button>


        </div>

    </div>


    <script>


        /* =========================================
           VARIÁVEIS
           ========================================= */

        let temporizadorSim;

        let temporizadorNao;

        let temporizadorTextoNao;

        let temporizadorVoltarNao;


        /* =========================================
           LIMPAR TEMPORIZADORES
           ========================================= */

        function limparTemporizadores() {

            clearTimeout(temporizadorSim);

            clearTimeout(temporizadorNao);

            clearTimeout(temporizadorTextoNao);

            clearTimeout(temporizadorVoltarNao);

        }


        /* =========================================
           ESCOLHER SIM
           ========================================= */

        function escolherSim() {

            limparTemporizadores();


            const inicio =
                document.getElementById("inicio");

            const gifInicial =
                document.getElementById("gifInicial");

            const gif =
                document.getElementById("gifFundo");

            const imagemAfter =
                document.getElementById("imagemAfter");

            const mensagemAfter =
                document.getElementById("mensagemAfter");

            const mensagemNao =
                document.getElementById("mensagemNao");

            const camadaAfter =
                document.getElementById("camadaAfter");

            const camadaNao =
                document.getElementById("camadaNao");

            const botaoVoltar =
                document.getElementById("botaoVoltar");


            /* ESCONDE TELA INICIAL */

            inicio.classList.add("esconder");

            gifInicial.style.opacity = "0";

            botaoVoltar.classList.remove("mostrar");

            mensagemNao.classList.remove("mostrar");

            camadaNao.classList.remove("mostrar");

            mensagemAfter.classList.remove("mostrar");

            imagemAfter.classList.remove("mostrar");

            camadaAfter.classList.remove("mostrar");


            /* REINICIA GIF SIM */

            gif.classList.remove("mostrar");

            gif.src = "";

            void gif.offsetWidth;

            gif.src = "/static/sim.gif";


            /* MOSTRA GIF */

            setTimeout(() => {

                gif.classList.add("mostrar");

            }, 50);


            /* APÓS 2.8 SEGUNDOS */

            temporizadorSim = setTimeout(() => {

                gif.classList.remove("mostrar");


                /* ESPERA O FADE-OUT */

                setTimeout(() => {

                    gif.src = "";


                    /* MOSTRA AFTER */

                    imagemAfter.classList.add("mostrar");

                    camadaAfter.classList.add("mostrar");


                    /* MOSTRA TEXTO */

                    mensagemAfter.classList.add("mostrar");


                    /* MOSTRA BOTÃO VOLTAR */

                    temporizadorSim = setTimeout(() => {

                        botaoVoltar.classList.add("mostrar");

                    }, 5000);


                }, 1000);


            }, 2800);

        }


        /* =========================================
           ESCOLHER NÃO
           ========================================= */

        function escolherNao() {

            limparTemporizadores();


            const inicio =
                document.getElementById("inicio");

            const gifInicial =
                document.getElementById("gifInicial");

            const gif =
                document.getElementById("gifFundo");

            const imagemAfter =
                document.getElementById("imagemAfter");

            const mensagemAfter =
                document.getElementById("mensagemAfter");

            const mensagemNao =
                document.getElementById("mensagemNao");

            const camadaAfter =
                document.getElementById("camadaAfter");

            const camadaNao =
                document.getElementById("camadaNao");

            const botaoVoltar =
                document.getElementById("botaoVoltar");


            /* ESCONDE TELA INICIAL */

            inicio.classList.add("esconder");

            gifInicial.style.opacity = "0";

            botaoVoltar.classList.remove("mostrar");

            mensagemAfter.classList.remove("mostrar");

            imagemAfter.classList.remove("mostrar");

            camadaAfter.classList.remove("mostrar");


            /* REINICIA GIF NÃO */

            gif.classList.remove("mostrar");

            gif.src = "";

            void gif.offsetWidth;

            gif.src = "/static/não.gif";


            /* MOSTRA GIF */

            setTimeout(() => {

                gif.classList.add("mostrar");

                camadaNao.classList.add("mostrar");

            }, 50);


            /* MOSTRA DESCULPA */

            temporizadorTextoNao = setTimeout(() => {

                mensagemNao.classList.add("mostrar");


                /* MOSTRA BOTÃO VOLTAR */

                temporizadorVoltarNao = setTimeout(() => {

                    botaoVoltar.classList.add("mostrar");

                }, 3000);


            }, 2000);

        }


        /* =========================================
           VOLTAR
           ========================================= */

        function voltarSelecao() {

            limparTemporizadores();


            const inicio =
                document.getElementById("inicio");

            const gifInicial =
                document.getElementById("gifInicial");

            const gif =
                document.getElementById("gifFundo");

            const imagemAfter =
                document.getElementById("imagemAfter");

            const mensagemAfter =
                document.getElementById("mensagemAfter");

            const mensagemNao =
                document.getElementById("mensagemNao");

            const camadaAfter =
                document.getElementById("camadaAfter");

            const camadaNao =
                document.getElementById("camadaNao");

            const botaoVoltar =
                document.getElementById("botaoVoltar");


            /* ESCONDE TUDO */

            botaoVoltar.classList.remove("mostrar");

            mensagemAfter.classList.remove("mostrar");

            mensagemNao.classList.remove("mostrar");

            camadaAfter.classList.remove("mostrar");

            camadaNao.classList.remove("mostrar");

            imagemAfter.classList.remove("mostrar");

            gif.classList.remove("mostrar");


            /* ESPERA O FADE */

            setTimeout(() => {

                gif.src = "";

                imagemAfter.src = "/static/after.jpg";


                /* RESTAURA GIF INICIAL */

                gifInicial.src = "/static/jinshi.gif";

                gifInicial.style.opacity = "1";


                /* MOSTRA NOVAMENTE A TELA INICIAL */

                inicio.classList.remove("esconder");


            }, 1000);

        }


    </script>


</body>

</html>

"""


@app.route("/")
def inicio():

    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
