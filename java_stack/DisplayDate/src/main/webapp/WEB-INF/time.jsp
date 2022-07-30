<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>


<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8" 
    import="java.util.Date" 
    import="java.text.SimpleDateFormat"
    import="java.time.LocalTime" %>

<head>
<title>Time</title>
 <link rel="stylesheet" href="/css/style.css" />
 <script src="/js/app.js" type="text/javascript"></script>
</head>


<body>
 	<script>time();</script>	
    <%-- <h5 class="text-center text-success align-middle" ><c:out value="${time}"/> </h5> --%>
     <h5 class="time" ><c:out value="${time}"/> </h5>
</body>
