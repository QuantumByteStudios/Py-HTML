mainUI = '''

<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello World App</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">

  <style>
    body {
      background-color: #0F111A;
      color: white;
    }

    .myApp {
      width: 100vw;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .button-82-pushable {
      position: relative;
      border: none;
      background: transparent;
      padding: 0;
      cursor: pointer;
      outline-offset: 4px;
      transition: filter 250ms;
      user-select: none;
      -webkit-user-select: none;
      touch-action: manipulation;
    }

    .button-82-shadow {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border-radius: 12px;
      background: hsl(0deg 0% 0% / 0.25);
      will-change: transform;
      transform: translateY(2px);
      transition:
        transform 600ms cubic-bezier(.3, .7, .4, 1);
    }

    .button-82-edge {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      border-radius: 12px;
      background: linear-gradient(to left,
          hsl(340deg 100% 16%) 0%,
          hsl(340deg 100% 32%) 8%,
          hsl(340deg 100% 32%) 92%,
          hsl(340deg 100% 16%) 100%);
    }

    .button-82-front {
      display: block;
      position: relative;
      padding: 12px 27px;
      border-radius: 12px;
      font-size: 1.1rem;
      color: white;
      background: hsl(345deg 100% 47%);
      will-change: transform;
      transform: translateY(-4px);
      transition:
        transform 600ms cubic-bezier(.3, .7, .4, 1);
    }

    @media (min-width: 768px) {
      .button-82-front {
        font-size: 1.25rem;
      }
    }

    .button-82-pushable:hover {
      filter: brightness(110%);
      -webkit-filter: brightness(110%);
    }

    .button-82-pushable:hover .button-82-front {
      transform: translateY(-6px);
      transition:
        transform 250ms cubic-bezier(.3, .7, .4, 1.5);
    }

    .button-82-pushable:active .button-82-front {
      transform: translateY(-2px);
      transition: transform 34ms;
    }

    .button-82-pushable:hover .button-82-shadow {
      transform: translateY(4px);
      transition:
        transform 250ms cubic-bezier(.3, .7, .4, 1.5);
    }

    .button-82-pushable:active .button-82-shadow {
      transform: translateY(1px);
      transition: transform 34ms;
    }

    .button-82-pushable:focus:not(:focus-visible) {
      outline: none;
    }
  </style>

</head>

<body>

  <div class="myApp">
    <center>
      <h1>
        <span style="color: #82aaff;">printf</span>
        <span style="color: #ffcb6b;">(</span>
        <span style="color: #c3e88d;">"Hello World\n"</span>
        <span style="color: #ffcb6b;">);</span>
      </h1>
      <p>This app is completely useless.<br>To exit this application, click the button below.</p>

      <a href="?exit()">
        <button class="button-82-pushable" role="button">
          <span class="button-82-shadow"></span>
          <span class="button-82-edge"></span>
          <span class="button-82-front text">
            EXIT
          </span>

        </button>
      </a>

    </center>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2"
    crossorigin="anonymous"></script>
</body>

</html>

'''
