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
    <title>Languages</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
<div class="container">
		<table class="table">
			<thead>
				<tr>
					<th>Name</th>
					<th>Creator</th>
					<th>Version</th>
					<th>Action</th>
				</tr>
			</thead>
			<tbody>
				<c:forEach items="${languages}" var="language">
				<tr>
						<td><a href="/languages/${language.id}"><c:out
									value="${language.name}"></c:out></a></td>
						<td><c:out value="${language.creator}"></c:out></td>
						<td><c:out value="${language.currentVersion}"></c:out></td>
						<td>
							<div class="row">
								<div class="col-3 mt-2 text-end">
									<a href="/languages/edit/${language.id}">Edit</a>
								</div>
								<div class="col-7 text-start">
									<form action="/languages/${language.id}" method="post">
										<input  type="submit" class="btn btn-link" value="Delete" />
									</form>
								</div>
							</div>
						</td>

					</tr>
				</c:forEach>
			</tbody>
		</table>
		
        <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>

<div class="container">
			<div class="row mt-3">
<!-- 				<div class="col-11">
					<h1 class="text-success">Edit expense</h1>

				</div>
				<div class="col">
					<a href="/expenses">Go Back</a>
				</div> -->
			</div>
<%-- 
			<%@ page isErrorPage="true" %>   --%>
			<form:form action="" method="post" modelAttribute="language">
<!-- 			<input type="hidden" name="_method" value="put"> -->
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
				<button type="submit" class="btn btn-primary">Create</button>
			</div>
		</form:form>
</div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
</div>
  </body>
</html>