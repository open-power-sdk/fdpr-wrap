FROM ppc64le/fedora
RUN yum -y groupinstall "Development Tools"
RUN yum -y install fedora-packager rpmdevtools alien
CMD git clone https://github.com/rpsene/fdpr-wrap.git \
    cd ./fdpr-wrap \
    make \
    mkdir ./release \
    mv ./rpmbuild/RPMS/ppc64le/*.rpm ./release \
    cd ./release \
    alien *.rpm