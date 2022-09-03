<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Add Song</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>

	
	<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<div class="container">
			<div class="row mt-3">

	<div class="d-flex justify-content-end">

		<a href="/dashboard">Dashboard</a>
	</div>
			</div>

			<%@ page isErrorPage="true" %>  
			<form:form action="/songs/new" method="post" modelAttribute="song">

			<div class="mb-3">
				<label for="name" class="form-label">Title:</label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="name" />
				<form:errors path="name" cssClass="invalid-feedback" />
			</div>
			<div class="mb-3">
				<label for="artist" class="form-label">Artist</label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="artist" />
				<form:errors path="artist" cssClass="invalid-feedback" />
			</div>

			<div class="mb-3">
				<label for="rating" class="form-label">Rating(1-10):</label>
				<form:input type="number" value="1" min="1" max="10"  cssErrorClass="form-control is-invalid" cssClass="form-control" path="rating"></form:input>
				<form:errors path="rating" cssClass="invalid-feedback" />
			</div>
			
			<div class="d-flex justify-content-end">
				<button type="submit" class="btn btn-primary">Add Song</button>
			</div>
		</form:form>
</div>


	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
