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
           CONFIGURAÇÕES FÁCEIS DE ALTERAR
           ========================================= */

        :root {
            --cor-fundo: #FA8072;
            --cor-caixa: #ffffff;
            --cor-botao: #dd0003;
            --cor-botao-hover: #00a383;
            --cor-frase: #ff0000;

            --tamanho-caixa: 400px;
            --arredondamento: 20px;

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

            background-image: url("/static/garden.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;

            font-family: Arial, sans-serif;
        }



        /* =========================================
           CAIXA PRINCIPAL
           ========================================= */

        .caixa {
            width: var(--tamanho-caixa);

            padding: 40px;

            background: var(--cor-caixa);

            border-radius: var(--arredondamento);

            text-align: center;

            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);

            /* IMPORTANTE:
               permite que o GIF fique preso
               dentro da caixa */
            position: relative;

            overflow: hidden;
        }


        /* =========================================
           GIF DE FUNDO
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


        /* GIF aparecendo */

        #gifFundo.mostrar {
            opacity: 1;
        }


        /* =========================================
           CONTEÚDO DA CAIXA
           ========================================= */

        .conteudo {
            position: relative;

            z-index: 2;
        }



        /* =========================================
           TÍTULO
           ========================================= */

        h1 {
            color: #333;
            margin-top: 0;
        }


        /* =========================================
           BOTÃO
           ========================================= */

        button {
            margin-top: 20px;

            padding: 14px 30px;

            border: none;
            border-radius: 10px;

            background: var(--cor-botao);
            color: white;

            font-size: var(--tamanho-botao);

            cursor: pointer;

            transition: 0.3s;
        }

        button:hover {
            background: var(--cor-botao-hover);

            transform: scale(1.05);
        }


        /* =========================================
           FRASE
           ========================================= */

        #frase {
            margin-top: 30px;

            color: var(--cor-frase);

            font-size: var(--tamanho-frase);
            font-weight: bold;

            opacity: 0;
            transform: translateY(30px);

            /* Inicialmente escondida */
        }


        /* =========================================
           ANIMAÇÃO DA FRASE
           ========================================= */

        #frase.mostrar {
            animation: revelar 1.5s ease forwards;
        }


        @keyframes revelar {

            0% {
                opacity: 0;
                transform: translateY(30px) scale(0.8);
            }

            60% {
                opacity: 1;
                transform: translateY(-5px) scale(1.05);
            }

            100% {
                opacity: 1;
                transform: translateY(0) scale(1);
            }

        }

    </style>
</head>


<body>

    <div class="caixa">

        <!-- =====================================
             GIF DE FUNDO
             ===================================== -->

        <img
            id="gifFundo"
            src="/static/flower.gif"
            alt=""
        >


        <!-- =====================================
             CONTEÚDO
             ===================================== -->

        <div class="conteudo">

            <h1>Clica Ai</h1>

            <p></p>

            <button onclick="mostrarFrase()">
                Aqui
            </button>

            <div id="frase">
                Voce é perfeita &lt;3
            </div>

        </div>

    </div>


    <script>

        let tempoGif;


        function mostrarFrase() {

            const frase = document.getElementById("frase");
            const gif = document.getElementById("gifFundo");


            /* =====================================
               REINICIA A FRASE
               ===================================== */

            frase.classList.remove("mostrar");

            void frase.offsetWidth;

            frase.classList.add("mostrar");


            /* =====================================
               REINICIA O GIF
               ===================================== */

            clearTimeout(tempoGif);

            gif.classList.remove("mostrar");


            /*
               Força o navegador a recarregar o GIF.
               Isso faz a animação começar novamente
               do primeiro frame.
            */

            gif.src = "";

            void gif.offsetWidth;

            gif.src = "/static/flower.gif";


            /* =====================================
               FADE IN
               ===================================== */

            setTimeout(() => {
                gif.classList.add("mostrar");
            }, 50);


            /* =====================================
               FADE OUT
               ===================================== */

            /*
               5000 = 5 segundos

               Altere esse número para controlar
               quanto tempo o GIF permanece visível.
            */

            tempoGif = setTimeout(() => {

                gif.classList.remove("mostrar");

            }, 5000);

        }

    </script>

</body>
</html>
"""


@app.route("/")
def inicio():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

