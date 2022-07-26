<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>First JSP</title>
</head>
<body>
    <h1>Hello World!</h1>
    <h5>Name: <c:out value="${name}"/> </h5>
    <h5>Item name: <c:out value="${itemName}"/> </h5>
    <h5>Price: <c:out value="${price}"/></h5>
    <h5>Description: <c:out value="${description}"/></h5>
    <h5>Vendor:<c:out value="${vendor}"/></h5>
</body>
</head>