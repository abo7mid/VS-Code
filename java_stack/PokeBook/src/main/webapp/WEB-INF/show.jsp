<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Show Expense</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>

  <body>
  <div class="container">
		<div class="row mt-5">
			<div class="col-11">
				<h1 class="text-primary">Expense Details</h1>
			</div>
			<div class="col">
				<a href="/expenses">Go back</a>
			</div>
		</div>
		<div class="row mx-5 mt-3">
			<p>Expense Name: ${poke.expense}</p>
			<p>Expense Description: ${poke.description}</p>
			<p>Vendor: ${poke.vendor}</p>
			<p>Amount Spent: ${poke.amount}</p>
		</div>

		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"></script>
  </div>
  </body>
</html>
