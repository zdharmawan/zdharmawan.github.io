---
title: Simple REST API with NodeJS
tags: 'nodejs, rest, api'
date: 2016-06-16 04:07:26
---

A good backend starts with a good API being exposed to the outside world. 

##Prerequisite

- Installed NodeJS (with NPM)
- Git client

##Start
Start with creating a directory and do initialization

    mkdir simple-api-nodejs
    cd simple-api-nodejs
    npm init
    
This will ask few questions, in the end it will generate ```package.js```, which should look like this for me:

```javascript
{
  "name": "simple-api-nodejs",
  "version": "1.0.0",
  "description": "Simple exploratory code on how to make simple REST API with NodeJS",
  "main": "index.js",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/zdharmawan/simple-api-nodejs.git"
  },
  "author": "Zulfikar Dharmawan",
  "license": "ISC"
}
```
It'll ask for ```test```, let's skip that for now.
