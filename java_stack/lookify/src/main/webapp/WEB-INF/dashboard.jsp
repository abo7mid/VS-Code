<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Lookify!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
	<div class="container">
		<c:if test="${blank != null}">
	
	<p class="alert alert-danger text-center"><c:out value="${blank}"></c:out></p>
	</c:if>
		<div class="row">
			<div class="col-3">
				<a href="/songs/new">Add New</a>
			</div>
			<div class="d-flex col-3">
				<a href="/search/topTen">Top Songs</a>

			</div>

				<form class="d-flex col-6" action="/search" method="get">
					<div class="col mx-3">
						<input class="form-control" name="artist" type="text" placeholder="Search" />
					 
					 </div>
					 <div class="col">
						<input class="btn btn-primary" type="submit" value="Search Artitsts" />
					</div>
				</form>
		</div>
		<table class="table">
			<tr>
				<th>Name</th>
				<th>Rating</th>
				<th>Actions</th>
			</tr>
			<c:forEach items="${songs}" var="song">
				<tr>
					<td><a href="/songs/${song.id}"><c:out
								value="${song.name}"></c:out> </a></td>
					<td><c:out value="${song.rating}"></c:out></td>
					<td>
						<form action="/delete/${song.id}" method="post">
							<input type="submit" value="delete" class="btn btn-link" />
						</form>
					</td>
				</tr>
			</c:forEach>

		</table>
	</div>

	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
