FROM centos:7

WORKDIR /app

COPY gvsu.conf .
COPY start.sh .

ARG DOWNLOAD_URL=http://192.168.1.13:8000

RUN yum update -y && \
	yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
	yum install -y httpd mod_ssl mod_wsgi python-pip vim && \
	curl $DOWNLOAD_URL/oracle-instantclient18.5-basiclite-18.5.0.0.0-3.x86_64.rpm -o basiclite.rpm && \
	yum install -y basiclite.rpm && \
	rm basiclite.rpm && \
	echo "/usr/lib/oracle/18.5/client64/lib" > /etc/ld.so.conf.d/oracle-instantclient.conf && \
	ldconfig && \
	mkdir -p /www/{gvsu,logs} && \
	rm -f /etc/localtime && \
	ln -sf /usr/share/zoneinfo/US/Estern /etc/localtime && \
	chown apache:apache /www/gvsu && \
	chmod 2765 /www/gvsu && \
	useradd flask && \
	mv gvsu.conf /etc/httpd/conf.d/. && \
	pip install --upgrade pip && \
	pip install flask cx_Oracle && \
	chmod +x /app/start.sh && \
	yum clean all && \
	rm -rf /var/cache/yum && \
	rm -rf /tmp/**

EXPOSE 80
EXPOSE 443

CMD ["/app/start.sh"]
