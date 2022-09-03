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
  <div class="d-flex justify-content-end m-3">
  <a href="/dashboard">Dashboard</a>
  </div>
  <div class="container">
  <h1>Top Ten Songs</h1>
  <div class="m-3 border border-dark border-2">
  <c:forEach items="${songs}" var="song"> 
     <p class="m-3 border">
      ${song.rating} - <a href="/songs/${song.id}">${song.name}</a> - ${song.artist}
     </p>
  </c:forEach>
  </div>
  </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
