        <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>

<head>
    <title>Date</title>
    <link rel="stylesheet" href="/css/style.css" />
    <script type="text/javascript" src="/js/app.js"></script>
</head>
 
 <body>
 	<script>date();</script>
    <%-- <h5 class="text-center text-info" ><c:out value="${date}"/> </h5> --%>
     <h5 class="date" ><c:out value="${date}"></c:out></h5>
 </body>


