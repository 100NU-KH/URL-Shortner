# URL Shortner 

This application generates short URL for the provided URL in request.

```mermaid
---
title: Creation flow
---
graph LR
    A[Receive-destination-url] --> B[Application]
    B[Application] --> C[return-tiny-url]
```

   
- The destination url is saved in DB along with the returned tiny URL

```mermaid
---
title: Redirection flow
---
graph LR
    A[Receive-tiny-url] --> B{condition}
    B --> C[redirect-to-destination-url]
    B --> D[Error-if-invalid-url]

```

- Received tiny URL is used to fetch the destination URL via the `hash-str` present in the tiny-url. 