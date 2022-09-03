<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>${song.name}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
  <div class="d-flex justify-content-end mt-3 mx-3">
  <a href="/dashboard">Dashboard</a>
  </div>
  <div class="container">

		<div class="row m-3">
			<div class="col">Title:</div>
			<div class="col">${song.name}</div>
		</div>
		<div class="row m-3">
			<div class="col">Artist:</div>
			<div class="col">${song.artist}</div>
		</div>
		<div class="row m-3">
			<div class="col">Rating(1-10)</div>
			<div class="col">${song.rating}</div>
		</div>

		<form  class="m-3" action="/delete/${song.id}" method="post">
		<input type="submit" value="Delete" class="btn btn-link"/>
		</form>
	</div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
