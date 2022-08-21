<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>${language.name}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
  
  <div class="mx-3 text-end ">
  <a href="/languages">Dashboard</a>
  </div>
  <div class="container">
  <p>${language.name}</p>
  <p>${language.creator}</p>
  <p>${language.currentVersion}</p>
  <div class="row mb-3 ">
  <a href="/languages/edit/${language.id}">Edit</a>
  </div>
  <form action="/languages/${language.id}" method="post">
  <div class="row">
     <button class="text-start btn btn-link" type="submit">Delete</button>
  </div>

  </form>

  </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>