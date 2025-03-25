# Nginx Reverse Proxy & Load Balancer Configuration

This repository contains my **Nginx configuration** for:
- ✅ Reverse Proxy
- ✅ Load Balancing
- ✅ Static File Handling
- ✅ URL Rewrites & Redirects
- ✅ Caching
- ✅ Variable Handling

## 📌 Features

### 1️⃣ Reverse Proxy
- Requests to `/server1/` are forwarded to `127.0.0.1:8000/`
- Requests to `/server2/` are forwarded to `127.0.0.1:5000/`
```nginx
location /server1/ {
    proxy_pass http://127.0.0.1:8000/;
}

location /server2/ {
    proxy_pass http://127.0.0.1:5000/;
}
```

### 2️⃣ Static File Hosting
- Serves files from `C:\Users\adars\htmlPrograms`
- `/uploads` and `/secondindex` mapped to different directories
```nginx
root C:\Users\adars\htmlPrograms;

location /uploads {
    root C:\Users\adars\htmlPrograms;
}

location /secondindex {
    alias C:\Users\adars\htmlPrograms\uploads;
}
```

### 3️⃣ Custom Index Page Handling
- `/firstindex` serves `index.html` if available, otherwise returns 404
```nginx
location /firstindex {
    root C:\Users\adars\htmlPrograms;
    try_files \index.html =404;
}
```

### 4️⃣ URL Redirects & Rewrites
- `/users` redirects to `/user` using **temporary (307) redirect**
```nginx
location = /users {
    return 307 /user;
}
```
- `/user` extracts query parameters and returns a response
```nginx
location = /user {
    set $username $arg_name;
    return 200 "host - $host\nuri - $uri\nargs - $username\n";
}
```

### 5️⃣ Caching for CSS, JS, and Images
```nginx
location ~* \.(css|js|jpg)$ {
    add_header Cache-control public;
    add_header Pragma public;
    add_header Vary Accept-Encoding;
    expires 1m;
}
```

---

## 🚀 How to Use
1. Install Nginx and Flask (`pip install flask`)
2. Run Flask servers on ports `8000` and `5000`
3. Start Nginx with this config
4. Test using:
   ```sh
   curl http://localhost:8080/server1/
   curl http://localhost:8080/server2/
   ```
    #Exact Port Numbers May Vary Check The Servers Source Code