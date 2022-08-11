<html lang="en">
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>All Books</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet">
</head>

<body>
	<div class="container">
		<h1>All Books</h1>
		<c:if test="${bookNotFound != null}">
		<p class="alert alert-danger text-center"> <c:out value="${bookNotFound}"></c:out> </p>
		</c:if>
		<table class="table">
			<thead>
				<tr>
					<th>ID</th>
					<th>Title</th>
					<th>Language</th>
					<th># Pages</th>
				</tr>
			</thead>
			<tbody>
				<c:forEach items="${books}" var="book">
				<tr>
					<td><c:out value="${book.id}"></c:out></td>
					<td><a href='/books/<c:out value="${book.id}"></c:out>'><c:out value="${book.title}"></c:out></a></td>
					<td><c:out value="${book.language}"></c:out></td>
					<td><c:out value="${book.numberOfPages}"></c:out></td>
				</tr>
				</c:forEach>
			</tbody>
		</table>
	</div>
	<script
		src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>