FROM centos
ENV PROJECTNAME wechatAlert
ENV STATIC_PATH static

RUN yum install epel-release.noarch -y
RUN yum install python-pip gcc gcc++ python-devel.x86_64 mysql-devel -y
RUN python -m pip install "django<2"
RUN pip install uwsgi
RUN pip install requests itchat

RUN mkdir /opt/django/
ADD django.tar.gz /opt/django/

ENTRYPOINT python /opt/django/manage.py runserver 0.0.0.0:8001
