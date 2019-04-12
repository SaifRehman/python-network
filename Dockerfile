FROM ubuntu

RUN apt-get update -yq && \
    apt-get upgrade -yq && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

RUN echo root:root | chpasswd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]