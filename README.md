# lab

Kubernetes app that verifies the source address of a header. Based on it, it returns 200 or 401

eg:
200
curl -X POST http://localhost:5000/verify -H "X-Forwarded-For: 150.222.81.1" -w "%{http_code}\n"
401
curl -X POST http://localhost:5000/verify -H "X-Forwarded-For: 150.222.86.1" -w "%{http_code}\n"

Application made by chatGPT with User-side prompt control ;)

Additionally, an element for kubernetes to make the application visible and accessible to other applications and has a pattern for minimal access protection.
