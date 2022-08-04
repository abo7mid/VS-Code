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
  <div class="container" >
  <h1 class="text-center">Here's Your Omikuji!</h1>
  <div class="bg-primary p-4 mx-auto w-50">
 		  <h3>In <c:out value="${number}"></c:out> 
		      years, you will live in <c:out value="${city}"></c:out>
		      with <c:out value="${name}"></c:out>
		      as your roommate, <c:out value="${hobby}"></c:out>
		      for a living. The next time you see a <c:out value="${living}"></c:out>
		      , you will have a good luck. Also, <c:out value="${say}"></c:out>.</h3> 
  </div>
  <div class="text-center p-5">
  <a href="/omikuji">Go Back</a>
  </div>
  </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
