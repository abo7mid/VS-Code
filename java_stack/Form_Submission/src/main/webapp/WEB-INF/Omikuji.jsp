<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 5 Boilerplate</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
  <div class="container">
  <h1 class="text-center">Send an Omikuji!</h1>
  <form method="post">
  <div class="mb-3">
    <label for="number" class="form-label">Pick any number from 5 to 25:</label>
    <input type="number" min="5" max="25" class="form-control" id="number" name="number">
  </div>
  <div class="mb-3">
    <label for="city" class="form-label">Enter the name of any city:</label>
    <input type="text" class="form-control" id="city" name="city">
  </div>
  <div class="mb-3">
    <label for="name" class="form-label">Enter the name of any real person</label>
    <input type="text" class="form-control" id="name" name="name">
  </div>
  <div class="mb-3">
    <label for="hobby" class="form-label">Enter professional endeavor or hobby:</label>
    <input type="text" class="form-control" id="hobby" name="hobby">
  </div>
  <div class="mb-3">
    <label for="living" class="form-label">Enter any type of living thing:</label>
    <input type="text" class="form-control" id="living" name="living">
  </div>
  <div class="mb-3">
    <label for="say" class="form-label">Say something nice to someone:</label>
    <textarea style="resize:none;" class="form-control" id="say" name="say"></textarea>
  </div>

  <div class="mb-5">
  <h5>Send and show a friend</h5>
  </div>
  <div class="d-flex justify-content-end">
  <button type="submit" class="btn btn-primary">Send</button>
  </div>
</form>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </div>
  </body>
</html>
