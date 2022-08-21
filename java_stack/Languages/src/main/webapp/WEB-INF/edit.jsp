<%-- <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
 --%>
 <!DOCTYPE html>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>${language.name}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
		
        <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<div class="container">
		<div class="row">
			<div class="text-end col-10">
				<form action="/languages/${language.id}" method="post">
					<button class="btn btn-link" type="submit">Delete</button>
				</form>
			</div>
			<div class="col mt-2">
				<a class="text-center" href="/languages">Dashboard</a>
			</div>
		</div>
		<%@ page isErrorPage="true" %>  
			<form:form action="/languages/edit/${language.id}" method="post" modelAttribute="language">
             <input type="hidden" name="_method" value="put">
		   <div class="mb-3">
				<form:label for="name" path="name" class="form-label">Name:</form:label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="name" />
				<form:errors path="name" cssClass="invalid-feedback" />
			</div>
			<div class="mb-3">
				<label for="creator" class="form-label">Creator:</label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="creator" />
				<form:errors path="creator" cssClass="invalid-feedback" />
			</div>
			<div class="mb-3">
				<label for="currentVersion" class="form-label">Version</label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="currentVersion" />
				<form:errors path="currentVersion" cssClass="invalid-feedback" />
			</div>


			
			<div class="d-flex justify-content-end">
				<button type="submit" class="btn btn-primary">Update</button>
			</div>
		</form:form>
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>

  </body>
</html>