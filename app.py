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

            /*
                Permite que o GIF fique
                dentro da caixa.
            */

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

            /*
                Faz o GIF preencher
                toda a caixa.
            */

            object-fit: cover;

            /*
                GIF fica atrás
                dos textos.
            */

            z-index: 0;

            /*
                Começa invisível.
            */

            opacity: 0;

            pointer-events: none;

            /*
                Fade-in e fade-out
                de 1 segundo.
            */

            transition: opacity 1s ease;

        }



        /* =========================================
           GIF VISÍVEL
           ========================================= */

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
           TÍTULO + SUBTÍTULO + BOTÃO
           ========================================= */

        #inicio {

            opacity: 1;

            /*
                Controla o fade-in
                e fade-out de todos
                os elementos iniciais.
            */

            transition: opacity 1s ease;

        }



        /*
            Quando recebe "esconder",
            título, subtítulo e botão
            desaparecem.
        */

        #inicio.esconder {

            opacity: 0;

            /*
                Impede que o botão
                seja clicado enquanto
                estiver invisível.
            */

            pointer-events: none;

        }



        /* =========================================
           TÍTULO
           ========================================= */

        h1 {

            color: #00FF00;

            margin-top: 0;

            margin-bottom: 8px;

        }



        /* =========================================
           SUBTÍTULO
           ========================================= */

        #subtitulo {

            color: #000000;

            font-size: 15px;

            font-weight: normal;

            margin-top: 0;

            margin-bottom: 10px;

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

        }



        /* =========================================
           ANIMAÇÃO DE ENTRADA DA FRASE
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



        /* =========================================
           ANIMAÇÃO DE SAÍDA DA FRASE
           ========================================= */

        #frase.esconder {

            animation: desaparecer 1s ease forwards;

        }



        @keyframes desaparecer {

            0% {

                opacity: 1;

                transform: translateY(0) scale(1);

            }


            100% {

                opacity: 0;

                transform: translateY(-20px) scale(0.9);

            }

        }

    </style>

</head>



<body>


    <!-- =========================================
         CAIXA PRINCIPAL
         ========================================= -->

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


            <!-- =================================
                 TÍTULO + SUBTÍTULO + BOTÃO
                 ================================= -->

            <div id="inicio">


                <h1>
                    Clica Ai
                </h1>


                <!-- SUBTÍTULO -->

                <div id="subtitulo">

                    o quase homem que fez com seu estagiario

                </div>


                <button onclick="mostrarFrase()">

                    Aqui

                </button>


            </div>



            <!-- =================================
                 FRASE
                 ================================= -->

            <div id="frase">

                Voce é perfeita &lt;3

            </div>


        </div>


    </div>



    <script>


        /* =========================================
           TEMPORIZADOR DO GIF
           ========================================= */

        let tempoGif;



        /* =========================================
           FUNÇÃO PRINCIPAL
           ========================================= */

        function mostrarFrase() {


            /*
                Seleciona os elementos
                que serão controlados.
            */

            const frase =
                document.getElementById("frase");

            const gif =
                document.getElementById("gifFundo");

            const inicio =
                document.getElementById("inicio");



            /* =====================================
               CANCELA TEMPORIZADOR ANTERIOR
               ===================================== */

            clearTimeout(tempoGif);



            /* =====================================
               ESCONDE:
               
               - Título
               - Subtítulo
               - Botão
               ===================================== */

            inicio.classList.add("esconder");



            /* =====================================
               REINICIA A FRASE
               ===================================== */

            frase.classList.remove("mostrar");

            frase.classList.remove("esconder");


            /*
                Força o navegador a
                reiniciar a animação.
            */

            void frase.offsetWidth;


            /*
                Faz a frase aparecer.
            */

            frase.classList.add("mostrar");



            /* =====================================
               REINICIA O GIF
               ===================================== */

            /*
                Primeiro remove o fade-in.
            */

            gif.classList.remove("mostrar");


            /*
                Remove o GIF temporariamente.
            */

            gif.src = "";


            /*
                Força o navegador
                a processar a alteração.
            */

            void gif.offsetWidth;


            /*
                Coloca o GIF novamente.

                Isso faz a animação começar
                novamente do primeiro frame.
            */

            gif.src = "/static/flower.gif";



            /* =====================================
               FADE-IN DO GIF
               ===================================== */

            setTimeout(() => {

                gif.classList.add("mostrar");

            }, 50);



            /* =====================================
               TEMPO DO GIF
               ===================================== */

            /*
                5000 = 5 segundos.

                Você pode alterar para:

                3000 = 3 segundos
                5000 = 5 segundos
                8000 = 8 segundos
                10000 = 10 segundos
            */

            tempoGif = setTimeout(() => {


                /* ================================
                   FADE-OUT DO GIF
                   ================================ */

                gif.classList.remove("mostrar");



                /* ================================
                   FADE-OUT DA FRASE
                   ================================ */

                frase.classList.remove("mostrar");

                frase.classList.add("esconder");



                /* ================================
                   ESPERA O FADE-OUT TERMINAR
                   ================================ */

                setTimeout(() => {


                    /*
                        Faz título,
                        subtítulo e botão
                        aparecerem novamente.
                    */

                    inicio.classList.remove("esconder");


                }, 1000);


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

    app.run(
        host="0.0.0.0",
        port=5000
    )