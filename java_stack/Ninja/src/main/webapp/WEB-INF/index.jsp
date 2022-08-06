<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Nijan Gold Game</title>
<link
	href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"
	rel="stylesheet">
</head>

<body>
	<div class="container">
		<div class="mb-3">
			<label>Your Gold:</label> <input type="text"
				value='<c:out value="${randomNum}"></c:out>' id="gold" name="gold">
		</div>
		<div class="row mb-5">

			<div class="col border text-center p-2">
				<form action="/farm" method="post">
					<label class="mb-3"> Farm<br>(earns 10-20 gold)
					</label> <br /> <input type="submit" name="farm" value="Find Gold!" />
				</form>
			</div>

			<div class="col border text-center p-2">
				<form action="/cave" method="post">
					<label class="mb-3"> Cave<br> (earns 10-20 gold)
					</label><br /> <input type="submit" name="cave" value="Find Gold!" />
				</form>
			</div>
			<div class="col border text-center p-2">
				<form action="/house" method="post">
					<label class="mb-3"> House<br> (earns 10-20 gold)
					</label><br /> <input type="submit" name="house" value="Find Gold!" />
				</form>
			</div>
			<div class="col border text-center p-2">
				<form action="/casino" method="post">
					<label class="mb-3"> Casino! <br />(earns/takes 0-50 gold)
					</label> <br /> <input type="submit" name="casino" value="Find Gold!" />
				</form>
			</div>

		</div>
		<div class="row">
			<h3>Activities :</h3>
		
				<c:choose>
					<c:when test="${sub}">
						<textarea class="text-danger" style="resize: none;"
							name="activities" cols="30" rows="10" id=""><c:out
								value="${message}"></c:out> <c:out
								value="${sub}"></c:out></textarea>
					</c:when>
					
					<c:otherwise>
						<textarea class="text-success" style="resize: none;"
							name="activities" cols="30" rows="10" id=""><c:out
								value="${message}"></c:out><c:out
								value="${sub}"></c:out></textarea>
					</c:otherwise>
				</c:choose>


		</div>
	</div>

	<script
		src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
