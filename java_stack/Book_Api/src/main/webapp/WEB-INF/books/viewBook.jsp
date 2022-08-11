<html lang="en">
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>
<c:out value="${book.title}"></c:out>
</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet">
</head>

<body>
	<div class="container">
		<h1>All Books</h1>

					<h3>ID : <c:out value="${book.id}"></c:out></h3>
					<h3>Title : <c:out value="${book.title}"></c:out></h3>
					<h3>Number of Pages : <c:out value="${book.numberOfPages}"></c:out></h3>
					<h3>Language : <c:out value="${book.language}"></c:out></h3>

	</div>
	<script
		src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>