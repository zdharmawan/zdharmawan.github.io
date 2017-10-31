Title: Installing Java 8 on Ubuntu
Date: 2017-10-31 10:20
Category: Java
Tags: java8, ubuntu, install
Authors: Zul Dharmawan
Summary: Installing (latest) Java 8 on Ubuntu 
Status: published

Install Java 8 on Ubuntu:

1. Create a folder to put JDK

```
mkdir /opt/jdk
cd /opt
```

2. Download the latest JDK:

```
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.tar.gz
```

3. Extract it

```
tar -zxf jdk-8u152-linux-x64.tar.gz -C /opt/jdk
```

4. Set it as default

```
update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_152/bin/java 100
update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_152/bin/javac 100
```
