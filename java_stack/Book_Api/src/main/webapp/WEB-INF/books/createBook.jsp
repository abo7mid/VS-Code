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
  <h1 class="text-center">Create a Book</h1>
  <form method="post">
  <c:if test="${success != null}">
  <p class="alert alert-success text-center"><c:out value="${success}"></c:out> </p>
  </c:if>
  <div class="mb-3">
    <label for="title" class="form-label">Title:</label>
    <input type="text" class="form-control" id="title" name="title">
  </div>
  <div class="mb-3">
    <label for="lang" class="form-label">Language:</label>
    <input type="text" class="form-control" id="lang" name="lang">
  </div>
  <div class="mb-3">
    <label for="pages" class="form-label">Pages:</label>
    <input type="text" class="form-control" id="pages" name="pages">
  </div>
  <div class="mb-3">
    <label for="desc" class="form-label">Description:</label>
    <input type="text" class="form-control" id="desc" name="desc">
  </div>



  <div class="d-flex justify-content-end">
  <button type="submit" class="btn btn-primary">Create</button>
  </div>
</form>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </div>
  </body>
</html>