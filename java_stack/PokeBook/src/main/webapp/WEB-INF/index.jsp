<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>PokeBook</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet">
</head>
<body>
	<div class="container">
		<h1 class="text-primary">View All expenses</h1>
		<table class="table">
			<thead>
				<tr>
					<th>Expense</th>
					<th>Vendor</th>
					<th>Amount</th>
					<th>Actions</th>
				</tr>
			</thead>
			<tbody>
				<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
				<c:forEach items="${poke1}" var="poke">
					<tr>
						<td><a href="/expenses/${poke.id}"><c:out value="${poke.expense}"></c:out></a></td>
						<td><c:out value="${poke.vendor}"></c:out></td>
						<td><c:out value="${poke.amount}"></c:out></td>
						<td><div class="row">
								<div class="col-3">
									<a class="" href="expenses/edit/${poke.id}">edit</a>
								</div>
								<%-- <div class="col">
								<a class="btn btn-danger" href="expenses/delete/${poke.id}">delete</a>
						       </div> --%>

								<div class="col">
									<form action="expenses/delete/${poke.id}" method="post">
									<input type="hidden" name="_method" value="delete" />
										<div class="">
											<!-- <button type="submit" class="btn btn-danger">Delete</button> -->
											<input class="btn btn-danger" type="submit" value="Delete" />
										</div>
									</form>
								</div>

							</div></td>
					</tr>
				</c:forEach>
			</tbody>
		</table>
		<%@ taglib prefix="form"
			uri="http://www.springframework.org/tags/form"%>


<div class="container">
			<h1 class="text-primary">Track an expense</h1>
			<c:if test="${created != null}">
				<p class="alert alert-success text-center">
					<c:out value="${created}"></c:out>
				</p>
			</c:if>
			<c:if test="${updated != null}">
				<p class="alert alert-success text-center">
					<c:out value="${updated}"></c:out>
				</p>
			</c:if>
			<c:if test="${deleted != null}">
				<p class="alert alert-success text-center">
					<c:out value="${deleted}"></c:out>
				</p>
			</c:if>
			<form:form action="/expenses" method="post" modelAttribute="poke">
			<!-- <input type="hidden" name="_method" value="put"> -->
			<div class="mb-3">
				<form:label for="expense" path="expense" class="form-label">Expense Name:</form:label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="expense" />
				<form:errors path="expense" cssClass="invalid-feedback" />
			</div>
			<div class="mb-3">
				<label for="vendor" class="form-label">Vendor:</label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="vendor" />
				<form:errors path="vendor" cssClass="invalid-feedback" />
			</div>
			<div class="mb-3">
				<label for="amount" class="form-label">Amount</label>
				<form:input type="text" cssErrorClass="form-control is-invalid" cssClass="form-control" path="amount" />
				<form:errors path="amount" cssClass="invalid-feedback" />
			</div>

			<div class="mb-3">
				<label for="description" class="form-label">Description:</label>
				<form:textarea style="resize:none;" cssErrorClass="form-control is-invalid" cssClass="form-control" path="description"></form:textarea>
				<form:errors path="description" cssClass="invalid-feedback" />
			</div>
			
			<div class="d-flex justify-content-end">
				<button type="submit" class="btn btn-primary">Create</button>
			</div>
		</form:form>
</div>

		<script
			src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
	</div>
</body>
</html>


