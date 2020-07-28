<html>

<head>
    <title>{{title}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/styles/main.css" />
    <link rel="stylesheet" href="/styles/home.css" />
    <link rel="stylesheet" href="/styles/results.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script>
        function enableStyle(id) {
            var element = document.getElementById(id);
            element.className = element.className.replace(/\bdisabled\b/g, "");
        }

        function goHome() {
            window.location = '/';
        }

        function closeModal() {
            var span = document.getElementsByClassName("close")[0];
            var modal = document.getElementById("errorModal");
            modal.style.display = "none";
        }
    </script>
</head>

<body>
    <div id="main_container">
        {{!base}}
    </div>
</body>

</html>