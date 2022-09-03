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
		<div class="row m-2">
			<div class="col-4">
				<p>Songs by artist : ${artist}</p>
			</div>


				<form class="d-flex col-7" action="/search" method="get">
					<div class="col mx-3">
						<input class="form-control" type="text" name="artist" placeholder="Search" />
					 
					 </div>
					 <div class="col">
						<input class="btn btn-primary" type="submit" value="New Search" />
					</div>
				</form>
				<a class="col-1" href="/dashboard">dashboard</a>
		</div>
<table class="table">
<tr>
<th>Name</th>
<th>Rating</th>
<th>Actions</th>
</tr>
<c:forEach items="${songs}" var="song">
<tr>
<td><a href="/songs/${song.id}"><c:out value="${song.name}"></c:out> </a></td>
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
